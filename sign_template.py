# import requests
#
# headers = {
#     'accept': 'application/json, text/plain, */*',
#     'accept-language': 'zh-CN',
#     'access-control-allow-credentials': 'true',
#     'authorization': 'Basic bW9iaWxlOjE3ODU0Mjc5NTY1OkU0RFREYngyfDF8UkNTfDE3MTc0ODI0OTIwOTB8RlJmdjBCZGQ4QVhUd0RrUmdfVHI1aHUwOFRQa0oxNGpNQjFaZm1pc1Q4enkyTWdrUzFIUFo4cU5kbzdJVkpJd3hpZmFJNmFyWUdyei5JNHdTOGh1SVNUcXk3QmpaMGZ4VGJKX1NySENJZEV6RlpMZzlkWFNGdzB4NzlWRHBBejBUZTBwbGc2eTBmZVh3c0NKMV9rSDdvMG9nVmY3WkEuOXhOWmw4YkFIUGFrLQ==',
#     'cms-client': '0010102',
#     'cms-device': 'default',
#     'content-type': 'application/json;charset=UTF-8',
#     'cookie': 'sajssdk_2015_cross_new_user=1; isUserDomainError=false; nation_code=+86; WT_FPC=id=2941aaefb0af23c1cef1714890191698:lv=1714890413164:ss=1714890191698; sds={"switch":0}; hecaiyun_stay_url=https%3A%2F%2Fyun.139.com%2Fm%2F%23%2Flogin; hecaiyun_stay_time=1714890455375; a_k=St2bzzj2P54Ze4E5; skey=TAFiNc3NQtSVYP/ej5KlzkfQZqcjF7WmfUJqHUsmNr5Kmk7LdmGI8wQ0Osu50814bPHdcB4s/rJrK8UowzDR3Qe0t7UIUvqiRsxWjQCZjSAJGjJEBbpWzSK4mvrLPk3GjLqA4LOCj+U0T1QLotRTDF9l5FtA4NRLT7JCR+YMHNg=; ud_id=1039929195747021143; ORCHES-I-ACCOUNT-SIMPLIFY=178****9565; hecaiyundata2021jssdkcross=%7B%22distinct_id%22%3A%2218f476bab27608-039a5f606e202ac-26001d51-1327104-18f476bab28549%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22phn%22%3A%22MTc4NTQyNzk1NjU%3D%22%2C%22phoneNumber%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218f476bab27608-039a5f606e202ac-26001d51-1327104-18f476bab28549%22%7D; ORCHES-I-ACCOUNT-ENCRYPT=MTc4NTQyNzk1NjU=; auth_token=E4DTDbx2|1|RCS|1717482492090|FRfv0Bdd8AXTwDkRg_Tr5hu08TPkJ14jMB1ZfmisT8zy2MgkS1HPZ8qNdo7IVJIwxifaI6arYGrz.I4wS8huISTqy7BjZ0fxTbJ_SrHCIdEzFZLg9dXSFw0x79VDpAz0Te0plg6y0feXwsCJ1_kH7o0ogVf7ZA.9xNZl8bAHPak-; token=Lg7wKbHyRVBJyC4G4qlm94h+0tOUORGLf5K/zK/v6K0AVV2OEwYWagIgDKlOfB0OqHGGO8BXTnSNUv9Oube8nc66W+aXunNE0qHx8VjOUO3Kc2TzkPpXs0CTfO6s8mpWhDNu92CPJXasXxuZlJ8uEyf/Pnnuy5HLoCZIrx+MEcYDmZxEXOx4dKfihAmGqJamjPK+Gpvpu4GbXwy8CDZ0D938OdaBTT1khxUzU+mxiNCzv85pfaRMLgB/5gdDEvCm2Kq68H/mW70s5xpU1C6Rfg==; NATION_CODE=86; LINK__account=LcbBKaMwlglFkcWtwv2WZA%3D%3D; LINK__accountForShow=178****9565; LINK__encryptedMobilePhone=LcbBKaMwlglFkcWtwv2WZA%3D%3D; LINK__outLinkAuthToken=PB5oIH9E3VBvfIJDi1hAQcSS2ucv/BHnrmVimj9RLBzNf3QnUMAatmvyytI5mcKlZgOopILBcw4hLUD7GDzBy8Zk8/McQuu+51+wF4lKgvlBCN6/WAZCPUxkT7P229cni90JuI4Cz/ZhLUtT/dNeWniQP8b30tXqQKfhravxZxjYlEJYfInk97yR9ImDw0q4KxrRR7qrAYjo/hxfO9s9yfME6TuhF10pSnlwORw5Sud/4FrXwCiJNU3bAzPA+5wQkk51R8PpHXI5mL/A/8sJhQ%3D%3D; logininfo=%7B%22account%22%3A%2217854279565%22%2C%22authToken%22%3A%22E4DTDbx2%7C1%7CRCS%7C1717482492090%7CFRfv0Bdd8AXTwDkRg_Tr5hu08TPkJ14jMB1ZfmisT8zy2MgkS1HPZ8qNdo7IVJIwxifaI6arYGrz.I4wS8huISTqy7BjZ0fxTbJ_SrHCIdEzFZLg9dXSFw0x79VDpAz0Te0plg6y0feXwsCJ1_kH7o0ogVf7ZA.9xNZl8bAHPak-%22%2C%22cutoverStatus%22%3A%22%22%2C%22userid%22%3A%221039929195747021143%22%7D; userInfo={"extMsg":{}}; authorization=Basic bW9iaWxlOjE3ODU0Mjc5NTY1OkU0RFREYngyfDF8UkNTfDE3MTc0ODI0OTIwOTB8RlJmdjBCZGQ4QVhUd0RrUmdfVHI1aHUwOFRQa0oxNGpNQjFaZm1pc1Q4enkyTWdrUzFIUFo4cU5kbzdJVkpJd3hpZmFJNmFyWUdyei5JNHdTOGh1SVNUcXk3QmpaMGZ4VGJKX1NySENJZEV6RlpMZzlkWFNGdzB4NzlWRHBBejBUZTBwbGc2eTBmZVh3c0NKMV9rSDdvMG9nVmY3WkEuOXhOWmw4YkFIUGFrLQ==; ORCHES-USER-ID=1J11olW8UMu7',
#     'inner-hcy-router-https': '1',
#     'mcloud-channel': '1000101',
#     'mcloud-client': '10601',
#     'mcloud-route': '001',
#     'mcloud-sign': '20240505142812,02eOtN2Q,9904453CA3E640CF5B2DD0A6587D8312',
#     'mcloud-version': '7.13.4',
#     'origin': 'https://yun.139.com',
#     'priority': 'u=1, i',
#     'referer': 'https://yun.139.com/m/',
#     'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
#     'sec-ch-ua-mobile': '?1',
#     'sec-ch-ua-platform': '"Android"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
#     'x-deviceinfo': '||3|7.13.4|Nexus 5|Nexus 5|m94dwPB1iU3lukWR6ujfJhA2nsjzc5Jj||Android 6.0|836X616|||',
#     'x-huawei-channelsrc': '10000035',
#     'x-inner-ntwk': '2',
#     'x-m4c-caller': 'h5',
#     'x-m4c-src': '10001',
#     'x-nationcode': '+86',
#     'x-svctype': '1',
#     'x-yun-api-version': 'v1',
#     'x-yun-app-channel': '10000035',
#     'x-yun-client-info': '||3|7.13.4|Nexus 5|Nexus 5|m94dwPB1iU3lukWR6ujfJhA2nsjzc5Jj||Android 6.0|836X616||||TmV4dXMgNQ==|',
#     'x-yun-svc-type': '1',
# }
#
# data = '{"commonAccountInfo":{"account":"17854279565","accountType":1}}'
#
# response = requests.post('https://yun.139.com/orchestration/thirdPart/extension/webExt/v1.0/query', headers=headers, data=data)
#
# print(response.json())
#
# # ------------------------------------------------------------
# # import requests
#
# headers = {
#     'accept': 'application/json, text/plain, */*',
#     'accept-language': 'zh-CN',
#     'access-control-allow-credentials': 'true',
#     'authorization': 'Basic bW9iaWxlOjE3ODU0Mjc5NTY1OkU0RFREYngyfDF8UkNTfDE3MTc0ODI0OTIwOTB8RlJmdjBCZGQ4QVhUd0RrUmdfVHI1aHUwOFRQa0oxNGpNQjFaZm1pc1Q4enkyTWdrUzFIUFo4cU5kbzdJVkpJd3hpZmFJNmFyWUdyei5JNHdTOGh1SVNUcXk3QmpaMGZ4VGJKX1NySENJZEV6RlpMZzlkWFNGdzB4NzlWRHBBejBUZTBwbGc2eTBmZVh3c0NKMV9rSDdvMG9nVmY3WkEuOXhOWmw4YkFIUGFrLQ==',
#     'caller': 'web',
#     'cms-client': '0010102',
#     'cms-device': 'default',
#     'content-type': 'application/json;charset=UTF-8',
#     'cookie': 'sajssdk_2015_cross_new_user=1; isUserDomainError=false; nation_code=+86; WT_FPC=id=2941aaefb0af23c1cef1714890191698:lv=1714890413164:ss=1714890191698; sds={"switch":0}; a_k=St2bzzj2P54Ze4E5; skey=TAFiNc3NQtSVYP/ej5KlzkfQZqcjF7WmfUJqHUsmNr5Kmk7LdmGI8wQ0Osu50814bPHdcB4s/rJrK8UowzDR3Qe0t7UIUvqiRsxWjQCZjSAJGjJEBbpWzSK4mvrLPk3GjLqA4LOCj+U0T1QLotRTDF9l5FtA4NRLT7JCR+YMHNg=; ud_id=1039929195747021143; ORCHES-I-ACCOUNT-SIMPLIFY=178****9565; hecaiyundata2021jssdkcross=%7B%22distinct_id%22%3A%2218f476bab27608-039a5f606e202ac-26001d51-1327104-18f476bab28549%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22phn%22%3A%22MTc4NTQyNzk1NjU%3D%22%2C%22phoneNumber%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218f476bab27608-039a5f606e202ac-26001d51-1327104-18f476bab28549%22%7D; ORCHES-I-ACCOUNT-ENCRYPT=MTc4NTQyNzk1NjU=; auth_token=E4DTDbx2|1|RCS|1717482492090|FRfv0Bdd8AXTwDkRg_Tr5hu08TPkJ14jMB1ZfmisT8zy2MgkS1HPZ8qNdo7IVJIwxifaI6arYGrz.I4wS8huISTqy7BjZ0fxTbJ_SrHCIdEzFZLg9dXSFw0x79VDpAz0Te0plg6y0feXwsCJ1_kH7o0ogVf7ZA.9xNZl8bAHPak-; token=Lg7wKbHyRVBJyC4G4qlm94h+0tOUORGLf5K/zK/v6K0AVV2OEwYWagIgDKlOfB0OqHGGO8BXTnSNUv9Oube8nc66W+aXunNE0qHx8VjOUO3Kc2TzkPpXs0CTfO6s8mpWhDNu92CPJXasXxuZlJ8uEyf/Pnnuy5HLoCZIrx+MEcYDmZxEXOx4dKfihAmGqJamjPK+Gpvpu4GbXwy8CDZ0D938OdaBTT1khxUzU+mxiNCzv85pfaRMLgB/5gdDEvCm2Kq68H/mW70s5xpU1C6Rfg==; NATION_CODE=86; LINK__account=LcbBKaMwlglFkcWtwv2WZA%3D%3D; LINK__accountForShow=178****9565; LINK__encryptedMobilePhone=LcbBKaMwlglFkcWtwv2WZA%3D%3D; LINK__outLinkAuthToken=PB5oIH9E3VBvfIJDi1hAQcSS2ucv/BHnrmVimj9RLBzNf3QnUMAatmvyytI5mcKlZgOopILBcw4hLUD7GDzBy8Zk8/McQuu+51+wF4lKgvlBCN6/WAZCPUxkT7P229cni90JuI4Cz/ZhLUtT/dNeWniQP8b30tXqQKfhravxZxjYlEJYfInk97yR9ImDw0q4KxrRR7qrAYjo/hxfO9s9yfME6TuhF10pSnlwORw5Sud/4FrXwCiJNU3bAzPA+5wQkk51R8PpHXI5mL/A/8sJhQ%3D%3D; logininfo=%7B%22account%22%3A%2217854279565%22%2C%22authToken%22%3A%22E4DTDbx2%7C1%7CRCS%7C1717482492090%7CFRfv0Bdd8AXTwDkRg_Tr5hu08TPkJ14jMB1ZfmisT8zy2MgkS1HPZ8qNdo7IVJIwxifaI6arYGrz.I4wS8huISTqy7BjZ0fxTbJ_SrHCIdEzFZLg9dXSFw0x79VDpAz0Te0plg6y0feXwsCJ1_kH7o0ogVf7ZA.9xNZl8bAHPak-%22%2C%22cutoverStatus%22%3A%22%22%2C%22userid%22%3A%221039929195747021143%22%7D; userInfo={"extMsg":{}}; authorization=Basic bW9iaWxlOjE3ODU0Mjc5NTY1OkU0RFREYngyfDF8UkNTfDE3MTc0ODI0OTIwOTB8RlJmdjBCZGQ4QVhUd0RrUmdfVHI1aHUwOFRQa0oxNGpNQjFaZm1pc1Q4enkyTWdrUzFIUFo4cU5kbzdJVkpJd3hpZmFJNmFyWUdyei5JNHdTOGh1SVNUcXk3QmpaMGZ4VGJKX1NySENJZEV6RlpMZzlkWFNGdzB4NzlWRHBBejBUZTBwbGc2eTBmZVh3c0NKMV9rSDdvMG9nVmY3WkEuOXhOWmw4YkFIUGFrLQ==; ORCHES-USER-ID=1J11olW8UMu7; hecaiyun_stay_url=https%3A%2F%2Fyun.139.com%2Fm%2F%23%2Fmain; hecaiyun_stay_time=1714890492508',
#     'inner-hcy-router-https': '1',
#     'mcloud-channel': '1000101',
#     'mcloud-client': '10601',
#     'mcloud-route': '001',
#     'mcloud-sign': '20240505142812,X0u08e3z,1711B467B4EC9E58DAC0EFE034FC5039',
#     'mcloud-version': '7.13.4',
#     'origin': 'https://yun.139.com',
#     'priority': 'u=1, i',
#     'referer': 'https://yun.139.com/m/',
#     'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
#     'sec-ch-ua-mobile': '?1',
#     'sec-ch-ua-platform': '"Android"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
#     'x-deviceinfo': '||3|7.13.4|Nexus 5|Nexus 5|m94dwPB1iU3lukWR6ujfJhA2nsjzc5Jj||Android 6.0|836X616|||',
#     'x-huawei-channelsrc': '10000035',
#     'x-inner-ntwk': '2',
#     'x-m4c-caller': 'h5',
#     'x-m4c-src': '10001',
#     'x-nationcode': '+86',
#     'x-svctype': '1',
#     'x-yun-api-version': 'v1',
#     'x-yun-app-channel': '10000035',
#     'x-yun-client-info': '||3|7.13.4|Nexus 5|Nexus 5|m94dwPB1iU3lukWR6ujfJhA2nsjzc5Jj||Android 6.0|836X616||||TmV4dXMgNQ==|',
#     'x-yun-svc-type': '1',
# }
#
# data = '{"account":"17854279565","toSourceId":"001005"}'
#
# response = requests.post('https://yun.139.com/orchestration/auth-rebuild/token/v1.0/querySpecToken', headers=headers, data=data)
#
# print(response.json())
#
#
#
#
import datetime

