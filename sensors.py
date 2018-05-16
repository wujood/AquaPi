#import RPi.GPIO as GPIO
import threading
import time
import sys
sys.path.insert(0, './Client')
import swagger_client

# ~ #How much time between sensor-reads in seconds
# ~ PERIOD_WATER_LVL=10
# ~ PERIOD_BRIGHTNESS=60

# ~ ### GPIO SETUP ###
# ~ GPIO.setmode(GPIO.BCM)`
# ~ #Water level sensor
# ~ INP_WATERLVL_GPIO=4
# ~ GPIO.setup(INP_WATERLVL_GPIO, GPIO.IN)
# ~ #Brightness sensor
# ~ INP_BRIGHTNESS_GPIO=17
# ~ GPIO.setup(INP_BRIGHTNESS_GPIO, GPIO.IN)
# ~ #Relais for light (using Normally-Open-mode (NO))
# ~ RELAY_LIGHT_GPIO=27
# ~ GPIO.setup(RELAY_LIGHT_GPIO, GPIO.OUT)
# ~ GPIO.output(RELAY_LIGHT_GPIO, GPIO.LOW)

client=swagger_client.api_client.ApiClient()
client.


# ~ def read_water_lvl():
	
	# ~ threading.Timer(PERIOD_WATER_LVL,read_water_lvl).start()

# ~ def read_brightness():
	
	# ~ threading.Timer(PERIOD_BRIGHTNESS,read_brightness).start()

# ~ def switch_light(on):
	# ~ if on:
		# ~ GPIO.output(RELAY_LIGHT_GPIO, GPIO.HIGH)
	# ~ else:
		# ~ GPIO.output(RELAY_LIGHT_GPIO, GPIO.LOW)

# ~ GPIO.cleanup()  
