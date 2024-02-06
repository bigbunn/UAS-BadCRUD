import unittest
import os
import random
import string
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class UpdateContactTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('--headless')
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        server = 'http://localhost:4444'

        self.browser = webdriver.Remote(command_executor=server,options=options)

        try:
            self.url = os.environ['URL']
        except:
            self.url = "http://localhost"    

    def test_update_contact(self):
        expected_result = "Halo, admin"
        self.browser.get(self.url + '/login.php')
        self.browser.find_element(By.NAME, "username").send_keys("admin")
        self.browser.find_element(By.NAME, "password").send_keys("nimda666!")
        self.browser.find_element(By.XPATH, "/html/body/form/button").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/h2").text  
        self.assertIn(expected_result, actual_result)

    # def test_2_create_contact(self):
        self.browser.get(self.url + '/create.php')
        self.browser.find_element(By.ID, 'name').send_keys('bani')
        self.browser.find_element(By.ID, 'email').send_keys('bani@example.com')
        self.browser.find_element(By.ID, 'phone').send_keys('088811112222')
        self.browser.find_element(By.ID, 'title').send_keys('Orang Bengkel')

        self.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        expected_result = "Dashboard"
        actual_title = self.browser.title
        self.assertEqual(expected_result, actual_title)

    # def test_3_update_contact(self):
        self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys('bani')
        self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys(Keys.ENTER)

        searched_contact_exists = self.browser.find_elements(By.XPATH, f"//td[contains(text(), '{'bani'}')]")
        self.assertTrue(searched_contact_exists)
        
        actions = self.browser.find_element(By.XPATH, "//tr[@role='row'][1]//td[contains(@class, 'actions')]")
        actions.find_element(By.XPATH, ".//a[contains(@class, 'btn-success')]").click()

        self.browser.find_element(By.ID, 'title').clear()
        self.browser.find_element(By.ID, 'title').send_keys("Udah bukan orang bengkel")

        self.browser.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        expected_result = "Dashboard"
        actual_result = self.browser.title
        self.assertEqual(expected_result, actual_result)

        self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys('bani')
        self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys(Keys.ENTER)

        is_contact_updated = self.browser.find_elements(By.XPATH, f"//td[contains(text(), '{'Udah bukan orang bengkel'}')]")
        self.assertTrue(is_contact_updated)

    # def test_4_delete_contact(self):
        actions = self.browser.find_element(By.XPATH, "//tr[@role='row'][1]//td[contains(@class, 'actions')]")
        actions.find_element(By.XPATH, ".//a[contains(@class, 'btn-danger')]").click()

        self.browser.switch_to.alert.accept()
        time.sleep(3)

        self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys('bani')
        self.browser.find_element(By.ID, 'employee_filter').find_element(By.TAG_NAME, 'input').send_keys(Keys.ENTER)

        is_exists = self.browser.find_elements(By.XPATH, f"//td[contains(text(), '{'bani'}')]")
        self.assertFalse(is_exists)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')