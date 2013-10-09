from components.green_light import GreenLight
from components.movement_sensor import MovementSensor

movement_sensor = MovementSensor()
green_light = GreenLight()

movement_sensor.turn_sensor_on(green_light.blink_once)
while True:
	pass
