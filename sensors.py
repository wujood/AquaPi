import RPi.GPIO as GPIO
import threading
import time
import sys
import spidev
from statistics import median

sys.path.insert(0, './api')
import swagger_client

### GPIO SETUP ###
GPIO.setmode(GPIO.BCM)

### DIGITAL ###

#SERVO
OUT_SERVO=26
GPIO.setup(OUT_SERVO, GPIO.OUT)
GPIO.output(OUT_SERVO, GPIO.LOW)

#Light barrier
INP_LIGHT_BARRIER=6
GPIO.setup(INP_LIGHT_BARRIER, GPIO.IN)

#LED 
OUT_LED=14
GPIO.setup(OUT_LED, GPIO.OUT)
GPIO.output(OUT_LED, GPIO.HIGH)

#RELAY
OUT_RELAY=4
GPIO.setup(OUT_RELAY, GPIO.OUT)
GPIO.output(OUT_RELAY, GPIO.HIGH)

### ANALOG ###

#Temperature
INP_TEMP_WATER=0
INP_TEMP_AIR=2

#Water level sensor
INP_WATERLVL=5

#Brightness sensor
INP_BRIGHTNESS=6

mosipin=10
misopin=9
cspin=8
clockpin=11
GPIO.setup(mosipin, GPIO.OUT)
GPIO.setup(misopin, GPIO.IN)
GPIO.setup(cspin, GPIO.OUT)
GPIO.setup(clockpin, GPIO.OUT)

def readadc(adcnum):
	if ((adcnum > 7) or (adcnum < 0)):
			return -1
	GPIO.output(cspin, True)  

	GPIO.output(clockpin, False)  # start clock low
	GPIO.output(cspin, False)     # bring CS low

	commandout = adcnum
	commandout |= 0x18  # start bit + single-ended bit
	commandout <<= 3    # we only need to send 5 bits here
	for i in range(5):
		if (commandout & 0x80):
				GPIO.output(mosipin, True)
		else:
				GPIO.output(mosipin, False)
		commandout <<= 1
		GPIO.output(clockpin, True)
		GPIO.output(clockpin, False)

	adcout = 0
	# read in one empty bit, one null bit and 10 ADC bits
	for i in range(12):
		GPIO.output(clockpin, True)
		GPIO.output(clockpin, False)
		adcout <<= 1
		if (GPIO.input(misopin)):
			adcout |= 0x1

	GPIO.output(cspin, True)
	
	adcout >>= 1       # first bit is 'null' so drop it
	return adcout


sample_size=50
sensor_data=[None]*sample_size
def smooth_sensor_read(analog_input_pin):
	for i in range(sample_size):
		sensor_data[i]=readadc(analog_input_pin)
	return median(sensor_data)

spi = spidev.SpiDev()
spi.open(0,0)
# ~ client=swagger_client.api_client.ApiClient()
def read_brightness():
	return smooth_sensor_read(INP_BRIGHTNESS)

def read_temperature_air():
	return smooth_sensor_read(INP_TEMP_AIR)

def read_temperature_water():
	return smooth_sensor_read(INP_TEMP_WATER)

def read_water_lvl():
	return smooth_sensor_read(INP_WATERLVL)

def switch_light(on):
	if on:
		GPIO.output(RELAY_LIGHT, GPIO.HIGH)
	else:
		GPIO.output(RELAY_LIGHT, GPIO.LOW)
		
def read_light_barrier():
	return GPIO.input(INP_TEMP)

def useComponentSettings(componentSettings):
	if(componentSettings.feeder == 1):
		GPIO.output(OUT_SERVO, GPIO.HIGH)
	else:
		GPIO.output(OUT_SERVO, GPIO.LOW)
	if(componentSettings.lamp == 1):
		GPIO.output(OUT_LED, GPIO.HIGH)
		GPIO.output(OUT_RELAY, GPIO.HIGH)
	else:
		GPIO.output(OUT_LED, GPIO.LOW)
		GPIO.output(OUT_RELAY, GPIO.LOW)
	
	return


try:
	api = swagger_client.apis.ComponentSettingsApi()
	while 1:
		time.sleep(1)
		request = swagger_client.models.ComponentSettings('Fibonacci')
		request.feeder = swagger_client.models.Feeder(0, '')
		request.waterlevelsensor = swagger_client.models.WaterLevelSensor(read_water_lvl(), '')
		request.pump = swagger_client.models.Pump(0, '')
		request.lamp = swagger_client.models.Lamp(0, '')
		request.waterthermometer = swagger_client.models.Thermometer(read_temperature_water(), '')
		request.airthermometer = swagger_client.models.Thermometer(read_temperature_air(), '')
		request.lightsensor = swagger_client.models.LightSensor(read_brightness(), '')
		request.waterflowsensor = swagger_client.models.WaterFlowSensor(0, '')

		api.put_component_settings(request)
		filter = swagger_client.models.ParamComponentSettingsPost('Fibonacci')
		response = api.post_component_settings(filter)
		useComponentSettings(response[0])
		print('------------------------------------')
		print('Helligkeit:\t\t',read_brightness())
		print('Wasserstand:\t\t',read_water_lvl())
		print('Lufttemperatur:\t\t',read_temperature_air())
		print('Wassertemperatur:\t',read_temperature_water())
except KeyboardInterrupt:
    pass
finally:
	GPIO.cleanup()  
