import os
import time

import requests
import json

# 太平洋汽车
class TPYQCIO():
    name = "太平洋汽车抽奖"

    def __init__(self, cookie):
        self.cookie = cookie

    # 抽奖
    def lottery(self):
        msg = '开始抽奖......\n'
        # 设置请求的URL
        url = 'https://act1.pcauto.com.cn/discount/api/activity/lottery'
        # 设置请求头
        headers = {
            'Host': 'act1.pcauto.com.cn',
            'Accept': 'application/json, text/plain, */*',
            'Sec-Fetch-Site': 'same-site',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Mode': 'cors',
            'Content-Type': 'application/json',
            'Origin': 'https://www1.pcauto.com.cn',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Referer': 'https://www1.pcauto.com.cn/',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Cookie': self.cookie,
        }
        # 设置请求体（JSON格式）
        data = {
            'actId': '19',
            'phone': '1055239575'
        }
        # 发送POST请求
        response = requests.post(url, headers=headers, json=data)
        # 打印响应内容
        print(response.text)
        # 如果你需要响应的JSON内容，可以这样做：
        response_json = response.json()
        if response_json['code'] == 200 and response_json['data']['code'] == 0:
            msg = f'抽奖成功, {response_json["data"]["msg"]}{response_json["data"]["amount"]}元\n'
        elif response_json['code'] == 1:
            msg = f'抽奖失败, {response_json["data"]["msg"]}\n'

        return msg

    # 领取
    def receice(self):
        msg = '开始领取红包......\n'
        # ----------------------------------------
        url1 = 'https://act1.pcauto.com.cn/discount/api/series/list'
        headers = {
            'Host': 'act1.pcauto.com.cn',
            'Accept': 'application/json, text/plain, */*',
            'Sec-Fetch-Site': 'same-site',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Mode': 'cors',
            'Content-Type': 'application/json',
            'Origin': 'https://www1.pcauto.com.cn',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Referer': 'https://www1.pcauto.com.cn/',
            'Content-Length': '14',  # 注意：这个值通常由库自动处理，所以通常不需要手动设置
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty'
        }
        data1 = json.dumps({"actId": "19"})  # 将数据转换为JSON字符串
        response1 = requests.post(url1, headers=headers, data=data1)
        data2 = response1.json()  # 获取JSON数据
        # 获取第一个对象的字段信息
        first_item = data2['data'][0]  # 列表中的第一个元素
        brand_id = first_item['brandId']
        brand = first_item['brand']
        serial_group_id = first_item['serialGroupId']
        serial_group_name = first_item['serialGroupName']
        serial_group_pic = first_item['serialGroupPic']

        # 打印结果
        # print(f"brandId: {brand_id}")
        # print(f"brand: {brand}")
        # print(f"serialGroupId: {serial_group_id}")
        # print(f"serialGroupName: {serial_group_name}")
        # print(f"serialGroupPic: {serial_group_pic}")
        # ----------------------------------------
        # 设置请求头
        headers = {
            'Host': 'act1.pcauto.com.cn',
            'Accept': 'application/json, text/plain, */*',
            'Sec-Fetch-Site': 'same-site',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Mode': 'cors',
            'Content-Type': 'application/json',
            'Origin': 'https://www1.pcauto.com.cn',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Referer': 'https://www1.pcauto.com.cn/',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Cookie': 'pcsuv=1715211510009.a.33360290; channel=10927; common_session_id=%3A%2218f5a92964aa07-0270717f313bc4c-774c1151-329160-18f5a92964baf9%22%7D'
        }

        # 设置请求体（data）
        data = {
            "playRecordId": 104486,  # 104271
            "locationVersion": 1,
            "locationMessage": "",
            "phone": "1055239575",
            "pcsuv": 52792536,
            "actId": 19,
            "source": 2,
            "sourceDetail": 5,
            "currentFrom": "https://www1.pcauto.com.cn/zt/discount-topics/app-wap/index.html#/?actId=19&sourceDetail=5&isActivity=1&app_ver=7.1.2",
            "city": "上海",
            "seriesBOList": [
                {
                    "serialGroupPic": serial_group_pic,
                    "brand": brand,
                    "brandId": brand_id,
                    "serialGroupId": serial_group_id,
                    "serialGroupName": serial_group_name
                }
            ],
            "locationType": 4,
            "cityId": "3"
        }

        # 发送 POST 请求
        response = requests.post(
            'https://act1.pcauto.com.cn/discount/api/enroll/save',
            headers=headers,
            json=data  # 使用 json 参数来发送 JSON 格式的请求体
        )
        resp = response.json()
        if resp['code'] == 200 and resp['data']['code'] == 0:
            msg = f'领取成功\n'
        else:
            msg = f'领取失败, {resp["data"]["msg"]}\n'



        return msg

    def main(self):
        msg = ''
        # msg1 = self.lottery()
        # msg = msg + msg1
        # time.sleep(10)
        # msg2 = self.receice()
        # print("msg2=", msg2)
        time.sleep(13)
        # msg = msg + msg2
        self.cashOut()


        return  msg


    # 提现
    def cashOut(self):
        # 定义URL和请求头
        url = 'https://act1.pcauto.com.cn/discount/api/cash/out'
        headers = {
            'Host': 'act1.pcauto.com.cn',
            'Accept': 'application/json, text/plain, */*',
            'Sec-Fetch-Site': 'same-site',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Mode': 'cors',
            'Content-Type': 'application/json',
            'Origin': 'https://www1.pcauto.com.cn',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
            'Referer': 'https://www1.pcauto.com.cn/',
            'Connection': 'keep-alive',
            'Sec-Fetch-Dest': 'empty',
            'Cookie': 'channel=10444; pcsuv=1715211510009.a.33360290; pcuvdata=lastAccessTime=1715230577401|visits=2; common_session_id=E868681D114A85801EB4AC7ED63FB6549BD9D807FE76CEAA86FB059DF81C2CA9157E2E2BD6F4ADF8AE0C982DE164FF39; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218f5a92964aa07-0270717f313bc4c-774c1151-329160-18f5a92964baf9%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnTpdHlfY29va2llX2lkIjoiMThmNWE5Mjk2NGFhMDctMDI3MDcxN2YzMTNiYzRjLTc3NGMxMTUxLTMyOTE2MC0xOGY1YTkyOTY0YmFmOSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218f5a92964aa07-0270717f313bc4c-774c1151-329160-18f5a92964baf9%22%7D; sajssdk_2015_cross_new_user=1'
        }

        data = {
            'devId': '7d30da2005b532639b5f2cd3e335cfde79654bb1',
            'openId': 'oFOGvjhieYfIbabUXNZHLaZNsXRE',
            'amount': '0.3'
        }

        response = requests.post(url, headers=headers, json=data)
        response_json = response.json()

        if response_json['code'] != 200 or (response_json['code'] == 200 and response_json['data']['code'] != 0):
            print(f'❌提现失败：{response_json["msg"]}')
        else:
            print(f'✅提现成功：{response_json["data"]["msg"]}')

    # def getUserInfo(self):


if __name__ == '__main__':
    env_name = 'tpyqc_cookie'
    cookie = os.getenv(env_name)
    cookie = 'pcsuv=1715211510009.a.33360290; channel=10927; common_session_id=E868681D114A85801EB4AC7ED63FB6549BD9D807FE76CEAA86FB059DF81C2CA9157E2E2BD6F4ADF8AE0C982DE164FF39; pcuvdata=lastAccessTime=1715211507667; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218f5a92964aa07-0270717f313bc4c-774c1151-329160-18f5a92964baf9%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMThmNWE5Mjk2NGFhMDctMDI3MDcxN2YzMTNiYzRjLTc3NGMxMTUxLTMyOTE2MC0xOGY1YTkyOTY0YmFmOSJ9%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218f5a92964aa07-0270717f313bc4c-774c1151-329160-18f5a92964baf9%22%7D'
    if not cookie:
        print(f'⛔️未获取到ck变量：请检查变量 {env_name} 是否填写')
        exit(0)
    print(TPYQCIO(cookie).main())
