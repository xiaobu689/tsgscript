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


# def gift_list():
#     url = 'https://mall.longwisedata.com/api/product/v1/card/defs/40/detail'
#     headers = {
#         'Host': 'mall.longwisedata.com',
#         'Sec-Fetch-Site': 'same-origin',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'Cookie': '_xflow_session_id=session_id_f10e25ef-8e9e-435c-840a-fc264d7a23f5; _xflow_session_time=2024-05-05%2009:50:15; _xflow_traceid=traceid_241cf353-22a5-4e21-81ca-12baf4f88150; _xflow_is_first_day=true; _xflow_super_trace_id=super_trace_id_214f687a-3de7-4020-8629-1782e91789f7; _xflow_uid=uid_283c2261-47e2-4ee7-9bf3-abc1c2f394a6; _orgCustId=SzRESqTtcbS/FBrLpqzRcugpDNw9lIF6lZlZhHy1ltm5R9XYwcUwqham65tu3tSMaSj3PEejC2woXcgQEQXYbA==; za_ciid=AeLQbgEAAAAAAAAAAAFsYW5nemjpAdlilQAAAAAAAJnGQQEAAAAAAQEAAAAAAM+ROgEAAAAAAWxhbmd6aGleb29OVks1SEVLRGtNRU1IeGRuUFVIS3FQU2RU0QEAamF2YS51dGlsLkRhdOUBWk9xRo8BAAAAAdlilQAAAAAAAQIB6g4TAAAAAAAAAdlilQAAAAAAAekOEwAAAAAAAQIB6g4TAAAAAAABgkgAAW9vTlZLNUhFS0RrTUVNSHhkblBVSEtxUFNkVNEAAA==; za_itid=TEVqiV9ZnUxEgK5gEDqLKDyHg46E3gDBt63lCiroqo95qkVWpP9wgG5u1l6cV7aB58HeQhkGRTizVPkEOLIOkg==; _e=3',
#         'Connection': 'keep-alive',
#         'Sec-Fetch-Mode': 'cors',
#         'Accept': 'application/json',
#         'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003127) NetType/4G Language/zh_CN miniProgram/wx1a2dd9470fae37c4',
#         'Referer': 'https://mall.longwisedata.com/web/h5/thirdcard/detail/40',
#         'Sec-Fetch-Dest': 'empty',
#         'Accept-Language': 'zh-CN,zh-Hans;q=0.9'
#     }
#
#     response = requests.get(url, headers=headers).json()
#     print("999999999999999999999999999999999999999", response["result"]["skus"])


# def sign_account_info():
#     message = ''
#     url = 'https://aim.longwisedata.com/lwmarketing_user_api/selectPersonInfoOne?token=34311e63fc59d2dc13c05ac6d1eb67b8&timestamp=1714814957486&sig=189484bc910e3032cdd760621c366877'
#
#     headers = {
#         'Host': 'aim.longwisedata.com',
#         'Sec-Fetch-Site': 'same-origin',
#         'Cookie': 'acw_tc=3adc341b17149639626511657ea77c9832618aacbca265ae2f67d9cc2e; _orgCustId=ZXsqd0idDdwlbxWyDPhQaR0CrhQxbXfurBtHt5AK937zWIx6KDNrcUSCPuijrZIrCyd36T/SGUnFHtUlffsLwQ==; za_itid=MdI2mIxCwnsSd2KqUOJqERgpI5YgOwgCeLd7c78tSBVzeQ2AQlgCuOI/mIv+hCFAvogk50Hb053fWPhvqseFFQ==; _xflow_uid=uid_283c2261-47e2-4ee7-9bf3-abc1c2f394a6',
#         'Connection': 'keep-alive',
#         'Sec-Fetch-Mode': 'cors',
#         'Accept': 'application/json, text/plain, */*',
#         'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003127) NetType/WIFI Language/zh_CN',
#         'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
#         'Sec-Fetch-Dest': 'empty',
#         'Accept-Encoding': 'gzip, deflate, br'
#     }
#
#     response = requests.get(url, headers=headers)
#     print(response.text)


# import requests


