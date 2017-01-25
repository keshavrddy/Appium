import os
import unittest
from appium import webdriver
from time import sleep

class ChessFreeTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = 'MotoG3'
        desired_caps['app'] = '/Users/Keshav/work/testing/android/Chess/ChessFree.apk'
        desired_caps['appPackage'] = 'com.adsolv.zwibe'
        desired_caps['appActivity'] = '.ChessFreeActivity'
        desired_caps['automationName'] = 'Appium'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        self.driver.quit()

    def test_single_player_mode(self):
        element = self.driver.find_element_by_id('ButtonPlay')
        element.click()
        # self.driver.find_element_by_class_name("android.widget.Textview")
        # self.assertEqual('MATCH SETTINGS', 'textfields[0].text')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChessFreeTest)
    unittest._TextTestResult(verbosity=2).run(suite)
