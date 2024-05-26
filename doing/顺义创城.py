"""
顺义创城

抓任意包请求头 token
变量名: SHCN_TOKEN

cron: 35 10 * * *
const $ = new Env("顺义创城");
"""
import os
import random
import re
import time
import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning, InsecurePlatformWarning

from common import qianwen_messages

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)


class SYCC():
    name = "顺义创城"

    def __init__(self, tokenStr):
        self.token = tokenStr
        self.headers = {
            'Host': 'admin.shunyi.wenming.city',
            'Connection': 'keep-alive',
            'X-Applet-Token': self.token,
            'content-type': 'application/json',
            'Accept-Encoding': 'gzip,compress,br,deflate',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x1800312d) NetType/WIFI Language/zh_CN',
            'Referer': 'https://servicewechat.com/wx0a035430a2e3a465/154/page-frame.html',
        }

    def userinfo(self):
        url = 'https://admin.shunyi.wenming.city/jeecg-boot/applet/user/userInfo'
        response = requests.get(url, headers=self.headers).json()
        if response['code'] == 200:
            print("----------------------------")
            print(f'🧑‍✈️账号：{response["result"]["phone"]}')
            print(f'🧑‍✈️积分：{response["result"]["score"]}')
            print("----------------------------")
        else:
            print("获取用户信息失败, ", response)

    def sign(self):
        url = 'https://admin.shunyi.wenming.city/jeecg-boot/applet/ccScoreRecord/signIn'
        response = requests.post(url, headers=self.headers).json()
        if response['code'] == 200:
            print("🎉签到成功")
        else:
            print("签到失败, ", response)

    def article_list(self):
        params = {
            'pageNo': '1',
            'pageSize': '20',
            'column': 'isTop,createTime',
            'order': 'desc',
        }
        url = 'https://admin.shunyi.wenming.city/jeecg-boot/applet/workNews/list'
        response = requests.get(url, params=params, headers=self.headers).json()
        if response['code'] == 200:
            list = response['result']['records']

    def checkout(self):
        url = 'https://admin.shunyi.wenming.city/jeecg-boot/applet/award/exchangeAward'
        data = '{"awardIds":["1788826595521810434"],"phone":"17854279565"}'
        response = requests.post(url, headers=self.headers, data=data).json()
        if response['code'] == 200:
            print("🎉兑换成功")
        else:
            print("❌兑换失败, ", response)


    def main(self):
        self.userinfo()
        # self.article_list()
        # self.sign()
        self.checkout()


if __name__ == '__main__':
    env_name = 'SYCC_TOKEN'
    tokenStr = os.getenv(env_name)
    tokenStr = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIxNzkzODczMDc4MjYwNDIwNjEwIn0.8_yB-FKynNIEYNGTlF1V5bS62RXOJuBqunytf--s-NM'
    if not tokenStr:
        print(f'⛔️未获取到ck变量：请检查变量 {env_name} 是否填写')
        exit(0)

    SYCC('').main()
