import os

import openai as openai

from openai import OpenAI
from openai import AsyncOpenAI

# openai.base_url = "https://api.openai.com/v1"

client = OpenAI(
    api_key=os.environ['OPENAI_API_KEY'],
)

'''
# 学院提供key的方式
client = OpenAI(api_key="b1f15c51c0ea080ccf16172802a44960")
openai.api_base = "https://apitoken.ceba.ceshiren.com/openai/v1/"
openai.base_url = "https://apitoken.ceba.ceshiren.com/openai/v1/"
"http://20.150.220.45/chatgpt/v1"
'''

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Where is the capital of China?",
        },
    ],
)

# 打印结果是：ChatCompletionMessage(content='The capital of China is Beijing.', role='assistant', function_call=None, tool_calls=None)
print(completion.choices[0].message)

# 打印结果是：CompletionUsage(completion_tokens=0, prompt_tokens=0, total_tokens=0)
print(dict(completion).get('usage'))

'''
打印结果是：
{
  "id": "chatcmpl-krmt5cxGc9u7SzC2mEGG0UoFrUV6b",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "logprobs": null,
      "message": {
        "content": "The capital of China is Beijing.",
        "role": "assistant",
        "function_call": null,
        "tool_calls": null
      }
    }
  ],
  "created": 1710415795,
  "model": "gpt-3.5-turbo",
  "object": "chat.completion",
  "system_fingerprint": "fp_ab32547f0d",
  "usage": {
    "completion_tokens": 0,
    "prompt_tokens": 0,
    "total_tokens": 0
  }
}
'''
print(completion.model_dump_json(indent=2))

# 异步

'''
client = AsyncOpenAI(api_key=os.environ['OPENAI_API_KEY'])
completion = await client.chat.completions.create(model="gpt-3.5-turbo",
                                                  messages=[{"role": "user", "content": "Hello world"}])
'''

# 官网示例
'''
client = OpenAI(api_key="sk-6DRRiOSKKtdbGZRL9771171546D14261974bB5Bb81FfB260", base_url="https://www.gptapi.us/v1")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system",
         "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

print(completion.choices[0].message)
'''

'''
def test_text_to_speech():
    response = client.audio.speech.create(
        model="tts-1",
        voice="nova",
        input="Hello, how are you?"
    )

    response.stream_to_file(speech_file="speech.mp3")
'''