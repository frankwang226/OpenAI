import os
from openai import OpenAI
# 使用个人注册的token
def test_text_generation():
    # openai.api_key = os.getenv('OPENAI_API_KEY_LEARN')
    # openai.api_base = os.getenv('OPENAI_API_BASE_LEARN')
    # openai.base_url = os.getenv('OPENAI_BASE_URL_LEARN')
    client = OpenAI()
    
    response = client.chat.completions.create(
        model='gpt-3.5-turbo',
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

