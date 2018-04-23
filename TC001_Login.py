#Author : Deepika
#Final Test Demo


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TC001_Login(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_login_feature(self):
       user = "huskyUser"
       pwd = "husker@123"

       driver = self.driver
       driver.maximize_window()
       driver.get("https://huskersapp.herokuapp.com")
       time.sleep(1)

       # Click on the Sign in button
       driver.find_element_by_xpath("/html/body/div/div/div[1]/div/a[1]/button").click()
       time.sleep(1)

       # Fetch the user ID and password by giving the below codes
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       time.sleep(1)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()