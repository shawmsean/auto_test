from hyrobot.common import *
from selenium import webdriver
from lib.webui import *
from selenium.webdriver.common.keys import Keys


class c2:
    name = '管理员首页 - UI-0102'

    # 测试用例步骤
    def teststeps(self):

        STEP(2, '点击左侧客户菜单')
        wd = get_global_webdriver()
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
        sleep(1)
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
            '客户名：', '南京中医院', '联系电话：', '2551867858', '地址：',
            '江苏省-南京市-秦淮区-汉中路-16栋504'
        ]

        CHECK_POINT('客户信息和添加内容一致 ', texts == expected)


class c3:
    name = '管理员首页 - UI-0103'

    # 测试用例步骤
    def teststeps(self):

        STEP(2, '点击左侧客户菜单')
        wd = get_global_webdriver()
        # 先找到上层节点，缩小查找范围
        sidebarMenu = wd.find_element_by_class_name('sidebar-menu')

        # 再找到内部元素
        elements = sidebarMenu.find_elements_by_tag_name('span')

        # 第一个span对应的菜单是 客户，点击它
        elements[0].click()

        STEP(3, '修改客户信息')

        # 点击编辑按钮
        wd.find_element_by_xpath(
            '/html/body/div[1]/div/section[2]/div[3]/div[4]/div/label[1]'
        ).click()

        # form-contorl 对应3个输入框
        inputs = wd.find_element_by_class_name('search-result-item') \
            .find_elements_by_class_name('form-control')
        sleep(1)
        # 修改客户姓名
        inputs[0].send_keys(Keys.CONTROL, "a")
        inputs[0].send_keys('南京省中医院')

        # 第1个 btn-xs 就是创建按钮， 点击创建按钮
        wd.find_element_by_xpath('/html/body/div[1]/div/section[2]/div[3]/div[2]/div/label[1]') \
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
            '客户名：', '南京省中医院', '联系电话：', '2551867858', '地址：',
            '江苏省-南京市-秦淮区-汉中路-16栋504'
        ]

        CHECK_POINT('客户信息和添加内容一致 ', texts == expected)


class c4:
    name = '管理员首页 - UI-0106'

    # 测试用例步骤
    def teststeps(self):

        STEP(2, '点击页脚处 链接 白月黑羽 点击访问官网')
        wd = get_global_webdriver()
        #获取当前窗口的handle
        main_window = wd.current_window_handle
        #获取当前窗口的url
        main_url = wd.current_url
        # 先找到上层节点，缩小查找范围
        wd.find_element_by_xpath('/html/body/div[1]/footer/strong/a').click()
        sleep(5)

        # 切换到新窗口
        for handle in wd.window_handles:
            wd.switch_to.window(handle)
            if "白月黑羽 Python3" in wd.title:
                break

        # 最大化窗口
        wd.maximize_window()
        sleep(3)
        wd.get_screenshot_as_file(r"G:\自动测试\screenshots\a1.png")
        STEP(3, '修改客户信息获取 页眉导航菜单中所有教程类目')
        navinames = wd.find_elements_by_class_name(
            'masthead__menu-item'
        )
        texts = [navi.text for navi in navinames]
        print(texts)
            
        STEP(4, '检查添加信息')
        # 预期内容为
        expected = [
            'Python基础',
            'Python进阶',
            'Web开发',
            '自动化和性能测试',
            'Linux和MySQL',
            '练习作业',
            '常见问题',
            '好文分享'
        ]
        print(expected)
        CHECK_POINT('导航菜单中所有教程类目正确 ', texts == expected)

        STEP(5,"返回主页面")
        wd.switch_to.window(main_window)
        wd.get_screenshot_as_file(r"G:\自动测试\screenshots\a2.png")
        wd.find_element_by_class_name("hidden-xs").click()
        wd.find_element_by_xpath("/html/body/div[1]/header/nav/div/ul/li[2]/ul/li[3]/div[2]/a").click()
        sleep(3)
        cur_url = wd.current_url
        print(main_url)
        print(cur_url)
        CHECK_POINT("检查是否返回主页",main_url==cur_url)
