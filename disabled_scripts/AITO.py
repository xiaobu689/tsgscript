"""
华为AITO
定时设置：
cron: 40 6 * * *
const $ = new Env("华为AITO");
"""
import datetime
import os

import requests
# from sign.notify import notify_pushPlus


class AITO:
    def __init__(self, cookie):
        self.cookie = cookie

    def sign_account_info(self):
        message = ''
        url = 'https://aim.longwisedata.com/lwmarketing_user_api/selectPersonInfoOne?token=34311e63fc59d2dc13c05ac6d1eb67b8&timestamp=1714814957486&sig=189484bc910e3032cdd760621c366877'

        headers = {
            'Host': 'aim.longwisedata.com',
            'Sec-Fetch-Site': 'same-origin',
            'Cookie': self.cookie,
            'Connection': 'keep-alive',
            'Sec-Fetch-Mode': 'cors',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003127) NetType/WIFI Language/zh_CN',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Encoding': 'gzip, deflate, br'
        }

        response = requests.get(url, headers=headers)
        print(response.text)
        data = response.json()
        if data.get('result') == '0':
            integral = data.get('data').get('integral')
            message += f"✅帐号：{data.get('data').get('nick')}\n"
            message += f"✅积分：{data.get('data').get('integral')}\n"
        else:
            message += f"❌帐号：{data.get('data').get('nick')}获取失败，可能cookie失效！\n"
            print(message)

        return message, data.get('data').get('integral')

    # 京东礼品卡列表
    def gift_list(self):
        url = 'https://mall.longwisedata.com/api/product/v1/card/defs/40/detail'
        headers = {
            'Host': 'mall.longwisedata.com',
            'Sec-Fetch-Site': 'same-origin',
            'Accept-Encoding': 'gzip, deflate, br',
            'Cookie': self.cookie,
            'Connection': 'keep-alive',
            'Sec-Fetch-Mode': 'cors',
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003127) NetType/4G Language/zh_CN miniProgram/wx1a2dd9470fae37c4',
            'Referer': 'https://mall.longwisedata.com/web/h5/thirdcard/detail/40',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9'
        }

        response = requests.get(url, headers=headers).json()
        # print(response)
        return response["result"]["skus"]

    # 签到
    def sign_in(self):
        message = ""
        # 签到
        url = 'https://aim.longwisedata.com/lwmarketing_user_api/taskSquare/signIn/signIn'

        headers = {
            'Host': 'aim.longwisedata.com',
            'Accept': 'application/json, text/plain, */*',
            'Sec-Fetch-Site': 'same-origin',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Sec-Fetch-Mode': 'cors',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://aim.longwisedata.com',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003127) NetType/4G Language/zh_CN',
            'Connection': 'keep-alive',
            'Cookie': self.cookie,
            'Sec-Fetch-Dest': 'empty'
        }

        data = {
            'token': '34311e63fc59d2dc13c05ac6d1eb67b8',
            'timestamp': '1714814957486',
            'sig': '189484bc910e3032cdd760621c366877'
        }

        response = requests.post(url, headers=headers, data=data)
        data = response.json()
        print(response.text)
        if data.get('result') == '200' or data.get('result') == '0':
            message += "✅签到结果：签到成功，"
            print(message)
        else:
            message = "❌签到结果：签到失败"
            print(message)

        return message

    def sign_task_list(self):
        url = 'https://aim.longwisedata.com/lwmarketing_user_api/taskList?token=34311e63fc59d2dc13c05ac6d1eb67b8&timestamp=1714814957486&sig=189484bc910e3032cdd760621c366877&pageNum=1&pageSize=10'

        headers = {
            'Host': 'aim.longwisedata.com',
            'Sec-Fetch-Site': 'same-origin',
            'Cookie': self.cookie,
            'Connection': 'keep-alive',
            'Sec-Fetch-Mode': 'cors',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003127) NetType/WIFI Language/zh_CN',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Encoding': 'gzip, deflate, br'
        }

        response = requests.get(url, headers=headers)
        # print(response.text)
        data = response.json()
        if data.get('result') == '0':
            task_list = data.get('list', [])
            print("Task List:", task_list)
            for task in task_list:
                print("Task=", task)
                if task.get('task_subtype') == 0:
                    task_id = task.get('task_id')
                    task_type = task.get('task_type')
                    article_title = task.get('name')
                    article_url = task.get('article_url')
                    print("Article Title:", article_title)
                    print("Article URL:", article_url)
                    # 领取任务
                    # 签到
                    url = 'https://aim.longwisedata.com/lwmarketing_user_api/taskForward/receiveTask'

                    headers = {
                        'Host': 'aim.longwisedata.com',
                        'Accept': 'application/json, text/plain, */*',
                        'Sec-Fetch-Site': 'same-origin',
                        'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
                        'Sec-Fetch-Mode': 'cors',
                        'Content-Type': 'application/x-www-form-urlencoded',
                        'Origin': 'https://aim.longwisedata.com',
                        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003127) NetType/4G Language/zh_CN',
                        'Connection': 'keep-alive',
                        'Cookie': self.cookie,
                        'Sec-Fetch-Dest': 'empty'
                    }

                    data = {
                        'token': '34311e63fc59d2dc13c05ac6d1eb67b8',
                        'timestamp': '1714814957486',
                        'sig': '189484bc910e3032cdd760621c366877',
                        'taskId': task_id,
                        'taskType': task_type
                    }

                    response = requests.post(url, headers=headers, data=data)
                    print("任务领取成功：", response.text)
        else:
            print("Failed to get task list.")  # {"result":"0","msg":"success"}

    def sign_my_tasklist(self):
        url = 'https://aim.longwisedata.com/lwmarketing_user_api/myTaskList?token=431d27a0ddb0aa1959c40af487aa4da9&timestamp=1714828633254&sig=fe0ca62a0b3ae9f4dce0e224fa3a257f&pageNum=1&pageSize=10&type=2'
        headers = {
            'Host': 'aim.longwisedata.com',
            'Sec-Fetch-Site': 'same-origin',
            'Cookie': self.cookie,
            'Connection': 'keep-alive',
            'Sec-Fetch-Mode': 'cors',
            'Accept': 'application/json, text/plain, */*',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003127) NetType/WIFI Language/zh_CN',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Sec-Fetch-Dest': 'empty',
            'Accept-Encoding': 'gzip, deflate, br'
        }

        response = requests.get(url, headers=headers)
        data = response.json()
        # print(response.text)
        if data.get('result') == '0':
            task_list = data.get('list', [])
            # print("Task List:", task_list)
            for task in task_list:
                if task.get('task_subtype') == 0 and task.get('browse_reward') > 0:
                    end_time = datetime.datetime.strptime(task.get('end_time'), '%Y-%m-%d %H:%M:%S')
                    # print("------------------测试打印结束时间=", end_time)
                    # 获取当前时间
                    current_time = datetime.datetime.now()
                    # 判断是否 end_time 小于当前时间
                    if end_time >= current_time:
                        print("task=", task)
                        task_id = task.get('task_id')
                        task_type = task.get('task_type')
                        article_title = task.get('name')
                        article_url = task.get('article_url')
                        real_url = task.get('real_url')
                        print(f'Task ID:', task_id)
                        print("real_url:", real_url)
                        print("article_url:", article_url)
                        print("article_title:", article_title)
                        print("------------------------------")

    def main(self):
        title = "AIOT之声签到"
        push_msg = ''
        msg1, integral1 = self.sign_account_info()
        if "失败" in msg1:
            print("账号信息获取失败，请检查cookie是否正确")
            return
        # else:
        #     msg2 = self.sign_in()
        #     # 积分进度
        #     msg3, integral3 = self.sign_account_info()
        #     diff_integra=  integral3 - integral1
        #     _msg = f'积分 + {diff_integra}'
        #     push_msg += msg1 + msg2 + msg3 + _msg
        #     result = self.gift_list()
        #     first_gift_price = result["result"]["skus"][0]["price"]
        #     tmp_msg = ''
        #     if integral3 >= first_gift_price:
        #         tmp_msg = f"已达标，可前往兑换奖品！\n"
        #     else:
        #         tmp_msg = f'{integral3}/{first_gift_price}'
        #     push_msg += f'✅{first_gift_price}进度: {tmp_msg}\n'
        #     push_msg += f'✅{first_gift_price}库存: {result["result"]["skus"][0]["stock"]}'

            # 推送
            # notify_pushPlus(title, push_msg)

        # 获取活动广场任务列表
        # self.sign_task_list()
        # 获取我的转发任务列表【带转发奖励的】
        # self.sign_my_tasklist()


if __name__ == '__main__':
    env_name = 'AITO_COOKIE'
    AITO_COOKIE = os.getenv(env_name)
    AITO_COOKIE = 'acw_tc=2760774d17155292543476252e9b1a62e32359fcf2d299db8b47a1e4b05f9e'
    if not AITO_COOKIE:
        print(f'⛔️未获取到ck变量：请检查变量 {env_name} 是否填写')
        exit(0)
    # 创建 AITO 实例并调用 main 方法
    print(AITO(AITO_COOKIE).main())
