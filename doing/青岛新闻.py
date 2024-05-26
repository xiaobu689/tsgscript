"""
上海长宁

抓任意包请求头 token
变量名: SHCN_TOKEN

cron: 35 10 * * *
const $ = new Env("上海长宁");
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


class SHCN():
    name = "青岛新闻"

    def __init__(self, tokenStr):
        self.token = tokenStr
        self.headers = {
            'Host': 'appnews.qingdaonews.com',
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Cookie': 'appnews_deviceInfo=YTo1OntzOjEyOiJtYWNoaW5lX2NvZGUiO3M6MzY6IjFGMEQzRDBGLTI3ODEtNEMxMS05QUU3LTkyMzc5ODA2MzU0RSI7czo3OiJ1c2VyX2lkIjtzOjg6IjExNzc5NzMxIjtzOjk6InVzZXJfdHlwZSI7aToxO3M6OToidHlwZV90ZXN0IjtzOjM6ImFwaSI7czo5OiJ0X3VzZXJfaWQiO3M6ODoiMTQzMjY4MjEiO30%3D; NSC_bqqofxt=ffffffff09022cbc45525d5f4f58455e445a4a423660; sto-id-20480-appnews_pool=KNDCAKAKFAAA; password=9i%2FNdBIygBSRfCVNaIgoWzwkPMuk9ncH; password_NS_Sig=oenCV6idkGc14wbC; token=9i%2FNdBIygBSRfCVNaIgoWzwkPMuk9ncH; uid=11779731; username=TZA7%2BiiCuW5rks5Gnrjvkw%3D%3D; username_NS_Sig=oenCV6iZ_VRRqFbO; PHPSESSID=664b075b787c13.93774969; PHPSESSID_NS_Sig=oenCV6manzgktFOz',
            'vtoken': 'GKxKSCYLrVWSuTZrL-VmJ1Md5Gp_ZcxNxkqt8CrvwwLkEOaFAbN5lLaPhnMb78GIyYuVOFkbJssUlesI0_OU7IH8MSLwZpucSoGEYeEfyWMi-1aaMTyjRINmQxF9zVZAg19PD-_M5P54IxfLhGX_b78aFn-ndv0-JaDHIdO3CY4U8gQIytwVz_XnQTOPCDiB4Nspm-RlwQv7A3_vpS0_1ZOH91XQIkiVY09dmaeBTCzWx-nIiqgiHHTtZu7w1ufPSImjHKkEslutpGDztXAr0mT6ehCSzS5pEjQgTMQ-VH_AxefB2w0tKoAyGfABW7AtW2gwyicNMDTjaPPP5kyjuw',
            'User-Agent': 'NewsApp/qdnews/6.10.10 (iPhone; iOS 16.6; Scale/3.00)',
            'Accept-Language': 'zh-Hans-CN;q=1',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
        }

    def userinfo(self):
        url = 'https://appnews.qingdaonews.com/api/user_info/detail'
        response = requests.get(url, headers=self.headers).json()
        if response['error_code'] == 0:
            print("----------------------------")
            print(f'🧑‍✈️账号：{response["result"]["user_id"]}')
            print(f'🧑‍✈️金币：{response["result"]["gold"]}')
            print("----------------------------")
        else:
            print(f'❌获取用户信息失败：{response}')

    def sign(self):
        data = {
            'sign': 'BSnCjQBureq8G3Bl4RnFgJ8hfUI_Uq0beETTGE64XxdZtcXrcjkQu8_T23t82FOBxpTkd3FoI-jepRwbb_AGn4wPGMO63A8HO-Qn0Gm9Ccz_6ncezsYss_Tj_WqwukvIW8snIBKosmkMyTmGnCxrtupONBMaND9oMzhuQ9vlmc7oUqfhnQooNSU-3O9KNY_XlqdirQ_zzPlw_FB5DuQtoPkVH-JRZvvFHaBDyz3Ho_5IaE8kWfNVRp6MCx_Sp0ruIHxdMxIWOS4MbvkWRwmNbJdiNjo1_ubbWEHL0DC_CJ0Gjy6oh7PSSHnvxRTE8SMUlxGn9zbXm0RMRLVX-HQ8_g',
        }
        url = 'https://appnews.qingdaonews.com/api/user_signinday/thing'
        response = requests.post(url, headers=self.headers, data=data).json()
        print("----------response=", response)

    def main(self):
        self.userinfo()
        self.sign()


if __name__ == '__main__':
    # env_name = 'SHCN_TOKEN'
    # tokenStr = os.getenv(env_name)
    # if not tokenStr:
    #     print(f'⛔️未获取到ck变量：请检查变量 {env_name} 是否填写')
    #     exit(0)

    SHCN('').main()
