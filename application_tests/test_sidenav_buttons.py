from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import selenium
import unittest, time


class ButtonsTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(3)
		self.base_url = "http://technetium.herokuapp.com"
		self.b_login = False

		driver = self.driver
		driver.get(self.base_url + "/")
#		WebDriverWait(driver, 10).until(EC.title_contains("Technetium"))

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
				self.b_login = True

				print "Test login resulting in target page with title: ", driver.title
				# wait 3 seconds to show the correct page being loaded before quitting the browser
				time.sleep(3)

			except:
				print "Exception: login failed"
	


	def test_dashboard_button(self):
		"""
		tests dashboard button after login
		"""

		b = False
		driver = self.driver

		link_element = driver.find_element_by_partial_link_text("Dashboard")
		if link_element is not None:
			link_element.click()
			WebDriverWait(driver, 10).until(EC.title_contains("Technetium"))			
			h2_elements = driver.find_elements_by_tag_name("h2")
			for element in h2_elements:
				if "Technetium Dashboard" in element.text:
					b = True
					break

		# wait 3 seconds to show the correct page being loaded
		time.sleep(3)

		self.assertTrue(b)


	def test_issue_tracker_button(self):
		"""
		tests dashboard button after login
		"""

		b = False
		driver = self.driver

		link_element = driver.find_element_by_partial_link_text("Issue Tracker")
		if link_element is not None:
			link_element.click()
			WebDriverWait(driver, 10).until(EC.title_contains("Technetium"))			
			h2_elements = driver.find_elements_by_tag_name("h2")
			for element in h2_elements:
				if "Issue Tracker" in element.text:
					b = True
					break

		# wait 3 seconds to show the correct page being loaded
		time.sleep(3)

		self.assertTrue(b)


	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()