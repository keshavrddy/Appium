import unittest
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction

class CommentTest():

    def putcomment(self):
        i =0
        while i < 5:
            self.driver.swipe(200, 1000, 200, 300)
            sleep(1)
            i += 1
        sleep(3)
        self.driver.find_elements_by_class_name("android.support.v7.widget.RecyclerView")[
            0].find_elements_by_class_name("android.widget.FrameLayout")[1].click()
        sleep(3)
        self.driver.find_element_by_id('com.adsolv.zwibe:id/post_comment_view').click()
        sleep(2)
        self.driver.find_element_by_id('com.adsolv.zwibe:id/edit_text_out').send_keys("Hi Hello")
        sleep(1)
        self.driver.find_element_by_id('com.adsolv.zwibe:id/button_comment').click()
        sleep(10)
        return
    def deletecomment(self):
        sleep(2)
        self.driver.find_element_by_id('com.adsolv.zwibe:id/action_profile').click()
        sleep(2)
        self.driver.find_elements_by_class_name('android.support.v7.widget.RecyclerView')[0].find_elements_by_class_name("android.support.v7.widget.ao")[3].click()
        sleep(2)
        self.driver.find_element_by_id('com.adsolv.zwibe:id/log_recycler_view').find_elements_by_class_name('android.widget.FrameLayout')[0].click()
        sleep(2)
        self.driver.find_element_by_id('com.adsolv.zwibe:id/post_comment_view').click()
        sleep(2)
        element = self.driver.find_elements_by_class_name('android.support.v7.widget.RecyclerView')[0].find_elements_by_class_name('android.widget.LinearLayout')[0]
        action = TouchAction(self.driver)
        action.long_press(element).release().perform();
        sleep(2)
        self.driver.find_elements_by_class_name('android.widget.LinearLayout')[0].click()
        sleep(2)
        self.driver.find_element_by_id('com.adsolv.zwibe:id/simple_alert_yes').click()
        sleep(10)
        return self






