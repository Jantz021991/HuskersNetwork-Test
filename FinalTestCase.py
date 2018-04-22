#Author : Deepika
#Final Test Demo

import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from TC001_Login import *
from TC002_SocialMediaLogin_Twitter import *
from TC003_UserSignUp import *
from TC004_Admin_CRUD_User import *
from TC005_Logout import *

class ConfigTestCase(unittest.TestCase):
    def setUp(self):
        print('set up')

    def runTest(self):
        print('run test')

if __name__ == "__main__":
   unittest.main()