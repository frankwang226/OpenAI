import os

import openai as openai


from openai import OpenAI
from openai import AsyncOpenAI


client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
)

completion = OpenAI().completions.create(
    model="gpt-3.5-turbo",
    prompt="Say this is a test",
)

print(completion.choices[0].text)
print(dict(completion).get('usage'))
print(completion.model_dump_json(indent=2))


# 异步

'''
client = AsyncOpenAI(api_key=os.environ['OPENAI_API_KEY'])
completion = await client.chat.completions.create(model="gpt-3.5-turbo",
                                                  messages=[{"role": "user", "content": "Hello world"}])
'''
