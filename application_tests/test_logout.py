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
		

	def tearDown(self):
		self.selenium.stop()

if __name__ == "__main__":
	unittest.main()		