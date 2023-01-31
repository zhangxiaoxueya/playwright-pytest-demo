#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import os
"""邮件配置"""
sender = ''  #发送方
receiver = '' #接收方
emailusername = ''  #登陆邮箱的用户名
emailpassword = ''  #登陆邮箱的授权码，客户端专用密码
server = ''  #smtp服务器
smtp_server_port = ''


#项目配置
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# page目录
page_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'page')

# case目录
case_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_case')

#数据目录
data_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')

# 报告目录
report_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_report')

#日志目录
log_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'log')

# os.path.abspath(path) #返回绝对路径
# os.path.basename(path) #返回文件名
# os.path.dirname(path) #返回文件路径
# os.path.join(path1[, path2[, ...]])  #把目录和文件名合成一个路径