import requests


def gift_list():
    url = 'https://mall.longwisedata.com/api/product/v1/card/defs/40/detail'
    headers = {
        'Host': 'mall.longwisedata.com',
        'Sec-Fetch-Site': 'same-origin',
        'Accept-Encoding': 'gzip, deflate, br',
        'Cookie': '_xflow_session_id=session_id_f10e25ef-8e9e-435c-840a-fc264d7a23f5; _xflow_session_time=2024-05-05%2009:50:15; _xflow_traceid=traceid_241cf353-22a5-4e21-81ca-12baf4f88150; _xflow_is_first_day=true; _xflow_super_trace_id=super_trace_id_214f687a-3de7-4020-8629-1782e91789f7; _xflow_uid=uid_283c2261-47e2-4ee7-9bf3-abc1c2f394a6; _orgCustId=SzRESqTtcbS/FBrLpqzRcugpDNw9lIF6lZlZhHy1ltm5R9XYwcUwqham65tu3tSMaSj3PEejC2woXcgQEQXYbA==; za_ciid=AeLQbgEAAAAAAAAAAAFsYW5nemjpAdlilQAAAAAAAJnGQQEAAAAAAQEAAAAAAM+ROgEAAAAAAWxhbmd6aGleb29OVks1SEVLRGtNRU1IeGRuUFVIS3FQU2RU0QEAamF2YS51dGlsLkRhdOUBWk9xRo8BAAAAAdlilQAAAAAAAQIB6g4TAAAAAAAAAdlilQAAAAAAAekOEwAAAAAAAQIB6g4TAAAAAAABgkgAAW9vTlZLNUhFS0RrTUVNSHhkblBVSEtxUFNkVNEAAA==; za_itid=TEVqiV9ZnUxEgK5gEDqLKDyHg46E3gDBt63lCiroqo95qkVWpP9wgG5u1l6cV7aB58HeQhkGRTizVPkEOLIOkg==; _e=3',
        'Connection': 'keep-alive',
        'Sec-Fetch-Mode': 'cors',
        'Accept': 'application/json',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003127) NetType/4G Language/zh_CN miniProgram/wx1a2dd9470fae37c4',
        'Referer': 'https://mall.longwisedata.com/web/h5/thirdcard/detail/40',
        'Sec-Fetch-Dest': 'empty',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9'
    }

    response = requests.get(url, headers=headers).json()
    print("999999999999999999999999999999999999999", response["result"]["skus"])


def sign_account_info():
    message = ''
    url = 'https://aim.longwisedata.com/lwmarketing_user_api/selectPersonInfoOne?token=34311e63fc59d2dc13c05ac6d1eb67b8&timestamp=1714814957486&sig=189484bc910e3032cdd760621c366877'

    headers = {
        'Host': 'aim.longwisedata.com',
        'Sec-Fetch-Site': 'same-origin',
        'Cookie': 'acw_tc=3adc341b17149639626511657ea77c9832618aacbca265ae2f67d9cc2e; _orgCustId=ZXsqd0idDdwlbxWyDPhQaR0CrhQxbXfurBtHt5AK937zWIx6KDNrcUSCPuijrZIrCyd36T/SGUnFHtUlffsLwQ==; za_itid=MdI2mIxCwnsSd2KqUOJqERgpI5YgOwgCeLd7c78tSBVzeQ2AQlgCuOI/mIv+hCFAvogk50Hb053fWPhvqseFFQ==; _xflow_uid=uid_283c2261-47e2-4ee7-9bf3-abc1c2f394a6',
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
#
if __name__ == '__main__':
    gift_list()
    sign_account_info()
