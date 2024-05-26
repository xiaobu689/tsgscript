import os
import random
from http import HTTPStatus
import dashscope


# 通义千问API
def qianwen_messages(basic_question, question):
    content = ''
    qw_key = os.getenv("QIANWEN_KEY")
    if not qw_key:
        print(f'⛔️未获取到通义千问key：请检查变量 {qw_key} 是否填写')
    else:
        dashscope.api_key = qw_key
        messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},
                    {'role': 'user', 'content': basic_question + question}]
        response = dashscope.Generation.call(
            dashscope.Generation.Models.qwen_turbo,
            messages=messages,
            seed=random.randint(1, 10000),
            result_format='message',
        )
        if response.status_code == HTTPStatus.OK:
            content = response['output']['choices'][0]['message']['content']
        else:
            print('Request id: %s, Status code: %s, error code: %s, error message: %s' % (
                response.request_id, response.status_code,
                response.code, response.message
            ))
    return content
