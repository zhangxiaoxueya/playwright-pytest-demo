#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Time    : 2021/10/22 3:16 下午 
@File    : util.py
@Author  : zhangxue
@Desc    : 工具类
'''
import datetime
import subprocess

"""获取当前时间"""
def get_nowtime():
    # now_time = datetime.datetime.now()
    now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return now_time


"""执行shell脚本"""
def invoke(cmd):
    output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
    o = output.decode("utf-8")
    return o




