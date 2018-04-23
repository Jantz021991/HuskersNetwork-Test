#Author : Erdenebileg


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class TC009_Hashtag_Feed(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_create_group(self):
       user = "groyce"
       pwd = "instructor1a"

       driver = self.driver
       driver.maximize_window()
       driver.get("https://huskersapp.herokuapp.com/groups")
       time.sleep(1)

       # Fetch the user ID and password by giving the below codes
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       time.sleep(1)

       driver.find_element_by_xpath("/html[1]/body[1]/header[1]/div[2]/div[1]/div[1]/ul[1]/li[2]/a[1]").click()
       time.sleep(1)

       driver.find_element_by_xpath("//a[@class='text-dark'][contains(text(),'Midland Soccer group 4 PM')]").click()
       time.sleep(1)

       driver.find_element_by_xpath("//h1[contains(text(),'Midland Soccer group 4 PM Details')]")
       time.sleep(1)




   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()