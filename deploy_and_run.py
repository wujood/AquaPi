import os
RPI_IP='192.168.8.234'

os.system('scp sensors.py pi@'+RPI_IP+':/home/pi/')
os.system('ssh -t pi@'+RPI_IP+' "python3 sensors.py"')
