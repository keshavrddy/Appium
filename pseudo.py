#
# import unittest
# from appium import webdriver
# from  CommentTest import CommentTest
#
# class ZwibeFreeTest(unittest.TestCase):
#
#     def setUp(self):
#         desired_caps = {}
#         desired_caps['platformName'] = 'Android'
#         desired_caps['platformVersion'] = '5.0'
#         desired_caps['deviceName'] = 'Keshav Reddy(Galaxy Note3)'
#         # desired_caps['app'] = '/Users/Keshav/work/testing/android/Zwibe/Zwibe.apk'
#         desired_caps['appPackage'] = 'com.adsolv.zwibe'
#         desired_caps['appActivity'] = '.activities.SplashActivity'
#         desired_caps['automationName'] = 'Appium'
#         desired_caps['noReset'] = 'True'
#         self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
#     def start_testing(self):
#         # This will come from parameters in future or from excel
#         testtype = "CommentTesting"
#         options = {"CommentTesting": CommentTest.putcomment,
#                    "DeleteCommentTesting": CommentTest.deletecomment
#
#                    }
#         options[testtype]()
#
#     def tearDown(self):
#             self.driver.quit()
#
# if __name__ == '__main__':
#     suite = unittest.TestLoader().loadTestsFromTestCase(ZwibeFreeTest)
#     unittest._TextTestResult(verbosity=6).run(suite)
