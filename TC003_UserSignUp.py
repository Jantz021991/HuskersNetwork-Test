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
       driver.get("https://huskersapp.herokuapp.com/home/")
       time.sleep(1)


       driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/ul/li[2]/a/span/i").click()
       time.sleep(1)

       #Click login button
       driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/ul/li[2]/div/a").click()
       time.sleep(1)

       #Redirects you to the login page, at the bottom go to the Sign UP button

       driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/div[2]/div/p/a/b").click()
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
       time.sleep(2)

        #Click on Sign Up button to register the user to Huskers Network
       driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div/div/form/div[6]/div/button").click()

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()