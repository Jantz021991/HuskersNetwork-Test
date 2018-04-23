#Author : Erdenebileg


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class TC007_Create_Group(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_create_group(self):
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

       # Click Create Button
       driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/a[1]").click()
       time.sleep(1)

       elem = driver.find_element_by_id("id_name")
       elem.send_keys("Unit Test Group")
       elem = driver.find_element_by_id("id_venue")
       for option in elem.find_elements_by_tag_name('option'):
           if option.text == 'Caniglia Field':
               option.click()
               break

       elem = driver.find_element_by_id("id_meeting_time")
       elem.send_keys("3 PM")
       elem = driver.find_element_by_id("id_group_details")
       elem.send_keys("Test Detail")
       elem = driver.find_element_by_id("id_groupAdmin")
       for option in elem.find_elements_by_tag_name('option'):
           if option.text == 'admin':
               option.click()
               break
       elem = driver.find_element_by_id("id_hashtag")
       elem.send_keys("#testcase")
       time.sleep(2)

       driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/form[1]/div[8]/div[1]/button[1]").click()
       time.sleep(3)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()