import random
from http import HTTPStatus
import dashscope

basic_news_question = '我需要你针对下面的文章，从一个民众的角度进行评论，我希望你的输出只有评论内容，没有别的无关紧要的词语，回复格式是：芝麻开门#你的评论#， 评论要日常化，字数在10-25字之间，下面是我需要你发表评论的文章内容：'


def qianwen_messages(basic_question, question):
    content = ''
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
