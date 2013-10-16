import RPi.GPIO as GPIO
import time
from lxml import etree

from http_scraper import HttpScraper

class LightAutomation:
	def __init__(self):		
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
	
		timestamp = time.gmtime()
		,2h
	def time_to_light_up(self):
		timestamp = time.gmtime()
		
		#before sunrise
		if timestamp.tm_hour <= self.sunrise.tm_hour and timestamp tm_min

	def turn_light_module_on(self):
		#kolla hur movement_.py hpysslar
		pass
		
