from hyrobot.common import *
from selenium import webdriver
from lib.webui import *
class c2:
    name = '管理员首页 - UI-0102'

    # 测试用例步骤
    def teststeps(self):
        
       

        STEP(2, '点击左侧客户菜单')

        # 先找到上层节点，缩小查找范围
        sidebarMenu = wd.find_element_by_class_name('sidebar-menu')

        # 再找到内部元素
        elements = sidebarMenu.find_elements_by_tag_name('span')

        # 第一个span对应的菜单是 客户，点击它
        elements[0].click()


        STEP(3, '添加客户')

        # 点击添加客户按钮
        wd.find_element_by_class_name('glyphicon-plus').click()

        # form-contorl 对应3个输入框
        inputs = wd.find_element_by_class_name('add-one-area') \
            .find_elements_by_class_name('form-control')

        # 输入客户姓名
        inputs[0].send_keys('南京中医院')
        # 输入联系电话
        inputs[1].send_keys('2551867858')
        # 输入客户描述
        inputs[2].send_keys('江苏省-南京市-秦淮区-汉中路-16栋504')

        # 第1个 btn-xs 就是创建按钮， 点击创建按钮
        wd.find_element_by_class_name('add-one-area') \
            .find_element_by_class_name('btn-xs') \
            .click()

        # 等待1秒
        sleep(1)


        STEP(4, '检查添加信息')

        # 找到 列表最上面的一栏
        item = wd.find_elements_by_class_name('search-result-item')[0]

        fields = item.find_elements_by_tag_name('span')[:6]

        texts = [field.text for field in fields]
        print(texts)

        # 预期内容为
        expected = [
            '客户名：',
            '南京中医院',
            '联系电话：',
            '2551867858',
            '地址：',
            '江苏省-南京市-秦淮区-汉中路-16栋504'
        ]

        CHECK_POINT('客户信息和添加内容一致 ',
                    texts == expected)



