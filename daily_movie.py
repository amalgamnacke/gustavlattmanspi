from http_scraper import HttpScraper

class DailyMovie:
	def __init__(self):
		self.debugMode = True
		self.scraper = HttpScraper()

		self.base_url_tpb = "thepiratebay.sx"
		self.base_page_tpb = "/user/"
		self.users_tpb = ["BOZX"]

	def debug(self, msg):
		if self.debugMode: print msg

	def get_current_page_titles_tpb(self, user):
		self.debug("Scraping: " + self.base_url_tpb + self.base_page_tpb + user + "...")
		raw_html = self.scraper.scrape(self.base_url_tpb, self.base_page_tpb + user, "a.detLink")
		self.debug("Got " + str(len(raw_html)) + " titles.")

				
		raw_html[0].getparent().getnext().get("href")
			
a = DailyMovie()
a.get_current_page_titles_tpb("BOZX")