# def music():
#     url = "https://ac.dun.163.com/v2/m/b"
#
#     headers = {
#         'Host': 'ac.dun.163.com',
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'tls': '1',
#         'Cookie': '_ntes_nnid=a382db1b647aa558b41d81e6f51c9852,1711957856326; _ntes_nuid=a382db1b647aa558b41d81e6f51c9852',
#         'Connection': 'keep-alive',
#         'Accept': '*/*',
#         'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
#         'Content-Length': '1519',
#         'Accept-Encoding': 'gzip, deflate, br',
#         'User-Agent': '%E7%BD%91%E6%98%93%E4%BA%91%E9%9F%B3%E4%B9%90/4918 CFNetwork/1410.0.3 Darwin/22.6.0'
#     }
#
#     data = {
#         'd': 'd=%7B%22rdata%22%3A%22a%2B8Ucj9YtIAU6cpe0lf5aztS2s75Hclw%2BGPhmyuhLr5P%5C%2FwA8kZGk5uWasWnIxCnF%2BsBUse0bmk6Zl6b2mPBXjxwFTSxIuAl1RNMpvyEmbnq%2BzDWOYxu0Gp1euu3zj4xlkUxoFRYmBfkip%2BI7yiXWFg1lMjhFThsbaLkJNKpEVf7QSNuCS%5C%2FEJyinzNVQCUweDq6W9U0vMdKFl8y63pXUlsDilCV%5C%2Fp8HPTmFQO2Lx76nOIkhsbUtU9ZeixPk9RQ3Awd7ZWTsNS5Ujrc4lKSgnERRBseje%2BnSuX0oYi120c8Lvhz59MW8AZbTS%2Bsyeq8sJeIb54D49Z0biDfKQyUffINoNm%2BBvNYN3P6uXVO4LIR3GBUmgR0K7ygMp4Ejty%2B%2Bene3t5sdYRxmIRo6nu34bPidKCxz2P0l5%5C%2FwhsimGFK0akLffqxL6btFoKpWshxxraEbid060wb3JNSkfe%5C%2FuK6TVFz26HjBo28amkiKhQsWD6dFBshER6XXf75cHOQTdHhF0UX6iOt0QxA7UEFKpNEjOwe12ffv2buizCSjfGHgafwIJHTNoX7%5C%2FxKCbyZYscI3eYyulLUyGFRvNQEsjVqXLGt%2B9w5SoKjRFF89DbyfO1A7yO0PJ0M8IqxDxOSJAMQorSLHDsMmqgbMz%5C%2Ff1mbCvxJEhAHoLKIRzM5nUkT4FNnFfY0Z%2BfjqGclWJO37GG43ylcp2rfzv6OyI5wjxHPgHTX6kTJmPo63i0P3g7K7aGfFXXNhj3aBafi3lQQclT8lXkcDwakIvKvNXJBQCKqhLZO68bs69FbZknG%5C%2F%2BPwBcdgNANnWq64I6ZgWeo9kcquo9ATe0kfn5i3IwXep2P6KI50SSBMDdrCjJ%5C%2F9hGjv5GfyKgqstOP29arnGp1tZkFEmFSt%5C%2FSt56QiT40g04%2BBZtmohDoSABxnj4roZ0gqVZA7E4PCDtWtgMuSz%2B4jnWtC1dGI6tWvwxQV7WtoMtVUFlwvXPEQjM3zu2i4yc1%2BUJDP02ZrApbR58bhhv6J%2Buimqyd9L87VExh7oZIzn4esGTc3%2B2FxYYpXF%5C%2FsmbuaXbb1RxsX8SNNHu9LBKeWWbv1Fh0FMQHLRTojIZ9Kp4laIk%2BIjB0b5dk8JhciJpU3%5C%2FuvYVsRpJ7jmuYacEGRZcxt7tdZPLJSOB6zjEDYqETISG00gqLg%3D%3D%22%2C%22rk%22%3A%22fegVGytIDypOAMwScbtuArOvkF3o0MpvTZtN2yZ0zCIfg8sM0QUN8de4%5C%2FlsRNsVrCOUhQvkn7DwvQZ%5C%2FSbDc2g1ySI7lIuXyGVGMZtsDL2%5C%2F4NObaFkYdNA2e2FYjvuIBcSNhFuJcVG1t9i4%2Bia5fJ%2BmsrWF2COOFLKSMvixA7hCY%3D%22%7D'
#     }
#
#     response = requests.post(url, headers=headers, data=data)
#     print("----------------------response=", response.text)

def test():
    import requests
    import json

    # 设置请求的URL和头部信息
    url = 'https://stdcrm.dtmiller.com/scrm-promotion-service/mini/wly/user/info'
    headers = {
        'Host': 'stdcrm.dtmiller.com',
        'Connection': 'keep-alive',
        'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJtaW5pYXBwX2N1c3RvbWVyIiwic3ViIjoib0JMbkk1ZnllSnMzWU5WY2hpeFZWdXRCaHlETSIsImV4cCI6MTcxNTE5NTEzNH0.mq6KyLJ_QbgSy6ZrnXp3xrtc2HPfjxq1-WBg9QNlrbmtZsnKQ7ZJXA3awsfIuFm1PO9L_Izh4v9TLEVDUQ9OUg',
        'Content-Type': 'application/json',  # 注意这里的Content-Type是大小写敏感的
        'Accept-Encoding': 'gzip,compress,br,deflate',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.49(0x18003129) NetType/4G Language/zh_CN',
        'Referer': 'https://servicewechat.com/wxed3cf95a14b58a26/197/page-frame.html'
    }

    # 假设此请求不需要发送任何数据（即GET请求），如果有需要发送的数据，请修改此处
    # 例如，如果需要发送JSON数据，可以使用json参数
    # data = {'key': 'value'}

    # 使用requests库发送GET请求（或者根据实际需要发送POST请求）
    response = requests.get(url, headers=headers)

    # 检查响应状态码并处理响应内容
    if response.status_code == 200:
        # 如果成功，处理响应内容
        print(response.json())
    else:
        # 如果失败，打印错误信息
        print(f"请求失败，状态码：{response.status_code}")
        print(response.text)





#
if __name__ == '__main__':
    test()
