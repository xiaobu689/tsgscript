"""
上海静安

抓任意包请求头 token
变量名: SHJA_TOKEN

cron: 13 8 * * *
const $ = new Env("上海静安");
"""
import os
import random
import time
import requests
from urllib3.exceptions import InsecureRequestWarning, InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)


class SHJA():
    name = "上海静安"

    def __init__(self, token):
        self.token = token
        self.verify = False
        self.headers = {
            'Host': 'jaapi.shmedia.tech',
            'Accept': '*/*',
            'version': '3.2.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-Hans-CN;q=1',
            'token': self.token,
            'Content-Type': 'application/json; charset=utf-8',
            # 'deviceId': '2fb0f9344555405abc65648642bfda94',
            'User-Agent': 'JingAn/3.2.2 (iPhone; iOS 16.6; Scale/3.00)',
            'Connection': 'keep-alive',
            'siteId': '310106',
            # 'Cookie': 'tfstk=fp6KaLmDefHzY31lsMNGzQx7sk9K9TIU6wSjEUYnNNQOSapkEMshyQQh56AW-TX-eZ7LYQTuYUnJ5gf3YajS23_G5adzYUYWyaj5tHe0nMSeUL68o-2c3lYd79LSrLZvPeZbor20IMSeULacZ_5PJCKy5DGWRaT6C3L6A3t5PFO6cn0BFL_5flKkcXiBR3Os53xp_BZvrR8ZeOcwK-7YP8MjhOK6kE_L8Y-1oHn6o1LwbhWtFBLfAFH8uKSzjUARXyM2z19Ckp1T5vphJO_vd1UspK1VxpjPoZbAVluDk3cLXTGraBtgIle64GR5i9x9olVoabRddhL0XlhraBtwXEqN8bly991..',
        }

    def userinfo(self):
        json_data = {}
        url = 'https://jaapi.shmedia.tech/media-basic-port/api/app/personal/get'
        response = requests.post(url, headers=self.headers, json=json_data, verify=self.verify).json()
        if response['code'] == 0:
            print("----------------------------")
            print(f'🧑‍✈️账号：{response["data"]["nickname"]}')
            print(f'🧑‍✈️积分：{response["data"]["fullScore"]}')
            print("----------------------------")
        else:
            print(f'❌获取用户信息失败：{response}')

    def login_score(self):
        json_data = {}
        url = 'https://jaapi.shmedia.tech/media-basic-port/api/app/points/login/add'
        response = requests.post(url, headers=self.headers, json=json_data, verify=self.verify).json()
        # print(response)
        if response['code'] == 0:
            print("登录任务执行成功")

    def sign(self):
        json_data = {}
        url = 'https://jaapi.shmedia.tech/media-basic-port/api/app/personal/score/sign'
        response = requests.post(url, headers=self.headers, json=json_data, verify=self.verify).json()
        if response['code'] == 0:
            print(f'✅{response["data"]["title"]}')
        else:
            print(f'❌签到任务失败：{response}')

    def task_list(self):
        sign_days_str = ''
        today_scores = ''
        jobs = []
        json_data = {'id': 'string'}
        url = 'https://jaapi.shmedia.tech/media-basic-port/api/app/personal/score/info'
        response = requests.post(url, headers=self.headers, json=json_data, verify=self.verify).json()
        if response['code'] == 0:
            sign_days_str = response["data"]["signTitle"]
            today_scores = response["data"]["todayPoint"]
            jobs = response["data"]["jobs"]
            print("-----------------------")
            print(f'🐹🐹🐹任务列表🐹🐹🐹')
            print("-----------------------")
            for i in jobs:
                if "完善个人资料" in i["title"] or "填写邀请码" in i["title"]:
                    continue
                now_pro = f'{i["progress"]}/{i["totalProgress"]}'
                print(f'👻{i["title"]}: {"已完成" if i["status"] == "1" else now_pro}')
            print("-----------------------")
            print(f'👀今日新增积分: {today_scores}')
            print(f'👀{sign_days_str}')

        return response

    def article_list(self):
        json_data = {
            'orderBy': 'release_desc',
            'channel': {
                'id': 'bf43bbcfd13e4b7ca7692e8a4629f461',
            },
            'pageSize': 50,
            'pageNo': 1,
        }
        url = 'https://jaapi.shmedia.tech/media-basic-port/api/app/news/content/list'
        response = requests.post(url, headers=self.headers, json=json_data, verify=self.verify).json()

        return response['data']['records']

    def article_read_task(self, id):
        status_codes = []
        # 阅读
        json_data = {
            'id': id,
        }
        url = 'https://jaapi.shmedia.tech/media-basic-port/api/app/news/content/get'
        response_get = requests.post(url, headers=self.headers, json=json_data, verify=self.verify).json()
        status_codes.append(response_get.get('code', None))
        # 扣减
        json_data = {
            'id': id,
            'countType': 'contentRead',
        }
        url = 'https://jaapi.shmedia.tech/media-basic-port/api/app/common/count/usage/inc'
        response = requests.post(url, headers=self.headers, json=json_data, verify=self.verify).json()
        status_codes.append(response.get('code', None))
        # 积分
        json_data = {}
        url = 'https://jaapi.shmedia.tech/media-basic-port/api/app/points/read/add'
        response = requests.post(url, headers=self.headers, json=json_data, verify=self.verify).json()
        status_codes.append(response.get('code', None))
        if all(code == 0 for code in status_codes):
            print(f'✅文章{id} 阅读成功')
        else:
            print(f'文章{id}阅读失败：{response_get}')

    def article_favor_task(self, id):
        status_codes = []
        # 收藏
        json_data = {
            'id': id,
        }
        url = 'https://jaapi.shmedia.tech/media-basic-port/api/app/news/content/favor'
        response_favor = requests.post(url, headers=self.headers, json=json_data, verify=self.verify).json()
        status_codes.append(response_favor.get('code', None))
        # 积分
        json_data = {}
        url = 'https://jaapi.shmedia.tech/media-basic-port/api/app/points/favor/add'
        response = requests.post(url, headers=self.headers, json=json_data, verify=self.verify).json()
        status_codes.append(response.get('code', None))
        if all(code == 0 for code in status_codes):
            print(f'✅文章{id} 收藏成功')
        else:
            print(f'❌文章{id} 收藏失败：{response_favor}')

    def article_share_task(self, id):
        json_data = {}
        url = 'https://jaapi.shmedia.tech/media-basic-port/api/app/points/share/add'
        response = requests.post(url, headers=self.headers, json=json_data, verify=self.verify).json()
        if response['code'] == 0:
            print(f'✅文章{id} 分享成功')
        else:
            print(f'❌文章{id} 分享失败：{response}')

    def video_view_task(self):
        json_data = {}
        url = 'https://jaapi.shmedia.tech/media-basic-port/api/app/points/video/add'
        response = requests.post(url, headers=self.headers, json=json_data, verify=self.verify).json()
        if response['code'] == 0:
            print(f'✅一条视频已经观看完成')
        else:
            print(f'❌视频观看失败：{response}')

    # 直播
    def live_streaming(self):
        json_data = {}
        url = 'https://jaapi.shmedia.tech/media-basic-port/api/app/points/live/add'
        response = requests.post(url, headers=self.headers, json=json_data, verify=self.verify).json()

    def gift_list(self):
        # TODO
        print('--------------------')
        print('🐹🐹🐹可兑换商品列表🐹🐹🐹')
        print('--------------------')
        print('😂积分太少啦，暂无商品可兑换')

    def main(self):
        self.userinfo()
        self.sign()
        article_list = self.article_list()
        counter = 0
        for i in article_list:
            article_id = random.choice(article_list)["id"]
            print('--------------------------------------------------------------------')
            print(f'🐹随机抓取到文章{i}: {article_id}，开始做任务啦......')
            if counter > 12:
                break
            self.article_read_task(article_id)
            time.sleep(random.randint(20, 30))
            self.article_share_task(article_id)
            time.sleep(random.randint(10, 18))
            if counter <= 5:
                self.article_favor_task(article_id)
                time.sleep(random.randint(10, 20))
            counter += 1
        for i in range(5):
            self.video_view_task()
            time.sleep(random.randint(20, 30))
        self.task_list()
        self.gift_list()


if __name__ == '__main__':
    env_name = 'SHJA_TOKEN'
    token = os.getenv(env_name)
    if not token:
        print(f'⛔️未获取到ck变量：请检查变量 {env_name} 是否填写')
        exit(0)

    SHJA(token).main()
