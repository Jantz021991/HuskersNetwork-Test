#Author : Vivek Bhat Hosmat


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class TC008_Create_Venue(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_create_group(self):
       user = "huskyUser"
       pwd = "husker@123"

       driver = self.driver
       driver.maximize_window()
       driver.get("https://huskersapp.herokuapp.com")
       time.sleep(1)


       #Click Sign in button
       driver.find_element_by_xpath("/html/body/div/div/header/div/div/div[2]/ul/li[3]/a").click()
       time.sleep(1)

       # Fetch the user ID and password by giving the below codes
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       time.sleep(1)

       #Click on the create venue button
       driver.find_element_by_xpath("/html/body/div/div/div[2]/div[2]/a/button").click()
       time.sleep(1)

       elem = driver.find_element_by_id("id_name")
       elem.send_keys("Bob Campos Soccer Fields")
       elem = driver.find_element_by_id("id_address_line_1")
       elem.send_keys("5035 S 33rd St")
       elem = driver.find_element_by_id("id_address_line_2")
       elem.send_keys(" ")
       elem = driver.find_element_by_id("id_city")
       elem.send_keys("Omaha")
       elem = driver.find_element_by_id("id_state")
       elem.send_keys("Nebraska")
       elem = driver.find_element_by_id("id_country")
       elem.send_keys("68107")

       driver.find_element_by_xpath("/html/body/div/div/form/div[7]/div/button").click()

   def tearDown(self):
       self.driver.close()

   if __name__ == "__main__":
       unittest.main()