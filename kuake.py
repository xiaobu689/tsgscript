# -*- coding: utf-8 -*-
import logging
import os
import re
from loguru import logger
import json
from jdbean import pushPlusAlert
from task_request import req


# PushPlus推送
async def pushPlusNotify(**kwargs):
    title = kwargs.get("title", "")
    content = kwargs.get("msg", "")
    name = 'PUSH_PLUS_TOKEN'
    token = os.getenv(name)
    if not token:
        print(f'⛔️未获取到ck变量：请检查变量 {name} 是否填写')
        exit(0)
    if token:
        meta = {
            "method": "POST",
            "url": "http://www.pushplus.plus/send",
            "data": json.dumps({
                'token': token,
                'title': title,
                'content': content,
            }),
            "headers": {"Content-Type": "application/json"}
        }
        res = await req(**meta)
        if res and not res.json().get('errcode'):
            return True
        else:
            return False


# 夸克签到
async def kk_sign():
    logging.info("----------------夸克签到任务开始----------------")
    result = {
        "code": 400,
        "msg": '请输入 kua ke cookie!',
        "time": 0
    }
    env_name = 'KK_COOKIE'
    token = os.getenv(env_name)
    if not token:
        print(f'⛔️未获取到ck变量：请检查变量 {env_name} 是否填写')
        exit(0)

    cookies = re.split(r'[@\n]', token)
    print(f"移动硬盘共获取到{len(cookies)}个账号")

    for i, cookie in enumerate(cookies, start=1):
        print(f"\n======== ▷ 第 {i} 个账号 ◁ ========")
        # 如果变量的名字是 "KK_COOKIE"，那么就继续执行
        if not [cookie]:
            return result
        meta = {
            "method": "GET",
            "url": "https://drive-m.quark.cn/1/clouddrive/capacity/growth/info?pr=ucpro&fr=pc&uc_param_str=",
            "headers": {
                "Cookie": cookie,
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
            }
        }
        res = await req(**meta)
        res_dict = res.json()
        if res_dict['status'] == 200:
            is_sign = res_dict["data"]["cap_sign"]["sign_daily"]
            if is_sign:
                number = res_dict["data"]["cap_sign"]["sign_daily_reward"] / (1024 * 1024)
                result.update({
                    "code": 200,
                    "msg": f"✅今天已经签到过了,签到奖励容量 {int(number)} MB"
                })
            else:
                sign_url = "https://drive-m.quark.cn/1/clouddrive/capacity/growth/sign?pr=ucpro&fr=pc&uc_param_str="
                payload = json.dumps({"sign_cyclic": "True"})
                meta.update({
                    "method": "POST",
                    "url": sign_url,
                    "data": payload
                })
                res = await req(**meta)
                res_dict = res.json()
                reward = res_dict["data"]["sign_daily_reward"] / (1024 * 1024)
                result.update({
                    "code": 200,
                    "msg": f"✅签到成功，今日签到奖励 {int(reward)} MB"
                })
        else:
            result.update({
                "code": 400,
                "msg": f"❌账号异常，签到失败，token 已失效."
            })
    # PushPlus通知
    logger.info(result)
    await pushPlusAlert(**result)
    logging.info("夸克签到任务结束")

if __name__ == '__main__':
    kk_sign()
