# -*- coding: utf-8 -*-
# @Time    : 2023/7/6 17:45
# @Author  : Twistzz
# @File : ding.py
import os

import requests
from jenkins import Jenkins

# jenkins_url = "http://127.0.0.1:8080/"
# server = Jenkins(jenkins_url, username='admin', password='123456')
# job_name = "job/ApiTest"
# job_url = server.get_info(job_name)['url']
# job_last_number = server.get_info(job_name)['lastBuild']['number']
# report_url = job_url + str(job_last_number) + '/allure'


def push_message():
    # content = {}
    # file_path = os.path.dirname(os.getcwd()) + '/allure-report/export/prometheusData.txt'
    # f = open(file_path)
    # for line in f.readlines():
    #     launch_name = line.strip('\n').split(' ')[0]
    #     num = line.strip('\n').split(' ')[1]
    #     content.update({launch_name: num})
    # f.close()
    # print(content)
    passed_num = "1"
    failed_num = "1"
    broken_num = "1"
    skipped_num = "1"
    case_num = "1"
    """
    企业微信消息发送，通过webhook发送消息
    """
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=0cc4e11c529be112b428b5a30ba51295d16e82ecec2013c4160bdf2cd72d527d"
    content = {
        "msgtype": "text",
        "text": {
            "content": "接口自动化脚本执行结果：\n运行总数" + case_num
                       + "\n通过数量：" + "test"
                       + "\n失败数量：" + "test"
                       + "\n阻塞数量：" + "test"
                       + "\n跳过数量：" + "test"
                       + "\n构建地址：\n" + "test"
                       + "\n报告地址：" + "test"
        }
    }
    res=requests.post(url=webhook, json=content)
    print(res.text)

push_message()
