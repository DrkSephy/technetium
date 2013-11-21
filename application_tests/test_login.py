from selenium import webdriver
import unittest

class LoginTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		#self.base_url = "http://locahost:8000"
		self.base_url = "http://technetium.herokuapp.com"

	def test_login(self):
		"""
		Test to login to technetium
		"""
		driver = self.driver
		driver.get(self.base_url + "/")
		


	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()