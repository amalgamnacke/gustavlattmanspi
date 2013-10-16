#import imp

#Use imp to import full file system paths
#movement_sensor = imp.load_source("MovementSensorDaemon", "/home/pi/python_scripts/movement_sensor.py")

import sys#, daemon

sys.path.append("/home/pi/python_scripts")
import movement_sensor

#Calls
#with daemon.DaemonContext():
movement_sensor.run()

