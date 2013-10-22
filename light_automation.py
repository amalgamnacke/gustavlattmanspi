from components.green_light import GreenLight
from components.movement_sensor import MovementSensor
from components.light_automation import LightAutomation
import time

def run():
	movement_sensor = MovementSensor()
	green_light = GreenLight()
	light_automation = LightAutomation()

	light_automation.turn_light_module_on()

	while True:
		pass
