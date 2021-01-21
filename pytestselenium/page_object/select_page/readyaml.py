import  yaml
import os
class FindElement():
    def __init__(self,driver):
        self.driver=driver
    def get_element(self,key):
        path=r"F:\All\pytestselenium\page_object\page\Login_163\login163.yaml"
        with open(path,'r',encoding="utf-8") as f:
            cfg=yaml.load(f)
        self.iframe="//iframe[contains(@id,'x-URS-iframe')]"
        self.type=cfg["username"]["type"]
        self.username=cfg["username"]["value"]


