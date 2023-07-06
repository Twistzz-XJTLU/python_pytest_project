import os

import requests
from jenkins import Jenkins

jenkins_url = "http://localhost:8080/"
server = Jenkins(jenkins_url, username='twistzz', password='963852741')
job_name = "job/python_pytest"
job_url = server.get_info(job_name)['url']
job_last_number = server.get_info(job_name)['lastBuild']['number']
report_url = job_url + str(job_last_number) + '/allure'


def push_message():
    content = {}
    file_path = "C:/Users/twist/.jenkins/workspace/python_pytest/allure-report/export/prometheusData.txt"
    f = open(file_path)
    for line in f.readlines():
        launch_name = line.strip('\n').split(' ')[0]
        num = line.strip('\n').split(' ')[1]
        content.update({launch_name: num})
    f.close()
    print(content)
    passed_num = content['launch_status_passed']  # 通过数量
    failed_num = content['launch_status_failed']  # 失败数量
    broken_num = content['launch_status_broken']  # 阻塞数量
    skipped_num = content['launch_status_skipped']  # 跳过数量
    case_num = content['launch_retries_run']  # 总数量
    """
    企业微信消息发送，通过webhook发送消息
    """
    webhook = "https://oapi.dingtalk.com/robot/send?access_token=0cc4e11c529be112b428b5a30ba51295d16e82ecec2013c4160bdf2cd72d527d"
    content = {
        "msgtype": "text",
        "text": {
            "content": "接口自动化脚本执行结果：\n运行总数" + case_num
                       + "\n通过数量：" + passed_num
                       + "\n失败数量：" + failed_num
                       + "\n阻塞数量：" + broken_num
                       + "\n跳过数量：" + skipped_num
                       + "\n构建地址：\n" + job_url
                       + "\n报告地址：" + report_url
        }
    }
    requests.post(url=webhook, json=content)


push_message()
