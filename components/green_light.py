import RPi.GPIO as GPIO
import time

class GreenLight:
	def __init__(self):
		self.pin_nr = 22		
		self.blink_time = 0.1

		GPIO.setup(self.pin_nr, GPIO.OUT)

	#Creates a single light blink
	def blink_once(self):
		GPIO.output(self.pin_nr, True)
		time.sleep(self.blink_time)
		GPIO.output(self.pin_nr, False)

	#Creates X amount of light blinks
	def blink(self, blink_amount):
		for i in range(0, blink_amount):
			GPIO.output(self.pin_nr, True)
			time.sleep(self.blink_time)
			GPIO.output(self.pin_nr, False)
			time.sleep(self.blink_time)		

	#Turn the light ON
	def turn_ons(self):
		GPIO.output(self.pin_nr, True)

	#Turn the light OFF
	def turn_off(self):
		GPIO.output(self.pin_nr, False)
