import unittest, os
from selenium import webdriver
from selenium.webdriver.common.by import By

class ProfilePictureUploadTestCase(unittest.TestCase):

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

    def test_1_login(self):
        expected_result = "Halo, admin"
        self.browser.get(self.url + '/login.php')
        self.browser.find_element(By.NAME, "username").send_keys("admin")
        self.browser.find_element(By.NAME, "password").send_keys("nimda666!")
        self.browser.find_element(By.XPATH, "/html/body/form/button").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/h2").text  
        self.assertIn(expected_result, actual_result)

    def test_2_profile_page(self):
        expected_result = "Profile"
        self.browser.get(self.url + '/profil.php')
        actual_result = self.browser.title
        self.assertIn(expected_result,actual_result)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, warnings='ignore')