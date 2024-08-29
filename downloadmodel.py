#!usr/bin/env python
# encoding:utf-8
from __future__ import division
 
import os
import time
import logging
import subprocess
import urllib
import requests
import torch
import random
from pathlib import Path
 
def autoDownload(filePath="model.txt", downloadDir="model/yolov8/"):
    if not os.path.exists(downloadDir):
        os.makedirs(downloadDir)
    while True:
        with open(filePath) as f:
            lists = [one.strip() for one in f.readlines() if one.strip()]
        count = 0
        for downloadUrl in lists:
            print("模型下载地址: ", downloadUrl)
            try:
                tmpFile = downloadDir + downloadUrl.split("/")[-1].strip()
                print("下载文件路径: ", tmpFile)
                if not os.path.exists(tmpFile):
                    torch.hub.download_url_to_file(downloadUrl, str(tmpFile))
                else:
                    print("当前训练模型文件已经下载完成!")
                    count += 1
            except Exception as e:
                print("Exception: ", e)
                time.sleep(random.randint(1, 5))
        print("下载数量为: ", count)
        if count == len(lists):
            break
 
if __name__ == "__main__":
 
    autoDownload(filePath="model.txt", downloadDir="model/")