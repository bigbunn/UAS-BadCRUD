import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        # option = webdriver.FirefoxOptions()
        # option.add_argument('--headless')
        # self.browser = webdriver.Firefox(options=option)
        
        self.browser = webdriver.Edge()
        # extension_path = "D:/adblocker.xpi"
        # self.browser.install_addon(extension_path)
        # self.addCleanup(self.browser.quit)

    def test_1_login_page_check(self):
        self.browser.get('http://localhost/BadCRUD/login.php')
        expected_result = "Login"        
        actual_result = self.browser.title
        self.assertIn(expected_result, actual_result)

    def test_2_login_check(self):           
        expected_result = "Halo, admin"
        self.browser.find_element(By.NAME, "username").send_keys("admin")
        self.browser.find_element(By.NAME, "password").send_keys("nimda666!")
        self.browser.find_element(By.XPATH, "/html/body/form/button").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/div[1]/h2").text  
        self.assertIn(expected_result, actual_result)

    def test_3_sign_out_check(self):
        expected_result = "Login"     
        self.browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div/div/a[3]').click()
        actual_result = self.browser.title
        self.assertIn(expected_result, actual_result)

    def test_4_invalid_login_check(self):           
        expected_result = "Wrong usename or password"
        self.browser.find_element(By.NAME, "username").send_keys("admin")
        self.browser.find_element(By.NAME, "password").send_keys("admin")
        self.browser.find_element(By.XPATH, "/html/body/form/button").click()
        actual_result = self.browser.find_element(By.XPATH, "/html/body/form/div/label").text  
        self.assertIn(expected_result, actual_result)

    def test_4_empty_login_check(self):           
        expected_result = "Login"  
        self.browser.find_element(By.XPATH, "/html/body/form/button").click()
        actual_result = self.browser.title
        self.assertIn(expected_result, actual_result)

    @classmethod
    def tearDownClass(self):
        self.browser.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2,warnings='ignore') 