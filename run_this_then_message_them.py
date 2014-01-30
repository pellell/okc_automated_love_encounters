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

        print "This is going to take at least 3 minutes maybe more ... please hold ... gathering perfect love for perfect people."
        u = open("username_pword_SEX_m_or_f","r").readlines()
        SEX = u[2].replace("\n","").replace("\r","")
        GENITALS = u[3].replace("\n","").replace("\r","")
        driver.find_element_by_id("username").send_keys(u[0].replace("\n","").replace("\r",""))
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(u[1].replace("\n","").replace("\r",""))
        driver.find_element_by_id("login_btn").click()

        driver.get(self.base_url + "/")


        XXX = open('output','a+')

        for derp in xrange(1,50):

            # match anywhere
            driver.get("http://m.okcupid.com/match?mygender="+SEX+"&using_saved_search=&matchOrderBy=MATCH&update_prefs=1&sa=1&fromWhoOnline=0&sort_type=0&filter1=2,25,27&filter2=0,"+str(GENITALS)+"&filter3=1,1&filter4=5,2678400&filter5=7,1&locid=0&")
            usernames = driver.find_elements_by_xpath("//a[@class=\"username\"]")
            for user in usernames:
                XXX.write(user.text+"\n")

            # match in 500 miles
            driver.get("http://m.okcupid.com/match?mygender="+SEX+"&using_saved_search=&matchOrderBy=MATCH&update_prefs=1&sa=1&fromWhoOnline=0&sort_type=0&filter1=2,25,27&filter2=3,500&filter3=0,"+GENITALS+"&filter4=1,1&filter5=5,2678400&filter6=7,1&locid=0&")
            usernames = driver.find_elements_by_xpath("//a[@class=\"username\"]")
            for user in usernames:
                XXX.write(user.text+"\n")

            #match in 100 miles
            driver.get("http://m.okcupid.com/match?mygender="+SEX+"&using_saved_search=&matchOrderBy=MATCH&update_prefs=1&sa=1&fromWhoOnline=0&sort_type=0&filter1=2,25,27&filter2=3,100&filter3=0,"+str(GENITALS)+"&filter4=1,1&filter5=5,2678400&filter6=7,1&locid=0&")
            usernames = driver.find_elements_by_xpath("//a[@class=\"username\"]")
            for user in usernames:
                XXX.write(user.text+"\n")

            # match in 25 miles
            driver.get("http://m.okcupid.com/match?mygender="+SEX+"&using_saved_search=&matchOrderBy=MATCH&update_prefs=1&sa=1&fromWhoOnline=0&sort_type=0&filter1=2,25,27&filter2=3,25&filter3=0,"+str(GENITALS)+"&filter4=1,1&filter5=5,2678400&filter6=7,1&locid=0&")
            usernames = driver.find_elements_by_xpath("//a[@class=\"username\"]")
            for user in usernames:
                XXX.write(user.text+"\n")
            time.sleep(4)



        XXX.close()
        uniqlines = set(open('output').readlines())

        this = open('uniqs', 'w').writelines(set(uniqlines))

        print "#\n#\n###########\n so there is a bunch of unique matches now python message_them\n##########\n#\n#\n\n"

    
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
