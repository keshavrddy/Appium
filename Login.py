from time import sleep



class Login():
    def test_phone_book_login(self):
        sleep(5)
        self.driver.find_element_by_id('facebook_sign_in_button').click()
        sleep(3)
        if self.driver.find_element_by_id('com.facebook.katana:id/login_username') == '':
            sleep(2)
            self.driver.find_element_by_id('com.facebook.katana:id/login_username').send_keys(
                'keshav.reddy2012@gmail.com')
        else:
            self.driver.find_element_by_id('com.facebook.katana:id/login_password').send_keys('pass9362088020')
        sleep(2)
        self.driver.find_element_by_id('com.facebook.katana:id/login_login').click()
        sleep(20)
        return