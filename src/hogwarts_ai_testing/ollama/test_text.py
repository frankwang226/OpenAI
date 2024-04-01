import os
from openai import OpenAI

# 使用个人注册的token
def test_text_generation():

    client = OpenAI(
        # 切换私有LLM
        base_url='http://127.0.0.1:11434/v1',
        api_key='ollama:llama2:7b',

        # base_url='http://20.150.220.45/chatgpt/v1',
        # api_key='xxx'
    )

    model = 'llama2:7b'

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            # {"role": "user", "content": "Who won the world series in 2020?"},
            # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "中国山东省的省会在哪里"}
        ],
        temperature=0
    )

    answer = response.choices[0].message.content
    print(answer)

