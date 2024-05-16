"""
随申行

APP：随申行
用途：兑换地铁优惠券，上海坐地铁使用
变量名：ssx_token
格式： 任意请求头抓 Authorization 值
定时设置：
cron: 25 9 * * *
const $ = new Env("随申行");
"""
import requests


class SuiShenXing():
    def __init__(self, cookie):
        self.cookie = cookie

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
        data = '{"uid":"Cb18437dc7f6b45c1819c25d98bf8a4fc"}'
        response = requests.post(url, headers=headers, data=data).json()
        if response['errCode'] == 0:
            msg = f'✅账号：{response["data"]["mobile"]}\n'
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
            'uid': 'Cb18437dc7f6b45c1819c25d98bf8a4fc',
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
        data = {
            "greenCreditTime": "2024-05-14 13:19:32",
            "language": "zh-cn",
            "carBonTypeName": "任务",
            "uniqueId": "任务_5_2024-05-14 13:19:32",
            "greenCredit": 5
        }
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
            'uid': 'Cb18437dc7f6b45c1819c25d98bf8a4fc',
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
        # print(response)
        if response['errCode'] == 0:
            for i in response['data']['userActivityMessages']:
                msg1 = f'✅{i["name"]}: {"已完成" if i["finishStatus"] == 1 else "未完成"}\n'
                print(msg1)
        else:
            msg = f'❌获取任务列表信息失败， cookie可能失效：{response["errMsg"]}'
            print(msg)

        # print(response.text)

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
            'uid': 'Cb18437dc7f6b45c1819c25d98bf8a4fc',
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
            'uid': 'Cb18437dc7f6b45c1819c25d98bf8a4fc',
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
            msg += f'✅喂养失败，今天已经喂养过了，明天再来吧!\n'
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
        data = '{"uid":"Cb18437dc7f6b45c1819c25d98bf8a4fc","activityId":"55ShoppingFestival"}'
        response = requests.post(url, headers=headers, data=data).json()
        msg = f'-----------------------------------\n'
        if response['errCode'] == 0:
            msg = f'✅抽奖成功，获得：{response["data"]["userLuckBagViewInfo"][0]["awardName"]}\n'
        elif response['errCode'] == -1961003:
            msg += f'❌抽奖失败，没有抽奖次数了!\n'
        else:
            msg += f'❌抽奖失败, cookie可能已失效！， {response["errMsg"]}\n'
        print(msg)

    def main(self):
        title = "随申行"
        msg1 = self.getUserInfo()
        msg2 = self.task_list()
        self.get_game_info()
        # self.feed()
        # self.query_address()
        # self.receive()
        # self.lottery()

        # 通知
        send(title, msg)



if __name__ == '__main__':
    cookie = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ1aWQiOiJDYjE4NDM3ZGM3ZjZiNDVjMTgxOWMyNWQ5OGJmOGE0ZmMiLCJkZXZpY2VJZCI6IjYzM0VCNDFENUVFQzQxQjFCQTkwRTk0QzBBMzdEMUQ2IiwiZXhwaXJlSW4iOjE3MzEwMjg4Nzg3NDcsImNyZWF0ZVRpbWUiOjE3MTU0NzY4Nzg3NDcsInBsYXRmb3JtQ29kZSI6ImlvcyIsImFwcElkIjoibWFhc19jYXIiLCJjaGFubmVsQ29kZSI6Im1hYXMiLCJhY2NvdW50TmFtZSI6IjE3OCoqKio5NTY1IiwiYWNjb3VudFR5cGUiOiIxIiwicHJvZHVjdElkIjo1LCJvcGVuSWQiOiIiLCJlayI6IiIsImNsaWVudElkIjoiMTUwMTQ4OTYxNjcwMzA3MDIwOCIsInVpZFR5cGUiOjEsInRhZyI6Mn0.LG5oHBgdxQul7YgrJHOyf7FLlIQ39R_hLmz_TGaUfKHyhIy2FOgLluQ5KD17gwBg_QqdlIstxr3Gjioye3D1kk8ZfuedOiojaiM-531VbfhwsEdlPeKL4Y0flUswYWgukjgQ0l-dXLBLV6FG8ytywYC3bBhUS3_J3RGmZctFvyk'
    SuiShenXing(cookie).main()
