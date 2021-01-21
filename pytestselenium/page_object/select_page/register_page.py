# coding=utf-8
from selenium import webdriver
import pytestselenium.config.config as cf
from pytestselenium.page_object.base_page import BasePage
import os
import yaml
import json
class register_page(BasePage):
    def __init__(self,driver):
        path=r"F:\All\pytestselenium\page_object\page\Login_163\login163.yaml"
        with open(path,'r',encoding="utf-8") as f:
            cfg=yaml.load(f)
        self.iframe="//iframe[contains(@id,'x-URS-iframe')]"
        self.type=cfg["username"]["type"]
        self.username=cfg["username"]["value"]
        print("register")
        self.driver=driver
    def Loginemail(self):
        site=cf.get_value("site")
        self.open('https://mail.163.com/')
    def EnterIframe(self):
        self.frame_in(self.iframe)
    def input_email(self):
        self.type(",".join(self.type,self.username),keys="123")

if __name__ == '__main__':
    reg=register_page()
    # driver = webdriver.Chrome()
    # driver.get("https://mail.163.com/")
    # driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@id,'x-URS-iframe')]"))
    # test = driver.find_element_by_xpath("//div[@class='u-input box']/input[@name='email']")
    # print(test.send_keys("123"))