#Author : Deepika
#Final Test Demo


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TC001_Logout(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_logout_feature(self):
       user = "instructor"
       pwd = "instructor1a"

       driver = self.driver
       driver.maximize_window()
       driver.get("https://huskersapp.herokuapp.com/home/")
       time.sleep(1)


       driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/ul/li[2]/a/span/i").click()
       time.sleep(1)

       #Click login button
       driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/ul/li[2]/div/a").click()
       time.sleep(1)

       # Fetch the user ID and password by giving the below codes
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       time.sleep(1)

       #Allow the user to logout
       driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/ul/li[2]/a/span/i").click()
       time.sleep(1)

       #Click on Logout
       driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/ul/li[2]/div/a[3]/span").click()
       time.sleep(2)

       #Check the Logon Icon
       driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/ul/li[2]/a/span/i").click()
       time.sleep(1)

       # Click login button
       driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/ul/li[2]/div/a").click()
       time.sleep(1)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()