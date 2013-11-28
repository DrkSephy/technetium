from selenium import selenium
import unittest, time

class LogoutTest(unittest.TestCase):
	def setUp(self):
		self.selenium = selenium("localhost", 4444, "*firefox", "http://technetium.herokuapp.com")
		self.selenium.start()

	def test_logout(self):
		"""
		Test to logout to technetium
		"""
		sel = self.selenium
		sel.click(link="logout")
		sel.wait_for_page_to_load("30000")

	def tearDown(self):
		self.selenium.stop()

if __name__ == "__main__":
	unittest.main()		