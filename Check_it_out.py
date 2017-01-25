from time import sleep

class Check_it_out():

    def Checkitout(self):
        sleep(5)
        # i = 0
        # while i < 3:
        #     self.driver.swipe(200, 1000, 200, 300)
        #     sleep(1)
        #     i += 1
        # sleep(3)
        self.driver.find_elements_by_class_name("android.support.v7.widget.RecyclerView")[0].find_elements_by_class_name("android.widget.FrameLayout")[0].click()
        sleep(3)
        self.driver.find_elements_by_class_name('android.widget.LinearLayout')[1].find_element_by_id('com.adsolv.zwibe:id/post_overflow').click()
        sleep(2)
        self.driver.find_elements_by_class_name('android.widget.LinearLayout')[0].click()
        sleep(2)
        self.driver.find_element_by_id('com.adsolv.zwibe:id/autoCompleteName').send_keys("Mi")
        sleep(30)
        self.driver.find_element_by_id('com.adsolv.zwibe:id/ic_done').click()
        sleep(10)