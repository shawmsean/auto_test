from selenium import webdriver
from time import sleep


def open_browser():

    print("打开网址")

    wd = webdriver.Firefox()
    wd.implicitly_wait(5)
    wd.get('http://127.0.0.1/mgr/sign.html')
    return wd


def mgr_login(wd):
    # 根据 ID 选择元素，并且输入字符串
    wd.find_element_by_id('username').send_keys('byhy')
    wd.find_element_by_id('password').send_keys('88888888')

    # 根据标签名查找元素
    wd.find_element_by_tag_name('button').click()
