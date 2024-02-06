import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By

class XSSDetectionTestCase(unittest.TestCase):

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
            
    def test_xss(self):
        expected_result = "Halo, admin"
        self.browser.get(self.url + '/login.php')
        self.browser.find_element(By.NAME, "username").send_keys("admin")
        self.browser.find_element(By.NAME, "password").send_keys("nimda666!")
        self.browser.find_element(By.XPATH, "/html/body/form/button").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/h2").text  
        self.assertIn(expected_result, actual_result)

    # def test_2_xss_page(self):
        self.browser.get(self.url + '/xss.php')

        input_field = self.browser.find_element(By.NAME, 'thing')
        input_value = '<script>alert("XSS Attack!");</script>'
        input_field.send_keys(input_value)

        self.browser.find_element(By.NAME, 'submit').click()

        alert = self.browser.switch_to.alert
        self.assertEqual('XSS Attack!', alert.text)
        alert.accept()

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')