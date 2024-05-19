"""
哈罗单车

路径：哈罗单车APP
用途：签到、看视频得鼓励金，鼓励金兑骑行券、话费
变量名：hello_token
格式： 任意请求头抓 Authorization 值

定时设置：每天一次就行，时间随意
cron: 26 11 * * *
const $ = new Env("哈罗单车");
"""
import os
import random
import time
import requests
from datetime import datetime
from sendNotify import send


class TTCY():
    def __init__(self):
        self.cookie = ''

    def hello_sign(self):
        headers = {
            'Host': 'api.hellobike.com',
            'Accept': 'application/json, text/plain, */*',
            'Sec-Fetch-Site': 'same-site',
            'requestId': '4uXHKDCygcAAksp',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Sec-Fetch-Mode': 'cors',
            'Content-Type': 'application/json',
            'Origin': 'https://m.hellobike.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/20G75 Ariver/1.0.15  NebulaSDK; app=easybike; version=6.62.5 WK RVKType(1) NebulaX/1.0.0',
            'Referer': 'https://m.hellobike.com/',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
        }

        json_data = {
            'from': 'h5',
            'systemCode': 61,
            'platform': 4,
            'version': '6.62.5',
            'action': 'common.welfare.signAndRecommend',
            'token': '1031e52fbecf434194e336918cd460a7',
        }

        url = 'https://api.hellobike.com/api?common.welfare.signAndRecommend'
        response = requests.post(url, headers=headers, json=json_data).json()
        # print(response)
        if response['code'] == 0 and response['data']['didSignToday']:
            msg = f'✅签到成功, 奖励金：+{response["data"]["bountyCountToday"]}'
        else:
            msg = '❌签到失败， cookie可能已失效！'

        print(msg)
        return msg

    def main(self):
        self.hello_sign()

        # 通知
        # send(title, msg)


if __name__ == '__main__':
    # env_name = 'TTCY_COOKIE'
    # cookie = os.getenv(env_name)
    # # if not cookie:
    # #     print(f'⛔️未获取到ck变量：请检查变量 {env_name} 是否填写')
    # #     exit(0)
    token = ''

    TTCY().main()