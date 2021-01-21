# coding=utf-8
# @Time  : 2019/12/22
# @Author: 星空物语
# @File  : home_page.py
# @Description: 百度首页

from page_object.base_page import BasePage
import logging
import config.config as cf

log = logging.getLogger('szh.HomePage')


# 百度首页
class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
    def open_homepage(self):
        site = cf.get_value('site')  # 从全局变量取百度地址
        self.open(site)

    # 点击新闻
    def click_news(self):
        self.click(self.l_news)

    # 点击hao123
    def click_hao123(self):
        self.click(self.l_hao123)

    # 输入搜索关键字
    def input_keyword(self, keys=u'星空物语'):
        self.type(self.i_keyword, keys)

    # 点击搜索
    def click_search(self):
        self.click(self.b_search)
