import os
from pathlib import Path

from openai import OpenAI

# 使用系统变量 OPENAI_API_KEY OPENAI_BASE_URL
client = OpenAI(
    # base_url='http://20.150.220.45/chatgpt/v1',
    # api_key='xxx'
)
requirement_file = Path(__file__).parent.parent / 'data' / 'requirement.md'
requirement = requirement_file.read_text()
ui_dom = (Path(__file__).parent.parent / 'data' / 'web.html').read_text()
service_doc = (Path(__file__).parent.parent / 'data' / 'service.md').read_text()


def test_case_manual():
    # 调用chat功能
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            # {"role": "user", "content": "Who won the world series in 2020?"},
            # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user",
             "content":
                 f"{requirement}\n\n"
                 f"以上是一段产品的需求介绍，请根据其中的功能生成对应的测试用例。"
                 f"对关键的数据类型进行等价类边界值的用例生成。"}
        ]
    )

    print(response.choices[0].message.content)


def test_case_flow():
    # 调用chat功能
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            # {"role": "user", "content": "Who won the world series in 2020?"},
            # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user",
             "content":
                 f"{requirement}\n\n"
                 f"以上是一段产品的需求介绍。"
                 f"对这个产品的用户操作流程生成一份时序图，要求使用plantuml的格式生成"}
        ]
    )

    print(response.choices[0].message.content)


def test_web():
    # 调用chat功能
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            # {"role": "user", "content": "Who won the world series in 2020?"},
            # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user",
             "content":
                 f"{ui_dom}\n\n"
                 f"以上是网页的html代码。"
                 f"请为这个页面生成对应的web自动化测试用例，使用pytest selenium。"}
        ]
    )

    print(response.choices[0].message.content)


def test_service():
    # 调用chat功能
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            # {"role": "user", "content": "Who won the world series in 2020?"},
            # {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user",
             "content":
                 f"{service_doc}\n\n"
                 f"以上是http接口的描述。"
                 f"请为这个接口生成对应的自动化测试用例，使用pytest requests"}
        ]
    )

    print(response.choices[0].message.content)
