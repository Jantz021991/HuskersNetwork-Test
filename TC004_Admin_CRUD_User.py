#Author : Deepika
#Final Test Demo


import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TC004_Admin_CRUD_User(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_login_feature(self):
       user = "instructor"
       pwd = "instructor1a"

       driver = self.driver
       driver.maximize_window()
       driver.get("https://huskersapp.herokuapp.com/admin/")
       time.sleep(1)


       # Fetch the user ID and password by giving the below codes
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       time.sleep(1)

        #Hit the login button to login to Admin Screen
       driver.find_element_by_xpath("/html/body/div/div[2]/div/form/div[3]/input").click()
       time.sleep(1)

       driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[1]/table/tbody/tr[2]/th/a").click()
       time.sleep  (1)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()