from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest, time


class LogoutTest(unittest.TestCase):
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
	

	def test_logout(self):
		"""
		Test to logout of technetium
		"""

		driver = self.driver
		b = False
		path_element = driver.find_element_by_xpath("//span[contains(@class, 'glyphicon-user')]")
		if path_element is not None:
			path_element.click()
			WebDriverWait(driver, 10)
			link_element = driver.find_element_by_partial_link_text("Log out")
			if link_element is not None:
				link_element.click()
				WebDriverWait(driver, 10).until(EC.title_contains("Technetium"))			
				p_elements = driver.find_elements_by_tag_name("p")
				for element in p_elements:
					if "Please sign in to continue" in element.text:
						b = True
						break		

		# wait 3 seconds to show the correct page being loaded
		time.sleep(3)

		self.assertTrue(b)


	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()		