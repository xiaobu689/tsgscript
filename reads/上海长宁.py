"""
上海长宁

抓任意包请求头 token
变量名: SHCN_TOKEN

cron: 32 9,17 * * *
const $ = new Env("上海长宁");
"""
import os
import random
import re
import time
import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import InsecureRequestWarning, InsecurePlatformWarning

from common import qianwen_messages, basic_news_question

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)


class SHCN():
    name = "上海长宁"

    def __init__(self, tokenStr):
        self.token = tokenStr.split('#')[0]
        self.isComment = tokenStr.split('#')[1]
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
            print("-----------------------")
            print(f'🐹🐹🐹任务列表🐹🐹🐹')
            print("-----------------------")
            for i in response['data']['jobs']:
                if "完善个人资料" in i["title"] or "填写邀请码" in i["title"]:
                    continue
                print(f'👻{i["title"]}: {"已完成" if i["status"] == "1" else "未完成"}')

    def article_list(self):
        json_data = {
            'orderBy': 'release_desc',
            'channel': {
                'id': 'fc83f7ef2a6f4c9d826cba3702adcc78',
            },
            'pageSize': 50,
            'pageNo': 1,
        }
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/news/content/list'
        response = requests.post(url, headers=self.headers, json=json_data, verify=False).json()

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

    def article_content(self, id):
        json_data = {'id': id}
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/news/content/get'
        response = requests.post(url, headers=self.headers, json=json_data, verify=False).json()
        return response

    def article_read(self, id):
        response = self.article_content(id)
        if response['code'] == 0:
            self.article_read_points_add()
            self.article_count_usage_desc(id)
            print(f'✅文章阅读成功')
        else:
            print(f'❌阅读失败，{response}')

    def article_favor(self, id):
        json_data = {'id': id}
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/news/content/favor'
        response = requests.post(url, headers=self.headers, json=json_data, verify=False).json()
        if response['code'] == 0:
            print(f'✅文章收藏成功')
        else:
            print(f'❌收藏失败，{response}')

    def article_share(self, id):
        json_data = {}
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/points/share/add'
        response = requests.post(url, headers=self.headers, json=json_data, verify=False).json()
        if response['code'] == 0:
            print(f'✅文章分享成功')
        else:
            print(f'❌文章分享失败，{response}')

    def video_view_task(self):
        json_data = {}
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/points/video/add'
        response = requests.post(url, headers=self.headers, json=json_data, verify=self.verify).json()
        if response['code'] == 0:
            print(f'✅看片儿完成+1')
        else:
            print(f'❌看片儿失败：{response}')

    def get_gpt_comment(self, id):
        article_concent = ''
        response = self.article_content(id)
        comment = ''
        commentCount = 0
        if response['code'] == 0:
            commentCount = response["data"]["count"]["commentCount"]
            if commentCount <= 0:
                content = response["data"]["txt"]
                soup = BeautifulSoup(content, 'html.parser')
                content_text = soup.get_text()
                message = qianwen_messages(basic_news_question, content_text)
                comment = message

        return comment

    def article_comment_add(self, id, content):
        json_data = {
            'displayResources': [],
            'content': content,
            'targetType': 'content',
            'targetId': id,
        }
        url = 'https://cnapi.shmedia.tech/media-basic-port/api/app/common/comment/add'
        response = requests.post(url, headers=self.headers, json=json_data).json()
        if response["code"] == 0:
            print(f'✅文章评论成功，评论内容：{content}')
        else:
            print(f'❌文章评论失败，{response}')

    def article_comment_task(self, id):
        comment = self.get_gpt_comment(id)
        if comment == '':
            print(f'😢未知错误或者文章可能评论过，算了吧，下一个')
        else:
            self.article_comment_add(id, comment)

    def gift_list(self):
        # TODO
        print('--------------------')
        print('🐹🐹🐹可兑换商品列表🐹🐹🐹')
        print('--------------------')
        print('😂积分太少啦，暂无商品可兑换')

    def main(self):
        self.sign()
        self.task_list()
        counter = 0
        article_list = self.article_list()
        # print(article_list)
        for i in article_list:
            if counter > 12:
                break
            article_id = random.choice(article_list)["id"]
            print('--------------------------------------------------------------------')
            print(f'🐹随机抓取到一篇文章: {article_id}，开始做任务......')
            self.article_read(article_id)
            time.sleep(random.randint(30, 60))
            self.article_comment_task(article_id)
            time.sleep(random.randint(10, 20))
            self.article_share(article_id)
            time.sleep(random.randint(10, 18))
            if self.isComment == 1:
                self.article_comment_task()
                time.sleep(random.randint(5, 10))
            if counter <= 5:
                self.article_favor(article_id)
                time.sleep(random.randint(10, 20))
            counter += 1
        for i in range(5):
            self.video_view_task()
            time.sleep(random.randint(20, 30))
        self.total_score()
        self.today_score()
        self.gift_list()


if __name__ == '__main__':
    env_name = 'SHCN_TOKEN'
    tokenStr = os.getenv(env_name)
    if not tokenStr:
        print(f'⛔️未获取到ck变量：请检查变量 {env_name} 是否填写')
        exit(0)

    SHCN(tokenStr).main()
