from Login import Login
import unittest
from appium import webdriver
from CommentTest import CommentTest
from Check_it_out import Check_it_out

class ZwibeFreeTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0'
        desired_caps['deviceName'] = 'Keshav Reddy(Galaxy Note3)'
        # desired_caps['app'] = '/Users/Keshav/work/testing/android/Zwibe/Zwibe.apk'
        desired_caps['appPackage'] = 'com.adsolv.zwibe'
        desired_caps['appActivity'] = '.activities.SplashActivity'
        desired_caps['automationName'] = 'Appium'
        desired_caps['noReset'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testzwibe(self):
        activity = self.driver.current_activity
        testing_options = {"CommentTesting": CommentTest.putcomment,"DeleteComment":CommentTest.deletecomment,
                           "Login":Login.test_phone_book_login,"Check_it_out":Check_it_out.Checkitout
                           }
        if activity == ".activities.LoginActivity":
            testtype = "Login"

        else:
            testtype = "Check_it_out"


        testing_options[testtype](self)

    def tearDown(self):
            self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ZwibeFreeTest)
    unittest._TextTestResult(verbosity=6).run(suite)
