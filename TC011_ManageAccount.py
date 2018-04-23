#Author : Deepika
#Final Test Demo


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TC011_ManageAccount(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_manage_account_feature(self):
       user = "huskyUser"
       pwd = "husker@123"

       driver = self.driver
       driver.maximize_window()
       driver.get("https://huskersapp.herokuapp.com")
       time.sleep(1)

        #Click on the Sign In button at the top right corner
       driver.find_element_by_xpath("/html/body/div/div/header/div/div/div[2]/ul/li[3]/a").click()
       time.sleep(1)


       # Fetch the user ID and password by giving the below codes
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       time.sleep(1)

       # Click on the User's profile
       driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/ul/li[2]/a/span/i").click()
       time.sleep(1)

       #Click on Manage Account
       driver.find_element_by_xpath("/html/body/header/div[1]/div/div[2]/ul/li[2]/div/a[2]/span").click()
       time.sleep(1)

        #Update the necessary information
       elem = driver.find_element_by_id("id_first_name")
       elem.send_keys("Sam")
       elem = driver.find_element_by_id("id_last_name")
       elem.send_keys("Angel")
       elem = driver.find_element_by_id("id_date_of_birth")
       elem.send_keys("10/02/1991")
       # element = driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/div/form/div[4]/div/input").click()
       elem = driver.find_element_by_id("id_favorite_team")
       for option in elem.find_elements_by_tag_name('option'):
           if option.text == 'Manchester':
               option.click()
               break

       elem = driver.find_element_by_id("id_current_location")
       elem.send_keys("Omaha")
       elem = driver.find_element_by_id("id_introduction")
       elem.send_keys(" I am a huge Soccer Fan!!I play soccer four times a week and I am new to this place, hoping to find a soccer team via Huskers Network! Cheers!")
       time.sleep(2)

       driver.find_element_by_xpath("/html/body/div/div/div[2]/div/div/div/div/div/form/div[8]/div/button").click()
       time.sleep(1)

   def tearDown(self):
       self.driver.close()


if __name__ == "__main__":
   unittest.main()