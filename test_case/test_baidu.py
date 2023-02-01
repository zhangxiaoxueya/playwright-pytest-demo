import sys
from time import sleep
from playwright.async_api import Dialog
from seldom.testdata.conversion import json_to_list
from page.baidu import BaiduElem
import allure
import pytest
from common.config import  *

@allure.feature('百度测试')
class TestBaidu():

    @allure.story("test001-搜索")
    def test_baidu_001(self, page, base_url):
        """
        名称：百度搜索"playwright"
        步骤：
        1、打开浏览器
        2、输入"playwright"关键字
        3、点击搜索按钮
        检查点：
        * 检查页面标题是否相等。
        """
        page.goto(base_url)
        page.type(BaiduElem.search_input, text="playwright")
        page.click(BaiduElem.search_button)
        sleep(2)
        assert page.title() == "playwright_百度搜索"

    @allure.story("test002-保存设置")
    def test_baidu_002(self, page, base_url):
        """
        名称：百度搜索设置
        步骤：
        1、打开百度浏览器
        2、点击设置链接
        3、在下拉框中"选择搜索"
        4、点击"保存设置"
        5、对弹出警告框保存
        检查点：
        * 检查是否弹出提示框
        """
        page.goto(base_url)
        page.click(BaiduElem.settings)
        page.click(BaiduElem.search_setting)
        sleep(2)
        page.click(BaiduElem.save_setting)

        def on_dialog(dialog: Dialog):
            assert dialog.type == "alert"
            assert dialog.message == "已经记录下您的使用偏好"
            dialog.accept()

        page.on("dialog", on_dialog)


    @allure.story("test003-搜索中国")
    def test_baidu_003(self, page):
        page.goto("https://www.baidu.com/")
        # Click input[name="wd"]
        page.click("input[name=\"wd\"]")
        # Fill input[name="wd"]
        page.fill("input[name=\"wd\"]", "zhongguo ")
        # Press Enter
        # with page.expect_navigation(url="https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=zhongguo%20&fenlei=256&rsv_pq=d3b5747500073d0a&rsv_t=0df4UB%2Fe5SQx6iVzGFj5id3G0Ani1ItME5dWapeuAhqLKksg0aXPVl0A86k&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=10&rsv_sug1=7&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&prefixsug=zhongguo%2520&rsp=5&inputT=1667&rsv_sug4=2346&rsv_jmp=fail"):
        with page.expect_navigation():
            page.press("input[name=\"wd\"]", "Enter")

    @pytest.mark.parametrize(
        "name, search_key",
        [("1", "Selenium"),
         ("2", "pytest文档"),
         ("3", "pytest-html"),
         ],
        ids=["case1", "case2", "case3"]
    )
    @allure.story("test004-参数化")
    def test_baidu_004(self, name, search_key, page, base_url):
        page.goto(base_url)
        page.type(BaiduElem.search_input, search_key)
        page.click(BaiduElem.search_button)
        sleep(2)
        assert page.title() == search_key + "_百度搜索"



    @pytest.mark.parametrize(
        "name, search_key",
        json_to_list(data_path + "/data_file.json")
    )
    @allure.story("test005-文件读取参数化")
    def test_baidu_006(self, name, search_key, page, base_url):
        page.goto(base_url)
        page.type(BaiduElem.search_input, search_key)
        page.click(BaiduElem.search_button)
        sleep(2)
        assert page.title() == search_key + "_百度搜索"
