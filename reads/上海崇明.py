"""
上海崇明

抓任意包请求头 token
变量名: SHCM_TOKEN

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

from common import qianwen_messages, make_request

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)


class SHCM():
    name = "上海崇明"

    def __init__(self, account_info):
        self.token = account_info.split('#')[0]
        self.isComment = account_info.split('#')[1]
        self.verify = False
        self.headers = {
            'Host': 'cmapi.shmedia.tech',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-Hans-CN;q=1',
            'token': self.token,
            'Content-Type': 'application/json; charset=utf-8',
            'deviceId': 'af223dabdc3b484c8eae7809f6da7ba6',
            'User-Agent': 'StandardApplication/6.2.7 (iPhone; iOS 16.6; Scale/3.00)',
            'Connection': 'keep-alive'
        }

    def login_score(self):
        json_data = {}
        url = 'https://cmapi.shmedia.tech/media-basic-port/api/app/points/login/add'
        response = make_request(url, json_data=json_data, method='post', headers=self.headers)
        # print(response)
        if response and response['code'] == 0:
            print("✅登录任务执行成功")

    def sign(self):
        json_data = {}
        url = 'https://cmapi.shmedia.tech/media-basic-port/api/app/personal/score/sign'
        response = make_request(url, json_data, 'post', self.headers)
        # print(response)
        if response and response['code'] == 0:
            print(f'✅{response["data"]["title"]}')
        else:
            print(f'❌{response["msg"]}')

    def total_score(self):
        json_data = {}
        url = 'https://cmapi.shmedia.tech/media-basic-port/api/app/personal/score/total'
        response = make_request(url, json_data, 'post', self.headers)
        if response and response['code'] == 0:
            print(f'✅当前总积分：{response["data"]["score"]}')
        else:
            print(f'❌总积分获取失败：{response}')

    def today_score(self):
        json_data = {}
        url = 'https://cmapi.shmedia.tech/media-basic-port/api/app/personal/score/info'
        response = make_request(url, json_data, 'post', self.headers)
        if response and response['code'] == 0:
            print(f'✅今日新增积分：{response["data"]["todayIncreasePoint"]}')
            # return response["data"]["jobs"]
        else:
            print(f'❌今日积分获取失败：{response}')

    def task_list(self):
        json_data = {}
        url = 'https://cmapi.shmedia.tech/media-basic-port/api/app/personal/score/info'
        response = make_request(url, json_data, 'post', self.headers)
        if response and response['code'] == 0:
            print("-----------------------")
            print(f'🐹🐹🐹任务列表🐹🐹🐹')
            print("-----------------------")
            for i in response['data']['jobs']:
                if "完善个人资料" in i["title"] or "填写邀请码" in i["title"]:
                    continue
                print(f'👻{i["title"]}: {"已完成" if i["status"] == "1" else "未完成"}')

    def article_list(self):
        channels = ["8e23b0c300464d19af63373e4fa8c70c", "a151a558a788459795390b19041d3a12",
                    "7e59ea39a0ab49978c58c6e9a5c95bca", "3f32881cc9d64a78a3f10bc4482e9f3d",
                    "e0bdf28d1adb4a509884b11db6d01d52"]
        channel = random.choice(channels)
        json_data = {
            'orderBy': 'release_desc',
            'channel': {
                'id': channel,
            },
            'pageSize': 50,
            'pageNo': 1,
        }
        url = 'https://cmapi.shmedia.tech/media-basic-port/api/app/news/content/list'
        response = make_request(url, json_data, 'post', self.headers)

        return response["data"]["records"]

    def article_read_points_add(self):
        json_data = {}
        url = 'https://cmapi.shmedia.tech/media-basic-port/api/app/points/read/add'
        make_request(url, json_data, 'post', self.headers)

    def article_count_usage_desc(self, id):
        json_data = {
            'id': id,
            'countType': 'contentRead',
        }
        url = 'https://cmapi.shmedia.tech/media-basic-port/api/app/common/count/usage/inc'
        make_request(url, json_data, 'post', self.headers)

    def article_content(self, id):
        json_data = {'id': id}
        url = 'https://cmapi.shmedia.tech/media-basic-port/api/app/news/content/get'
        response = make_request(url, json_data, 'post', self.headers)
        return response

    def article_read(self, id):
        response = self.article_content(id)
        if response and response['code'] == 0:
            self.article_read_points_add()
            self.article_count_usage_desc(id)
            print(f'✅文章阅读成功')
        else:
            print(f'❌阅读失败，{response}')

    def article_favor(self, id):
        json_data = {'id': id}
        url = 'https://cmapi.shmedia.tech/media-basic-port/api/app/news/content/favor'
        response = make_request(url, json_data, 'post', self.headers)
        if response and response['code'] == 0:
            print(f'✅文章收藏成功')
        else:
            print(f'❌收藏失败，{response}')

    def article_favor_task(self, id):
        response_content = self.article_content(id)
        if response_content and response_content['code'] == 0:
            if response_content['data']['count']["favorite"] is False:
                self.article_favor(id)
            elif response_content['data']['count']["favorite"]:
                print(f'已经收藏过了，不再重复收藏')
            else:
                print(f'❌收藏失败，{response_content}')
        else:
            print(f'❌获取文章失败，{response_content}')

    def article_share(self, id):
        json_data = {}
        url = 'https://cmapi.shmedia.tech/media-basic-port/api/app/points/share/add'
        response = make_request(url, json_data, 'post', self.headers)
        if response and response['code'] == 0:
            print(f'✅文章分享成功')
        else:
            print(f'❌文章分享失败，{response}')

    def article_like(self, id):
        json_data = {
            "id": id
        }
        url = 'https://cmapi.shmedia.tech/media-basic-port/api/app/news/content/like'
        response = make_request(url, json_data, 'post', self.headers)
        if response and response['code'] == 0:
            print(f'✅文章点赞成功')
        else:
            print(f'❌文章点赞失败，{response}')

    def video_view_task(self):
        json_data = {}
        url = 'https://cmapi.shmedia.tech/media-basic-port/api/app/points/video/add'
        response = requests.post(url, headers=self.headers, json=json_data, verify=self.verify).json()
        if response and response['code'] == 0:
            print(f'✅看片儿完成+1')
        else:
            print(f'❌看片儿失败：{response}')

    def get_gpt_comment(self, id):
        basic_news_question = '我需要你针对下面的文章，从一个普通民众的角度进行评论，我希望你的输出只有评论内容，没有别的无关紧要的词语，回复格式是：芝麻开门#你的评论#， 评论语气要尽可能生活化、日常化，字数限制在5-15字之间，下面是我需要你发表评论的文章内容：'
        article_concent = ''
        response = self.article_content(id)
        comment = ''
        commentCount = 0
        if response and response['code'] == 0:
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
        url = 'https://cmapi.shmedia.tech/media-basic-port/api/app/common/comment/add'
        response = requests.post(url, headers=self.headers, json=json_data).json()
        if response and response["code"] == 0:
            print(f'✅文章评论成功')
        else:
            print(f'❌文章评论失败，{response}')

    def article_comment_task(self, id):
        comment = self.get_gpt_comment(id)
        if comment == '':
            print(f'😢未知错误或者文章可能评论过，算了吧，下一个')
        else:
            parts = comment.split('#')
            if len(parts) > 1:
                comment = parts[1].strip()
            print(f'🐌预评论内容：【{comment}】, 你没意见我就在20s后评论了哈......')
            time.sleep(random.randint(20, 25))
            self.article_comment_add(id, comment)

    def gift_list(self):
        # TODO
        print('--------------------')
        print('🐹🐹🐹可兑换商品列表🐹🐹🐹')
        print('--------------------')
        print('😂积分太少啦，暂无商品可兑换')

    def main(self):
        counter = 0
        self.login_score()
        self.sign()
        for j in range(2):
            self.video_view_task()
            time.sleep(random.randint(20, 30))
        article_list = self.article_list()
        # print(article_list)
        for i in range(7):
            article_id = random.choice(article_list)["id"]
            print('--------------------------------------------------------------------')
            print(f'🐹随机抓取到一篇文章{article_id}，开始做任务......')
            self.article_read(article_id)
            time.sleep(random.randint(20, 35))
            if counter <= 2:
                if self.isComment == '1':
                    self.article_comment_task(article_id)
                    time.sleep(random.randint(20, 40))
                else:
                    print("未开启自动评论, 如要开启，请更改环境变量配置")
                    time.sleep(random.randint(10, 25))
                self.article_favor_task(article_id)
                time.sleep(random.randint(10, 20))
                self.article_share(article_id)
                time.sleep(random.randint(10, 18))
                self.article_like(article_id)
                time.sleep(random.randint(10, 18))
            counter += 1
        self.total_score()
        self.today_score()
        self.gift_list()


if __name__ == '__main__':
    env_name = 'SHCM_TOKEN'
    tokenStr = os.getenv(env_name)
    if not tokenStr:
        print(f'⛔️未获取到ck变量：请检查变量 {env_name} 是否填写')
        exit(0)
    tokens = re.split(r'&', tokenStr)
    print(f"上海崇明共获取到{len(tokens)}个账号")
    for i, account_info in enumerate(tokens, start=1):
        print(f"\n======== ▷ 第 {i} 个账号 ◁ ========")
        SHCM(account_info).main()
        print("\n随机等待30-60s进行下一个账号")
        time.sleep(random.randint(30, 60))
