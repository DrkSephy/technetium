from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest, time

class LoginTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(3)
		
		# set b_local true to test locally
		b_local = False
		if b_local:
			self.base_url = "http://localhost:8000"
		else:
			self.base_url = "http://technetium.herokuapp.com"


	def test_login(self):
		"""
		Test to login to technetium
		"""
		b = False
		driver = self.driver
		driver.get(self.base_url + "/")

		link_element = driver.find_element_by_partial_link_text("Sign in with Bitbucket")
		if link_element is not None:
			link_element.click()
		
			title = ""
			try:
				# wait for the page to refresh
				WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_name("submit"))
				submit_element = driver.find_element_by_name("submit")

				username_element = driver.find_element_by_name("username")
				password_element = driver.find_element_by_name("password")

				username = "technetiumtest"
				password = "zaq1xsw2"
				username_element.send_keys(username)
				password_element.send_keys(password)

				submit_element.click()
				WebDriverWait(driver, 10).until(EC.title_contains("Technetium"))
				b = True

				print "Test login resulting in target page with title: ", driver.title
				# wait 3 seconds to show the correct page being loaded before quitting the browser
				time.sleep(3)

			except:
				print "Test login failed"
	
		self.assertTrue(b)


	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()