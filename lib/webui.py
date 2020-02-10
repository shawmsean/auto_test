from selenium import webdriver
from time import sleep
from hyrobot.common import *
def mgr_login(wd):
    # 根据 ID 选择元素，并且输入字符串
    wd.find_element_by_id('username').send_keys('byhy')
    wd.find_element_by_id('password').send_keys('88888888')

    # 根据标签名查找元素
    wd.find_element_by_tag_name('button').click()

def open_browser():
    wd=webdriver.Firefox()
    GSTORE["global_webdriver"]=wd
    wd.get('http://127.0.0.1/mgr/sign.html')
    wd.implicitly_wait(5)

def get_global_webdriver():
    return GSTORE["global_webdriver"]

