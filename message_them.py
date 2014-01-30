from selenium.webdriver.common.alert import Alert
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class MessageThem(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://m.okcupid.com"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_message_them(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("username").clear()


        u = open("username_pword","r").readlines()
        driver.find_element_by_id("username").send_keys(u[0].replace("\n","").replace("\r",""))
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(u[1].replace("\n","").replace("\r",""))
        driver.find_element_by_id("login_btn").click()

#open msg file

        msg = open("edit_this_message","r").readlines()
        msg = msg[0]

# go gettum tiger

        for HOT_HOT_HOT in open('uniqs').readlines():
            try:
                try:
                    driver.get("http://m.okcupid.com/profile/"+str(HOT_HOT_HOT).replace("\n","")+"?cf=regular")
                    alert = self.driver.switch_to_alert()
                    alert.accept()
                except Exception,bz:
                    print bz

                driver.get("http://m.okcupid.com/profile/"+str(HOT_HOT_HOT).replace("\n","")+"?cf=regular")
                match_percent = driver.find_element_by_css_selector("li.match").text

                time.sleep(5)
                driver.get("http://www.okcupid.com/messages?r1="+str(HOT_HOT_HOT).replace("\n","")+"&compose=1&fromprofile=1")
                driver.find_element_by_id("message_text").clear()

                driver.find_element_by_id("message_text").send_keys(match_percent+msg)
                time.sleep(2)
                driver.find_element_by_link_text("Send").click()
                driver.find_element_by_id("sendmsg").click()
                time.sleep(1)
                try:
                    alert = self.driver.switch_to_alert()
                    alert.accept()
                except Exception,bz:
                    print bz
            except Exception,e:
                print e

    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
