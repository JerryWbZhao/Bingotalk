#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest, time, re, os
import HTMLTestRunner
class Student2(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://s.qa.bingotalk.cn/#/login"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #学生登录用例
    def test_student_order(self):
        u"""学生约课用例"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        try:
        #是一个无法找到的元素id
            driver.find_element_by_name("username").send_keys("13920180515")
        except:
            driver.get_screenshot_as_file("D:\\selenium_use_case\\error_png\\s_username.png")
        #如果没有找到上面的元素就截取当前页面。
        driver.find_element_by_name("password").send_keys("Pass1234")
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/form/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div/div[1]/ul/li[2]").click()
        time.sleep(2)
        #跳过引导
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div/div[2]/div/div/div/div/div[4]/div/div[3]/span/button[1]/span").click()
        #鼠标定位在悬浮窗
        move_on_to_add_condition = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div/div[2]/div/div/div/div/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/div/div[1]/div[2]")
        ActionChains(driver).move_to_element(move_on_to_add_condition).perform()
        time.sleep(2)
        #点击去约课
        driver.find_element_by_class_name("add-mask").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div[1]/div/div/p[2]/button").click()
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div/div[2]/div/div/div/div/div[1]/div[2]/div[2]/div/div[2]/div/div[3]/span/button[2]").click()
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div/div[2]/div/div/div/div/div[4]/div/div[2]/div[5]").click()
        #鼠标再次定位在悬浮窗
        move_on_to_add_condition = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div/div[2]/div/div/div/div/div[2]/div[3]/table/tbody/tr[1]/td[7]/div/div/div[1]/p")
        ActionChains(driver).move_to_element(move_on_to_add_condition).perform()
        time.sleep(2)
        #点击取消约课
        driver.find_element_by_class_name("remove-mask").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div/div[2]/div/div/div/div/div[6]/div/div[3]/span/button[2]").click()        
        time.sleep(2)
        driver.close() 
               
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Student2("test_student_order"))    
    results = unittest.TextTestRunner().run(suite)