from hyrobot.common import *
from selenium import webdriver
from lib.webui import *


class c2:
    name = '药品管理 - UI-0103'

    # 测试用例步骤
    def teststeps(self):
        STEP(1,"点击左侧药品按钮")
        INFO("点击左侧药品按钮")
        wd=get_global_webdriver()
        element=wd.find_element_by_xpath("/html/body/div[1]/aside/section/ul/li[3]/a/span")
        element.click()
        sleep(3)
        wd.get_screenshot_as_file(r"g:\1.png")
        print("it doesnt work")
        STEP(2,"点击右侧的增加药品按钮")
        INFO("添加药品")
        wd.find_element_by_xpath("/html/body/div[1]/div/section[2]/div[1]/button").click()
        wd.find_element_by_xpath("/html/body/div[1]/div/section[2]/div[1]/div[1]/div[1]/input").send_keys("测试2")
        wd.find_element_by_xpath("/html/body/div[1]/div/section[2]/div[1]/div[1]/div[2]/input").send_keys("test2")
        wd.find_element_by_xpath("/html/body/div[1]/div/section[2]/div[1]/div[1]/div[3]/textarea").send_keys("用于测试")
        wd.find_element_by_xpath("/html/body/div[1]/div/section[2]/div[1]/div[2]/button[1]").click()
        STEP(3,"检验添加的数据是否正确")
        INFO("检验数据")
        expect=["测试2","test2","用于测试"]
        item=wd.find_elements_by_class_name("search-result-item")[0]
        fields=item.find_elements_by_tag_name("span")[:]
        com=[field.text for field in fields]
        text=[]
        for a in range(6):
            if a%2!=0:
                text.append(com[a])

        #text=[fields[1].text,fields[3].text,fields[5].text]
        print(text)
        CHECK_POINT("录入与显示一致",expect==text)


