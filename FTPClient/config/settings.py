#!/usr/bin/env python
#coding=utf-8


import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_DIR)

# 服务端地址
FTP_SERVER_IP = "39.101.137.249"
FTP_SERVER_PORT = 3389

# 文件下载保存路径
DOWNLOAD_FILE_PATH = os.path.join(BASE_DIR, "download")

# 日志文件存放路径
LOGS = os.path.join(BASE_DIR, "logs","ftpclient.log")
