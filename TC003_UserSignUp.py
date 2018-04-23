#Author : Deepika
#Final Test Demo


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TC003_UserSignUp(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_login_feature(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("https://huskersapp.herokuapp.com")
       time.sleep(1)

        #Click on the Sign up button
       driver.find_element_by_xpath("/html/body/div/div/div[1]/div/a[2]/button").click()
       time.sleep(1)



       #Now enter the credentials to Sign up

       elem = driver.find_element_by_id("id_username")
       elem.send_keys("SamRocks")
       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys("Samantha")
       elem.send_keys(Keys.RETURN)
       elem = driver.find_element_by_id("id_email")
       elem.send_keys("smantha@unomaha.edu")
       elem = driver.find_element_by_id("id_password1")
       elem.send_keys("husker@123")
       elem = driver.find_element_by_id("id_password2")
       elem.send_keys("husker@123")
       time.sleep(1)

        #Click on Sign Up button to register the user to Huskers Network
       driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/form/div[6]/div/button").click()

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()