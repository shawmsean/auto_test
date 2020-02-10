from selenium import webdriver
from time import sleep
def suite_setup():

    print("打开网址")

    wd = webdriver.Firefox()
    wd.implicitly_wait(5)

def suite_teardown():
    wd.quit()