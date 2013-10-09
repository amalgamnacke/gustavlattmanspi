import RPi.GPIO as GPIO
import time, threading

class MovementSensor(threading.Thread):
	def __init__(self):
		self.pin_nr = 18
		self.sleep_time = 0.1
		self.sensor_running = False

		GPIO.setup(self.pin_nr, GPIO.IN)

	#Turns the sensor ON
	def turn_sensor_on(self, callback_function):
		self.sensor_running = True
		while self.sensor_running:
			if GPIO.input(self.pin_nr):
				callback_function()
			time.sleep(self.sleep_time)

	#Turns the sensor OFF
	def turn_sensor_off(self):
		self.sensor_running = False
