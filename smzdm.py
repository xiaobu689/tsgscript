"""
什么值得买签到
定时设置：
cron: 30 7 * * *
const $ = new Env("什么值得买");
"""
import hashlib
import os
import re
import time
import requests
import urllib3

from sendNotify import send

urllib3.disable_warnings()


class SMZDM():
    name = "什么值得买"

    def __init__(self, cookie):
        self.cookie = cookie

    def robot_token(self, headers):
        ts = int(round(time.time() * 1000))
        url = "https://user-api.smzdm.com/robot/token"
        data = {
            "f": "android",
            "v": "10.4.1",
            "weixin": 1,
            "time": ts,
            "sign": hashlib.md5(
                bytes(
                    f"f=android&time={ts}&v=10.4.1&weixin=1&key=apr1$AwP!wRRT$gJ/q.X24poeBInlUJC",
                    encoding="utf-8",
                )
            )
            .hexdigest()
            .upper(),
        }
        html = requests.post(url=url, headers=headers, data=data)
        result = html.json()
        token = result["data"]["token"]
        return token

    def sign(self, headers, token):
        Timestamp = int(round(time.time() * 1000))
        data = {
            "f": "android",
            "v": "10.4.1",
            "sk": "ierkM0OZZbsuBKLoAgQ6OJneLMXBQXmzX+LXkNTuKch8Ui2jGlahuFyWIzBiDq/L",
            "weixin": 1,
            "time": Timestamp,
            "token": token,
            "sign": hashlib.md5(
                bytes(
                    f"f=android&sk=ierkM0OZZbsuBKLoAgQ6OJneLMXBQXmzX+LXkNTuKch8Ui2jGlahuFyWIzBiDq/L&time={Timestamp}&token={token}&v=10.4.1&weixin=1&key=apr1$AwP!wRRT$gJ/q.X24poeBInlUJC",
                    encoding="utf-8",
                )
            )
            .hexdigest()
            .upper(),
        }
        url = "https://user-api.smzdm.com/checkin"
        resp = requests.post(url=url, headers=headers, data=data)
        error_msg = resp.json()["error_msg"]
        return error_msg, data

    def all_reward(self, headers, data):
        url2 = "https://user-api.smzdm.com/checkin/all_reward"
        resp = requests.post(url=url2, headers=headers, data=data)
        result = resp.json()
        msgs = []
        if "normal_reward" in result["data"]:
            normal_reward = result["data"]["normal_reward"]
            msgs = [
                {
                    "name": "✅签到奖励",
                    "value": normal_reward["reward_add"]["content"],
                },
                {
                    "name": "✅连续签到",
                    "value": normal_reward["sub_title"],
                },
            ]
        return msgs

    def active(self):
        cookie = self.cookie
        zdm_active_id = ["ljX8qVlEA7"]
        for active_id in zdm_active_id:
            url = f"https://zhiyou.smzdm.com/user/lottery/jsonp_draw?active_id={active_id}"
            rewardurl = f"https://zhiyou.smzdm.com/user/lottery/jsonp_get_active_info?active_id={active_id}"
            infourl = "https://zhiyou.smzdm.com/user/"
            headers = {
                "Host": "zhiyou.smzdm.com",
                "Accept": "*/*",
                "Connection": "keep-alive",
                "Cookie": cookie,
                "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/smzdm 10.4.6 rv:130.1 (iPhone 13; iOS 15.6; zh_CN)/iphone_smzdmapp/10.4.6/wkwebview/jsbv_1.0.0",
                "Accept-Language": "zh-CN,zh-Hans;q=0.9",
                "Referer": "https://m.smzdm.com/",
                "Accept-Encoding": "gzip, deflate, br",
            }
            response = requests.post(url=url, headers=headers).json()
            response_info = requests.get(url=infourl, headers=headers).text
            _ = requests.get(url=rewardurl, headers=headers).json()
            name = (
                str(
                    re.findall(
                        '<a href="https://zhiyou.smzdm.com/user"> (.*?) </a>',
                        str(response_info),
                        re.S,
                    )
                )
                .replace("[", "")
                .replace("]", "")
                .replace("'", "")
            )
            level = (
                str(
                    re.findall(
                        r'<img src="https://res.smzdm.com/h5/h5_user/dist/assets/level/(.*?).png\?v=1">',
                        str(response_info),
                        re.S,
                    )
                )
                .replace("[", "")
                .replace("]", "")
                .replace("'", "")
            )
            gold = (
                str(
                    re.findall(
                        '<div class="assets-part assets-gold">\n                    (.*?)</span>',
                        str(response_info),
                        re.S,
                    )
                )
                .replace("[", "")
                .replace("]", "")
                .replace("'’", "")
                .replace('<span class="assets-part-element assets-num">', "")
                .replace("'", "")
            )
            silver = (
                str(
                    re.findall(
                        '<div class="assets-part assets-prestige">\n                    (.*?)</span>',
                        str(response_info),
                        re.S,
                    )
                )
                .replace("[", "")
                .replace("]", "")
                .replace("'’", "")
                .replace('<span class="assets-part-element assets-num">', "")
                .replace("'", "")
            )
            msg = [
                {
                    "name": "✅签到结果",
                    "value": response["error_msg"],
                },
                {"name": "✅等级", "value": level},
                {"name": "✅昵称", "value": name},
                {"name": "✅金币", "value": gold},
                {"name": "✅碎银", "value": silver},
            ]
        return msg

    # 签到额外奖励
    # def extra_reward(self, headers):
    #     continue_checkin_reward_show = False
    #     userdata_v2 = self.show_view_v2(headers)
    #     try:
    #         for item in userdata_v2["data"]["rows"]:
    #             if item["cell_type"] == "18001":
    #                 print("发现额外签到奖励, 准备领取")
    #                 continue_checkin_reward_show = item["cell_data"]["checkin_continue"]["continue_checkin_reward_show"]
    #                 break
    #     except Exception as e:
    #         print("签到额外奖励未知错误")
    #     if not continue_checkin_reward_show:
    #         return
    #     url = "https://user-api.smzdm.com/checkin/extra_reward"
    #     resp = requests.post(url=url, headers=headers)

    # def show_view_v2(self, headers):
    #     url = "https://user-api.smzdm.com/checkin/show_view_v2"
    #     data = {
    #         'basic_v': '0',
    #         'f': 'iphone',
    #         'sign': '1668A9209483682BAC40177BCD2C462B',
    #         'time': '1714870850000',
    #         'v': '11.0.5',
    #         'weixin': '1',
    #         'zhuanzai_ab': 'a'
    #     }
    #     resp = requests.post(url=url, headers=headers, data=data)
    #     if resp.status_code == 200 and int(resp.json()["error_code"]) == 0:
    #         return resp.json()

    def main(self):
        headers = {
            "Host": "user-api.smzdm.com",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie": self.cookie,
            "User-Agent": "smzdm_android_V10.4.1 rv:841 (22021211RC;Android12;zh)smzdmapp",
        }
        msg = self.active()
        token = self.robot_token(headers)
        # 签到
        error_msg, data = self.sign(headers, token)
        msg.append({"name": "✅签到结果", "value": error_msg})
        # 奖励
        reward_msg = self.all_reward(headers, data)
        msg += reward_msg
        msg = "\n".join([f"{one.get('name')}: {one.get('value')}" for one in msg])

        # 额外签到奖励
        # userdata_v2 = self.show_view_v2(headers)
        # self.extra_reward(headers)

        # 推送消息
        send("什么值得买签到", msg)

        return msg


if __name__ == "__main__":
    env_name = 'SMZDM'
    SMZDM_COOKIE = os.getenv(env_name)
    if not SMZDM_COOKIE:
        print(f'⛔️未获取到ck变量：请检查变量 {env_name} 是否填写')
        exit(0)
    # 创建 SMZDM 实例并调用 main 方法
    print(SMZDM(SMZDM_COOKIE).main())
