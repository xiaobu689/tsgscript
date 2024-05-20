"""
随申行

路径：随申行APP
用途：签到、养宠物攒兜豆，兑换地铁优惠券
变量名：SSX_COOKIE
格式： 任意请求头抓 Authorization 值

定时设置：每天一次就行，时间随意
cron: 33 8 * * *
const $ = new Env("随申行");
"""
import os
import random
import time
import requests
from datetime import datetime
from sendNotify import send


class SSX():
    def __init__(self, cookie):
        parts = cookie.split('#')
        self.cookie = parts[0]
        self.uid = parts[1]


    def getUserInfo(self):
        url = 'https://api.shmaas.net/actbizgtw/v1/getUserInfo'
        headers = {
            'Host': 'api.shmaas.net',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 x-isapp=1&bundleId=cn.shmaas.maas',
            'X-Saic-App-Version': '1',
            'Referer': 'https://www.shmaas.cn/',
            'X-Saic-Channel': 'maas_car',
            'X-Saic-AppId': 'maas_car',
            'X-Saic-Device-Id': '633EB41D5EEC41B1BA90E94C0A37D1D6',
            'Origin': 'https://www.shmaas.cn',
            'Sec-Fetch-Dest': 'empty',
            'X-Saic-Platform': 'h5',
            'X-Saic-Finger': 'MBisvmnrb85whea41715658907341dp2',
            'X-Saic-ProductId': '5',
            'Content-Length': '43',
            'Sec-Fetch-Site': 'cross-site',
            'x-dyeing': 'sp200318',
            'Connection': 'keep-alive',
            'Authorization': self.cookie,
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Mode': 'cors'
        }
        data = f'{{"uid":"{self.uid}"}}'
        response = requests.post(url, headers=headers, data=data).json()
        if response['errCode'] == 0:
            msg = f'✅账号：{response["data"]["mobile"]}\n'
            # msg += f'✅兜豆：{response["data"]["score"]}\n'
        else:
            msg = f'❌获取账号信息失败， cookie可能失效：{response["errMsg"]}\n'
        msg += f'-----------------------------------\n'
        print(msg)

        return msg

    def receive(self):
        url = 'https://api.shmaas.net/cap/base/platform/receiveBubbleCredit'
        headers = {
            'Host': 'api.shmaas.net',
            'Cookie': 'acw_tc=ac11000117156639186525612e5c8544ba0ff273142a266caba983771d576b; aliyungf_tc=8b769837fece37828771663c3b9dc985365992f0a08432fc77d139d08076cfa2',
            'User-Agent': 'ios-shell-maas/2.00.40 (iPhone; iOS 16.6; Scale/3.00)',
            'X-Saic-App-Version': '2.00.40',
            'X-Saic-Req-Ts': '1715663973681.638916',
            'X-Saic-LocationTime': '1715663960499',
            'X-Saic-Real-App-Version': '2.00.40.27021',
            'X-Saic-Channel': 'maas',
            'X-Saic-AppId': 'maas_car',
            'X-Saic-Gps': '121.306507,31.136091',
            'X-Saic-Device-Id': '633EB41D5EEC41B1BA90E94C0A37D1D6',
            'X-Saic-OS-Name': 'ios',
            'X-Saic-User-Agent': 'timezone/GMT+8 platform/iOS platform_version/16.6 carrier_code/65535 carrier_name/-- device_name/iPhone device_id/633EB41D5EEC41B1BA90E94C0A37D1D6 app_name/passenger app_version/2.00.40',
            'X-Saic-Platform': 'IOS',
            'X-Saic-Finger': 'BDE67B52-1322-46DE-A266-F398CB580E1C',
            'X-Saic-ProductId': '5',
            'Content-Length': '144',
            'X-Saic-CityCode': '310100',
            'Connection': 'keep-alive',
            'X-Saic-Ds': 'db0cdc011b62592d',
            'uid': self.uid,
            'Authorization': self.cookie,
            'Accept-Language': 'zh-Hans-CN;q=1',
            'X-Saic-Req-Sn': 'DE26B71E-8F58-4081-AA0C-0AE435F21E02',
            'env': 'release',
            'X-Saic-Location-CityCode': '310100',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-Saic-LocationAccuracy': '30.221807'
        }
        bean = self.query_finsh_status()
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = {
            "greenCreditTime": current_time,
            "language": "zh-cn",
            "carBonTypeName": "任务",
            "uniqueId": f"任务_{bean}_{current_time}",
            "greenCredit": bean
        }
        # data = {
        #     "greenCreditTime": "2024-05-14 13:19:32",
        #     "language": "zh-cn",
        #     "carBonTypeName": "任务",
        #     "uniqueId": "任务_5_2024-05-14 13:19:32",
        #     "greenCredit": 5
        # }
        msg = f'-----------------------------------\n'
        response = requests.post(url, headers=headers, json=data).json()
        if response['errCode'] == 0:
            msg += f'✅领取成功！\n'
            print(msg)
        elif response['errCode'] == -2763132:
            msg += f'❌已经领取过了，请勿重复领取！\n'
            print(msg)
        else:
            msg += f'❌领取失败， cookie可能已失效：{response["errMsg"]}\n'
            print(msg)

        return msg

    def task_list(self):
        msg = ""
        url = 'https://api.shmaas.net/cap/app/queryLowCarbonHome'
        headers = {
            'Host': 'api.shmaas.net',
            'Cookie': 'acw_tc=ac11000117156639186525612e5c8544ba0ff273142a266caba983771d576b; aliyungf_tc=8b769837fece37828771663c3b9dc985365992f0a08432fc77d139d08076cfa2',
            'User-Agent': 'ios-shell-maas/2.00.40 (iPhone; iOS 16.6; Scale/3.00)',
            'X-Saic-App-Version': '2.00.40',
            'X-Saic-Req-Ts': '1715663961036.255859',
            'X-Saic-LocationTime': '1715663960499',
            'X-Saic-Real-App-Version': '2.00.40.27021',
            'X-Saic-Channel': 'maas',
            'X-Saic-AppId': 'maas_car',
            'X-Saic-Gps': '121.306507,31.136091',
            'X-Saic-Device-Id': '633EB41D5EEC41B1BA90E94C0A37D1D6',
            'X-Saic-OS-Name': 'ios',
            'X-Saic-User-Agent': 'timezone/GMT+8 platform/iOS platform_version/16.6 carrier_code/65535 carrier_name/-- device_name/iPhone device_id/633EB41D5EEC41B1BA90E94C0A37D1D6 app_name/passenger app_version/2.00.40',
            'X-Saic-Platform': 'IOS',
            'X-Saic-Finger': 'BDE67B52-1322-46DE-A266-F398CB580E1C',
            'X-Saic-ProductId': '5',
            'Content-Length': '20',
            'X-Saic-CityCode': '310100',
            'Connection': 'keep-alive',
            'X-Saic-Ds': 'db0cdc011b62592d',
            'uid': self.uid,
            'Authorization': self.cookie,
            'Accept-Language': 'zh-Hans-CN;q=1',
            'X-Saic-Req-Sn': '73304D35-EEDB-4940-8CAC-A7808CCFAE09',
            'env': 'release',
            'X-Saic-Location-CityCode': '310100',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-Saic-LocationAccuracy': '30.221807'
        }
        data = {"language": "zh-cn"}
        response = requests.post(url, headers=headers, json=data).json()
        if response['errCode'] == 0:
            for i in response['data']['userActivityMessages']:
                if "用户注册" in i["name"] or "用户实名" in i["name"] or "用户首单" in i["name"] or "打车出行" in i["name"]:
                    continue
                msg1 = f'✅{i["name"]}: {"已完成" if i["finishStatus"] == 1 else "未完成"}\n'
                print(msg1)
        else:
            msg = f'❌获取任务列表信息失败， cookie可能失效：{response["errMsg"]}'
            print(msg)

        # print(response.text)
        return msg

    def get_game_info(self):
        msg = ''
        url = 'https://api.shmaas.net/cap/base/credits/queryNowAdoptInfo'
        headers = {
            'Host': 'api.shmaas.net',
            'Cookie': 'acw_tc=ac11000117156639186525612e5c8544ba0ff273142a266caba983771d576b; aliyungf_tc=8b769837fece37828771663c3b9dc985365992f0a08432fc77d139d08076cfa2',
            # 没有cookie也不影响调用
            'User-Agent': 'ios-shell-maas/2.00.40 (iPhone; iOS 16.6; Scale/3.00)',
            'X-Saic-App-Version': '2.00.40',
            'X-Saic-Req-Ts': '1715663938665.126953',
            'X-Saic-LocationTime': '1715663918342',
            'X-Saic-Real-App-Version': '2.00.40.27021',
            'X-Saic-Channel': 'maas',
            'X-Saic-AppId': 'maas_car',
            'X-Saic-Gps': '121.306507,31.136091',
            'X-Saic-Device-Id': '633EB41D5EEC41B1BA90E94C0A37D1D6',
            'X-Saic-OS-Name': 'ios',
            'X-Saic-User-Agent': 'timezone/GMT+8 platform/iOS platform_version/16.6 carrier_code/65535 carrier_name/-- device_name/iPhone device_id/633EB41D5EEC41B1BA90E94C0A37D1D6 app_name/passenger app_version/2.00.40',
            'X-Saic-Platform': 'IOS',
            'X-Saic-Finger': 'BDE67B52-1322-46DE-A266-F398CB580E1C',
            'X-Saic-ProductId': '5',
            'Content-Length': '20',
            'X-Saic-CityCode': '310100',
            'Connection': 'keep-alive',
            'X-Saic-Ds': 'db0cdc011b62592d',
            'uid': self.uid,
            'Authorization': self.cookie,
            'Accept-Language': 'zh-Hans-CN;q=1',
            'X-Saic-Req-Sn': '03C73F9F-BDCD-4F4E-B27F-DC04D8A5994A',
            'env': 'release',
            'X-Saic-Location-CityCode': '310100',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-Saic-LocationAccuracy': '30.221807'
        }
        data = {"language": "zh-cn"}

        response = requests.post(url, headers=headers, json=data).json()
        msg = f'-----------------------------------\n'
        msg += f'✅领养物: 和平鸽\n'
        msg += f'✅当前等级：{response["data"]["feedUserGameNew"]["level"]}\n'
        msg += f'✅喂养进度：{response["data"]["feedUserGameNew"]["nowScore"]}/{response["data"]["feedUserGameNew"]["needScore"]}\n'
        print(msg)

        return msg

    def feed(self):
        msg = '✅开始喂养......\n'
        url = 'https://api.shmaas.net/cap/base/credits/v2/feedUserGame'
        headers = {
            'Host': 'api.shmaas.net',
            'Cookie': 'acw_tc=ac11000117156639186525612e5c8544ba0ff273142a266caba983771d576b; aliyungf_tc=8b769837fece37828771663c3b9dc985365992f0a08432fc77d139d08076cfa2',
            'User-Agent': 'ios-shell-maas/2.00.40 (iPhone; iOS 16.6; Scale/3.00)',
            'X-Saic-App-Version': '2.00.40',
            'X-Saic-Req-Ts': '1715663944108.955811',
            'X-Saic-LocationTime': '1715663918342',
            'X-Saic-Real-App-Version': '2.00.40.27021',
            'X-Saic-Channel': 'maas',
            'X-Saic-AppId': 'maas_car',
            'X-Saic-Gps': '121.306507,31.136091',
            'X-Saic-Device-Id': '633EB41D5EEC41B1BA90E94C0A37D1D6',
            'X-Saic-OS-Name': 'ios',
            'X-Saic-User-Agent': 'timezone/GMT+8 platform/iOS platform_version/16.6 carrier_code/65535 carrier_name/-- device_name/iPhone device_id/633EB41D5EEC41B1BA90E94C0A37D1D6 app_name/passenger app_version/2.00.40',
            'X-Saic-Platform': 'IOS',
            'X-Saic-Finger': 'BDE67B52-1322-46DE-A266-F398CB580E1C',
            'X-Saic-ProductId': '5',
            'Content-Length': '33',
            'X-Saic-CityCode': '310100',
            'Connection': 'keep-alive',
            'X-Saic-Ds': 'db0cdc011b62592d',
            'uid': self.uid,
            'Authorization': self.cookie,
            'Accept-Language': 'zh-Hans-CN;q=1',
            'X-Saic-Req-Sn': 'DB26401E-B0A1-4D1A-9F88-058D591F6BCE',
            'env': 'release',
            'X-Saic-Location-CityCode': '310100',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'X-Saic-LocationAccuracy': '30.221807'
        }
        data = {
            'language': 'zh-cn',
            'gameId': 998
        }
        response = requests.post(url, headers=headers, json=data).json()
        msg = f'-----------------------------------\n'
        if response['errCode'] == 0:
            msg += f'✅喂养成功，更新等级进度：{response["data"]["feedUserGameNew"]["nowScore"]}/{response["data"]["feedUserGameNew"]["needScore"]}\n'
        elif response['errCode'] == -2763250:
            msg += f'✅今天已经喂养过了，明天再来吧!\n'
        else:
            msg += f'❌喂养失败，{response["errMsg"]}\n'
        print(msg)

        return msg

    def query_address(self):
        msg = ''
        url = 'https://dualstack-restios.amap.com/v5/place/text'
        headers = {
            'Host': 'dualstack-restios.amap.com',
            'Accept': '*/*',
            'platinfo': 'platform=iOS&product=sea&sdkversion=9.7.0&founversion=1.8.2',
            'x-info': 't34+94jruh/r2BCfvOVOAdT/3hBBx5N7L2rs2wkhydqjoBoMlswtRSzEnP4GoLbT1Pb8820nK8KarglxuCo0RYIQ6/W6+rsH5iJe6Qr3E+jwqcYJDRRhP2uhUUrEKSc0UTaCX5J8CricuFCAcVl+8vqP7xkEJObHQqeNqYd7d1INtIxMjY0YDRkNWP1LMlKLGA0YBCwtrCzNrZKTrYwtrEytjE0ZGDgMgPpAAM5gkMPvWpvM3MRk25qkzBTb5Dy94ozcxMRiPRBRU1ySX5SYnmpraGRoaWxYU5SYa2tqZmlak1iUnGHrGORrZuIKAGfGhIoKAQAA',
            'logversion': '2.1',
            'Accept-Encoding': 'gzip,deflate',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'AMAP_SDK_iOS_Search_9.7.0',
            'Connection': 'keep-alive',
            'csid': '6C593DEE-6628-4EFB-999E-010569620BBB'
        }
        data = {
            'location': '121.306507,31.136091',
            'page_num': '1',
            'region': '上海市',
            'output': 'json',
            'keywords': '闵浦新苑二村',
            'city_limit': 'false',
            'sortrule': 'weight',
            'language': 'zh',
            'key': 'c358c360816bf9feebd70e46b52f3937',
            'show_fields': 'children,business,indoor,navi,photos',
            'page_size': '15',
            'scode': '55c5e446c409007de1e89b8c84342db0',
            'ts': '1715663958518'
        }

        response = requests.post(url, headers=headers, data=data).json()

    def finish_query_address(self):
        headers = {
            'Host': 'api.shmaas.net',
            'User-Agent': 'ios-shell-maas/2.00.40 (iPhone; iOS 16.6; Scale/3.00)',
            'X-Saic-App-Version': '2.00.40',
            'X-Saic-Req-Ts': '1715867520961.298828',
            'X-Saic-LocationTime': '1715867440458',
            'X-Saic-Real-App-Version': '2.00.40.27021',
            'X-Saic-Channel': 'maas',
            'X-Saic-AppId': 'maas_car',
            'X-Saic-Gps': '121.529377,31.058028',
            'X-Saic-Device-Id': '633EB41D5EEC41B1BA90E94C0A37D1D6',
            'X-Saic-OS-Name': 'ios',
            'X-Saic-User-Agent': 'timezone/GMT+8 platform/iOS platform_version/16.6 carrier_code/65535 carrier_name/-- device_name/iPhone device_id/633EB41D5EEC41B1BA90E94C0A37D1D6 app_name/passenger app_version/2.00.40',
            'X-Saic-Platform': 'IOS',
            'X-Saic-Finger': '201D55AB-F776-4F83-B851-93CAD4A89E56',
            'X-Saic-ProductId': '5',
            # 'Content-Length': '38',
            'X-Saic-CityCode': '310100',
            'Connection': 'keep-alive',
            'X-Saic-Ds': 'db0cdc011b62592d',
            'uid': self.uid,
            'Authorization': self.cookie,
            'Accept-Language': 'zh-Hans-CN;q=1',
            'X-Saic-Req-Sn': 'A3485813-214F-468F-8FFC-BEFCED2C5D20',
            'env': 'release',
            'X-Saic-Location-CityCode': '310100',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Saic-LocationAccuracy': '35.000000',
        }

        json_data = {
            'language': 'zh-cn',
            'behaviorType': 10,
        }

        url = 'https://api.shmaas.net/actbizgtw/v1/reportUserBehavior'
        response = requests.post(url, headers=headers, json=json_data).json()

        if response['errCode'] == 0:
            msg = f'✅联程规划完成，兜豆：+{response["data"]["rewardValue"]}\n'
        else:
            msg = f'❌联程规划未完成，{response["errMsg"]}\n'

        return msg

    def sign(self):
        headers = {
            'Host': 'api.shmaas.net',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 x-isapp=1&bundleId=cn.shmaas.maas',
            'X-Saic-App-Version': '1',
            'Referer': 'https://www.shmaas.cn/',
            'X-Saic-Channel': 'maas_car',
            'X-Saic-AppId': 'maas_car',
            'X-Saic-Device-Id': '633EB41D5EEC41B1BA90E94C0A37D1D6',
            'Origin': 'https://www.shmaas.cn',
            'Sec-Fetch-Dest': 'empty',
            'X-Saic-Platform': 'h5',
            'X-Saic-Finger': 'MB9mywnmgpbxiyvl17158698778494g4',
            'X-Saic-ProductId': '5',
            'Sec-Fetch-Site': 'cross-site',
            'x-dyeing': 'sp200318',
            'Connection': 'keep-alive',
            'Authorization': self.cookie,
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Mode': 'cors',
        }

        json_data = {
            'uid': self.uid,
            'activityId': '55ShoppingFestival',
            'taskType': 1,
        }
        url = 'https://api.shmaas.net/actbizgtw/v1/completeActivityTask'
        response = requests.post(url, headers=headers, json=json_data).json()
        print("-----------------response=", response)
        if response['errCode'] == 0:
            msg = f'✅签到成功，抽奖次数：+1\n'
            print(msg)
        else:
            msg = f'❌签到失败，{response["errMsg"]}\n'
            print(msg)

        return msg

    # 抽奖
    def lottery(self):
        url = 'https://api.shmaas.net/actbizgtw/v1/openActivityUserLuckBag'
        headers = {
            'Host': 'api.shmaas.net',
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x1800312b) NetType/WIFI Language/zh_CN miniProgram/wxac5a35f99768c9c2',
            'X-Saic-App-Version': '1',
            'Referer': 'https://www.shmaas.cn/',
            'X-Saic-Channel': 'maas_car',
            'X-Saic-AppId': 'maas_car',
            'X-Saic-Device-Id': '16941',
            'Origin': 'https://www.shmaas.cn',
            'Sec-Fetch-Dest': 'empty',
            'X-Saic-Platform': 'h5',
            'X-Saic-Finger': 'MBo9z9343op0ou4217156612811632qe',
            'X-Saic-ProductId': '5',
            'Content-Length': '77',
            'Sec-Fetch-Site': 'cross-site',
            'x-dyeing': 'sp200318',
            'Connection': 'keep-alive',
            'Authorization': self.cookie,
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Accept-Encoding': 'gzip, deflate, br',
            'Sec-Fetch-Mode': 'cors'
        }
        data = f'{{"uid":"{self.uid}","activityId":"55ShoppingFestival"}}'
        response = requests.post(url, headers=headers, data=data).json()
        msg = f'-----------------------------------\n'
        if response['errCode'] == 0:
            msg = f'✅抽奖成功，获得：{response["data"]["userLuckBagViewInfo"][0]["awardName"]}\n'
        elif response['errCode'] == -1961003:
            msg += f'❌抽奖失败，没有抽奖次数了!\n'
        else:
            msg += f'❌抽奖失败, cookie可能已失效！， {response["errMsg"]}\n'
        print(msg)

        return msg

    def query_finsh_status(self):
        headers = {
            'Host': 'api.shmaas.net',
            # 'Cookie': 'acw_tc=ac11000117159144480791268eaec93bb642cf1f070947519672f7869ed165; aliyungf_tc=e50803547e715566685370e042ad35c42818a4c7128a98e0af259d8d183b5490; mtr-mdap=628d1480-802c-4753-b487-9f4387c151bb; mtr-userid=VISITOR',
            'User-Agent': 'ios-shell-maas/2.00.40 (iPhone; iOS 16.6; Scale/3.00)',
            'X-Saic-App-Version': '2.00.40',
            'X-Saic-Req-Ts': '1715914466424.373047',
            'X-Saic-LocationTime': '1715914447506',
            'X-Saic-Real-App-Version': '2.00.40.27021',
            'X-Saic-Channel': 'maas',
            'X-Saic-AppId': 'maas_car',
            'X-Saic-Gps': '121.306501,31.136084',
            'X-Saic-Device-Id': '633EB41D5EEC41B1BA90E94C0A37D1D6',
            'X-Saic-OS-Name': 'ios',
            'X-Saic-User-Agent': 'timezone/GMT+8 platform/iOS platform_version/16.6 carrier_code/65535 carrier_name/-- device_name/iPhone device_id/633EB41D5EEC41B1BA90E94C0A37D1D6 app_name/passenger app_version/2.00.40',
            'X-Saic-Platform': 'IOS',
            'X-Saic-Finger': 'B9E7857C-512B-4E46-BBED-E596A1C795BA',
            'X-Saic-ProductId': '5',
            # 'Content-Length': '20',
            'X-Saic-CityCode': '310100',
            'Connection': 'keep-alive',
            'X-Saic-Ds': 'db0cdc011b62592d',
            'uid': self.uid,
            'Authorization': self.cookie,
            'Accept-Language': 'zh-Hans-CN;q=1',
            'X-Saic-Req-Sn': 'C9A66E54-6083-4DA3-8C58-023FFFE27507',
            'env': 'release',
            'X-Saic-Location-CityCode': '310100',
            'Accept': '*/*',
            'Content-Type': 'application/json',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'X-Saic-LocationAccuracy': '28.536021',
        }

        json_data = {
            'language': 'zh-cn',
        }

        url = 'https://api.shmaas.net/cap/app/queryLowCarbonHome'
        response = requests.post(url, headers=headers, json=json_data).json()
        bean = 0
        # 0：未完成 1：已完成
        if response['errCode'] == 0:
            for i in response['data']['userActivityMessages']:
                if "用户注册" in i["name"] or "用户实名" in i["name"] or "用户首单" in i["name"] or "打车出行" in i["name"]:
                    continue
                if i["finishStatus"] == 1:
                    bean += i["rewardValue"]
        else:
            msg = f'❌获取任务列表信息失败， cookie可能失效：{response["errMsg"]}'
            print(msg)

        return bean


    def main(self):
        title = "随申行"
        msg1 = self.getUserInfo()
        time.sleep(random.randint(8, 15))

        msg2 = self.task_list()
        msg3 = self.get_game_info()
        time.sleep(random.randint(7, 15))

        msg4 = self.feed()
        time.sleep(random.randint(10, 20))

        self.query_address()
        msg5 = self.finish_query_address()
        time.sleep(random.randint(5, 10))

        msg6 = self.sign()
        time.sleep(random.randint(5, 15))
        msg7 = self.lottery()
        time.sleep(random.randint(5, 15))

        msg8 = self.receive()

        msg = msg1 + msg2 + msg3 + msg4 + msg5 + msg6 + msg7 + msg8

        # 通知
        send(title, msg)


if __name__ == '__main__':
    env_name = 'SSX_COOKIE'
    cookie = os.getenv(env_name)
    if not cookie:
        print(f'⛔️未获取到ck变量：请检查变量 {env_name} 是否填写')
        exit(0)

    SSX(cookie).main()
