import RPi.GPIO as GPIO
import time
from lxml import etree

from http_scraper import HttpScraper

MODE_ALL_OFF = 0
MODE_ALL_ON = 1
MODE_DAYLIGHT_AUTO = 2
MODE_ECO_AUTO = 3

class LightAutomation:
	def __init__(self):
		self.is_light_module_turned_on = False
		self.modes = MODE_ECO_AUTO
		
		self.http_scraper = HttpScraper()

		self.fallback_sunrise = "07:30" 
		self.fallback_sunset = "17:55"
		
		self.fetched_sun_time = self.http_scraper.scrape_vackertvader()
		if not self.fetched_sun_time:
			self.fetched_sun_time = [self.fallback_sunrise, self.fallback_sunset]	
		
		self.sunrise = self.fetched_sun_time[0]
		self.sunset = self.fetched_sun_time[1]
	
	# Fetches fresch daylight data
	def update_sun_time(self):
		self.fetched_sun_time = self.http_scraper.scrape_vackertvader()
		if not self.fetched_sun_time:
			self.fetched_sun_time = [self.fallback_sunrise, self.fallback_sunset]
		
		self.sunrise = self.fetched_sun_time[0]
		self.sunset = self.fetched_sun_time[1]

	# Will return false if current time is between sunrise and sunset
	def time_to_light_up(self):
		timestamp = time.gmtime()
		
		#before sunrise
		isBeforeSunrise = timestamp.tm_hour == self.sunrise.tm_hour and timestamp.tm_min <= self.sunrise.tm_min
		isBeforeSunrise = isBeforeSunrise or timestamp.tm_hour < self.sunrise.tm_hour

		#after sunset
		isAfterSunset = timestamp.tm_hour == self.sunset.tm_hour and timestamp.tm_min >= self.sunset.tm_min
		isAfterSunset = isAfterSunset or timestamp.tm_hour > self.sunset.tm_hour

		if isBeforeSunrise or isAfterSunset:
			return True
		else:
			return False

	def turn_light_module_on(self):
		self.is_light_module_turned_on = true
		while self.is_light_module_turned_on:

			# Exit this loop
			if MODE_ALL_OFF == self.modes:
				self.is_light_module_turned_on = false
				continue
			
			# Be sure to turn on all lights at 100Â%
			if MODE_ALL_ON == self.modes:
				#relay module, light all up if not lighted up already
				continue
			
			if MODE_DAYLIGHT_AUTO == self.modes:
				#asd
				pass
	
