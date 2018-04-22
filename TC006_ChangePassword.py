#Author : Deepika
#Final Test Demo


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TC006_ChangePassword(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_changePassword_feature(self):
       user = "student"
       pwd = "ChangePassword@929"
       newpwd = "NewPassword@101"

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

       #Click on ChangePassword
       driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/ul/li[2]/div/a[1]/span").click()
       time.sleep(2)

       #Input Old Password
       elem = driver.find_element_by_id("id_old_password")
       elem.send_keys(pwd)
       elem = driver.find_element_by_id("id_new_password1")
       elem.send_keys(newpwd)
       elem = driver.find_element_by_id("id_new_password2")
       elem.send_keys(newpwd)


       driver.find_element_by_xpath("/html/body/div/div/form/div[4]/div/button").click()
       time.sleep(2)