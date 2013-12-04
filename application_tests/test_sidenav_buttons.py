from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest, time


class SidenavButtonsTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Firefox()
		self.driver.implicitly_wait(3)

		username = "technetiumtest"
		password = "zaq1xsw2"

		# set b_local true to test locally
		b_local = False
		if b_local:
			base_url = "http://localhost:8000"
		else:
			base_url = "http://technetium.herokuapp.com"

		driver = self.driver
		driver.get(base_url + "/")
#		WebDriverWait(driver, 10).until(EC.title_contains("Technetium"))

		link_element = driver.find_element_by_partial_link_text("Sign in with Bitbucket")
		if link_element is not None:
			link_element.click()

			try:
				# wait for the page to refresh
				WebDriverWait(driver, 10).until(lambda driver : driver.find_element_by_name("submit"))
				submit_element = driver.find_element_by_name("submit")

				username_element = driver.find_element_by_name("username")
				password_element = driver.find_element_by_name("password")

				username_element.send_keys(username)
				password_element.send_keys(password)

				submit_element.click()
				WebDriverWait(driver, 10).until(EC.title_contains("Technetium"))

#				print "Setup Login to: ", driver.title
				# wait 3 seconds to show the correct page being loaded before quitting the browser
#				time.sleep(3)

			except:
				print "Setup Login failed"
	

	def test_home_button(self):
		"""
		tests Home button after login
		"""

		b = False
		driver = self.driver

		link_element = driver.find_element_by_partial_link_text("Home")
		if link_element is not None:
			link_element.click()
			WebDriverWait(driver, 10).until(EC.title_contains("Technetium"))			
			h1_elements = driver.find_elements_by_tag_name("h1")
			for element in h1_elements:
				if "Welcome to Technetium!" in element.text:
					b = True
					break

		# wait 3 seconds to show the correct page being loaded
		time.sleep(3)

		self.assertTrue(b)


	def test_issue_tracker_button(self):
		"""
		tests Issue Tracker button after login
		"""

		b = False
		driver = self.driver

		link_element = driver.find_element_by_partial_link_text("Issue Tracker")
		if link_element is not None:
			link_element.click()
			WebDriverWait(driver, 10).until(EC.title_contains("Technetium"))			
			h2_elements = driver.find_elements_by_tag_name("h2")
			for element in h2_elements:
				if "Technetium Issue Tracker" in element.text:
					b = True
					break

		# wait 3 seconds to show the correct page being loaded
		time.sleep(3)

		self.assertTrue(b)


	def test_subscriptions_button(self):
		"""
		tests Subscriptions button after login
		"""

		b = False
		driver = self.driver

		link_element = driver.find_element_by_partial_link_text("Subscriptions")
		if link_element is not None:
			link_element.click()
			WebDriverWait(driver, 10).until(EC.title_contains("Technetium"))			
			h2_elements = driver.find_elements_by_tag_name("h2")
			for element in h2_elements:
				if "Manage Repository Subscriptions" in element.text:
					b = True
					break

		# wait 3 seconds to show the correct page being loaded
		time.sleep(3)

		self.assertTrue(b)


	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()