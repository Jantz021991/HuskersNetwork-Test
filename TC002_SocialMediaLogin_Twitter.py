#Author : Deepika
#Final Test Demo


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class TC001_Login(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_twitter_login_feature(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("https://huskersapp.herokuapp.com/home/")
       time.sleep(1)


       driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/ul/li[2]/a/span/i").click()
       time.sleep(2)

       #Click login button
       driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/ul/li[2]/div/a").click()
       time.sleep(2)


       #Hit the Login via Twitter button -
       driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div[1]/div/button[2]").click()
       time.sleep(2)

       #Provide your Twitter Account credentials to login if you are not logged in on Twitter -
       #Twitter credentials

       username = "huskernetwork@gmail.com"
       pwd = "husker@123"

       elem = driver.find_element_by_id("username_or_email")
       elem.send_keys(username)
       elem = driver.find_element_by_id("password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       time.sleep(2)

       driver.find_element_by_id("allow").click()
       time.sleep(2)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()