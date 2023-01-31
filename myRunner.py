#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Time    : 2021/10/19 4:59 下午 
@File    : myRunner.py
@Author  : zhangxue
@Desc    : 运行文件入口
'''
import time
import logging
import pytest
from common.util import invoke
from common.config import *
from config import RunConfig
from common.log import logger



def init_env(new_report):
    """
    初始化测试报告目录
    """
    os.mkdir(new_report)
    os.mkdir(new_report + "/image")

def myrunner():
    # 1、运行脚本，生成allure数据
    try:
        logger.info("开始测试✨✨✨！")
        now_time = time.strftime("%Y_%m_%d_%H_%M_%S")
        RunConfig.NEW_REPORT = os.path.join(report_path, now_time)
        init_env(RunConfig.NEW_REPORT)
        html_report = os.path.join(RunConfig.NEW_REPORT, "report.html")
        xml_report = os.path.join(RunConfig.NEW_REPORT, "junit-xml.xml")
        if RunConfig.mode == "headless":
            pytest.main(["-s", "-v", RunConfig.cases_path,
                         "--browser=" + RunConfig.browser,
                         "--alluredir=" + RunConfig.NEW_REPORT,
                         "--junit-xml=" + xml_report,
                         "--self-contained-html",
                         "--maxfail", RunConfig.max_fail,
                         "--reruns", RunConfig.rerun])
        if RunConfig.mode == "headful":
            pytest.main(["-s", "-v", "--headed", RunConfig.cases_path,
                         "--browser=" + RunConfig.browser,
                         "--alluredir=" + RunConfig.NEW_REPORT,
                         "--junit-xml=" + xml_report,
                         "--self-contained-html",
                         "--maxfail", RunConfig.max_fail,
                         "--reruns", RunConfig.rerun
                         ])
        logger.info("测试结束，生成测试报告💕 💕 💕 ！")
    except Exception as e:
        logger.error("脚本批量执行失败！", e)
        print("脚本批量执行失败！", e)

    # 2、生成allure的html报告
    try:
        cmd = 'allure generate %s -o %s --clean' % (RunConfig.NEW_REPORT, RunConfig.NEW_REPORT+'/exportReport')
        print(cmd)
        print("开始执行报告生成")
        invoke(cmd)
        print("报告生成完毕")
    except Exception as e:
        print("报告生成失败，请重新执行", e)
        raise

    # # 3、发送邮件
    # try:
    #     Send_email.send_mail_report("接口测试报告")
    #
    # except Exception as e:
    #     print("发送邮件失败，请重新执行", e)
    #     raise
if __name__ == '__main__':
    myrunner()


