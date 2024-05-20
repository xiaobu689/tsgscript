"""
上海长宁
抓任意包请求头 token
变量名: QDXW_TOKEN
cron: 35 10 * * *
const $ = new Env("上海长宁");
"""
import os
import random
import time
import requests


class SHCN():
    name = "上海长宁"

    def __init__(self, token):
        self.token = token
        self.verify = False
        self.headers = {
            'Host': 'cnapi.shmedia.tech',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-Hans-CN;q=1',
            'token': self.token,
            'Content-Type': 'application/json; charset=utf-8',
            'deviceId': 'af223dabdc3b484c8eae7809f6da7ba6',
            'User-Agent': 'StandardApplication/6.2.7 (iPhone; iOS 16.6; Scale/3.00)',
            'Connection': 'keep-alive'
        }

    def sign(self):
        json_data = {}
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/personal/score/sign'
        response = requests.post(url, headers=self.headers, json=json_data, verify=False).json()
        # print(response)
        if response['code'] == 0:
            print(f'✅{response["data"]["title"]}')
        else:
            print(f'❌{response["msg"]}')

    def total_score(self):
        json_data = {}
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/personal/score/total'
        response = requests.post(url, headers=self.headers, json=json_data, verify=False).json()
        if response['code'] == 0:
            print(f'✅当前总积分：{response["data"]["score"]}')
        else:
            print(f'❌总积分获取失败：{response}')

    def today_score(self):
        json_data = {}
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/personal/score/info'
        response = requests.post(url, headers=self.headers, json=json_data, verify=False).json()
        if response['code'] == 0:
            print(f'✅今日新增积分：{response["data"]["todayIncreasePoint"]}')
        else:
            print(f'❌今日积分获取失败：{response}')

    def task_list(self):
        json_data = {}
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/personal/score/info'
        response = requests.post(url, headers=self.headers, json=json_data, verify=False).json()
        print(f'👀任务列表：response=', response)
        if response['code'] == 0:
            print(f'👀任务列表👀')
            for i in response['data']['jobs']:
                print(f'👻{i["title"]}: {"已完成" if i["status"] == "1" else "未完成"}')

    def article_list(self):
        json_data = {
            'orderBy': 'release_desc',
            'channel': {
                'id': 'fc83f7ef2a6f4c9d826cba3702adcc78',
            },
            'pageSize': 20,
            'pageNo': 1,
        }
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/news/content/list'
        response = requests.post(url, headers=self.headers, json=json_data, verify=False).json()
        # print(response)

        return response["data"]["records"]

    def article_read_points_add(self):
        json_data = {}
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/points/read/add'
        response = requests.post(url, headers=self.headers, json=json_data, verify=False).json()

    def article_count_usage_desc(self, id):
        json_data = {
            'id': id,
            'countType': 'contentRead',
        }
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/common/count/usage/inc'
        response = requests.post(url, headers=self.headers, json=json_data, verify=False).json()

    def article_read(self, id):
        json_data = {'id': id}
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/news/content/get'
        response = requests.post(url, headers=self.headers, json=json_data, verify=False).json()
        if response['code'] == 0:
            self.article_read_points_add()
            self.article_count_usage_desc(id)
            print(f'✅文章{response["data"]["id"]} 阅读成功')
        else:
            print(f'❌阅读失败，{response}')

    def article_favor(self, id):
        json_data = {'id': id}
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/news/content/favor'
        response = requests.post(url, headers=self.headers, json=json_data, verify=False).json()
        if response['code'] == 0:
            print(f'✅文章{response["data"]["id"]} 收藏成功')
        else:
            print(f'❌收藏失败，{response}')

    def article_share(self, id):
        json_data = {}
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/points/share/add'
        response = requests.post(url, headers=self.headers, json=json_data, verify=False).json()
        if response['code'] == 0:
            print(f'✅文章{id} 分享成功')
        else:
            print(f'❌分享失败，{response}')

    def gift_list(self):
        # TODO
        print('--------------------')
        print('👀可兑换商品列表👀')
        print('--------------------')
        print('😂积分太少啦，暂无商品可兑换')

    def main(self):
        self.sign()
        self.task_list()
        counter = 0
        list = self.article_list()
        for i in list:
            if counter >= 3:
                break
            self.article_read(i["id"])
            time.sleep(random.randint(20, 30))
            self.article_share(i["id"])
            time.sleep(random.randint(10, 18))
            if counter <= 5:
                self.article_favor(i["id"])
                time.sleep(random.randint(10, 20))
            counter += 1
        self.total_score()
        self.today_score()
        self.gift_list()


if __name__ == '__main__':
    env_name = 'SHCN_TOKEN'
    token = os.getenv(env_name)
    if not token:
        print(f'⛔️未获取到ck变量：请检查变量 {env_name} 是否填写')
        exit(0)

    SHCN(token).main()
