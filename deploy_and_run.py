import os
RPI_IP='192.168.2.235'

os.system('scp sensors.py pi@'+RPI_IP+':/home/pi/')
os.system('ssh pi@'+RPI_IP+' "python3 sensors.py"')

