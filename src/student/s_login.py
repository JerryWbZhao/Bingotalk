#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, os
import HTMLTestRunner
class Student1(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://s.qa.bingotalk.cn/#/login"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #学生登录用例
    def test_student_login(self):
        u"""学生登录用例"""
        driver = self.driver
        driver.get(self.base_url + "/")
        try:
        #是一个无法找到的元素id
            driver.find_element_by_name("username").send_keys("13550190818")
        except:
            driver.get_screenshot_as_file("D:\\selenium_use_case\\error_png\\s_username.png")
        #如果没有找到上面的元素就截取当前页面。
        driver.find_element_by_name("password").send_keys("Pass1234")
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/form/button").click()
        time.sleep(2)
        driver.close() 
               
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Student1("test_student_login"))   
    results = unittest.TextTestRunner().run(suite)