from selenium import webdriver
from time import sleep
from hyrobot.common import *
from lib.webui import *
def suite_setup():

    print("打开网址")
    open_browser()
    wd=get_global_webdriver()
    mgr_login(wd)
def suite_teardown():
    wd=get_global_webdriver()
    wd.quit()