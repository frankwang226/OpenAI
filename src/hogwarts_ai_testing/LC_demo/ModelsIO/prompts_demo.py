from langchain_core.messages import SystemMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate, HumanMessagePromptTemplate

'''
PromptTemplate--->会话模型
'''
# 定义一个包含两个变量的提示模板
prompt1 = PromptTemplate.from_template(
    "给出一个{topic} 的广告, 它的价格是￥ {price} ，广告需要能够引起用户的兴趣")
# 格式化并传入参数
print(prompt1.format(topic='冰淇淋', price=3))

# invoke 调用
prompt_val = prompt1.invoke({"topic": "冰淇淋", "price": "3"})
print(prompt_val)
# 转换为字符串
prompt_val_str = prompt_val.to_string()
print(prompt_val_str)

# 定义一个包含两个变量的提示模板
prompt2 = PromptTemplate.from_template("告诉我一个广告")
# 格式化并传入参数
print(prompt2.format())
print("----1")

'''
ChatPromptTemplate--->聊天模型
'''
# 制定模板
chat_prompt = ChatPromptTemplate.from_messages(
    [("system", "你是一个游戏的 npc，有三个任务让玩家完成，需要给出玩家三个任务，并且规定出完成的标准。"),
     ("human", "你好，我是这个游戏的玩家"),
     ("ai", "{user} 玩家你好，欢迎来到这个游戏"),
     ("human", "{user_input}"),
     ])
print(chat_prompt)
print(type(chat_prompt))
# 格式化消息列表，并且传入参数
messages = chat_prompt.format_messages(user="ling", user_input="你好，我需要做什么")
print(messages)
print(type(messages))
print("----2")
# 使用 invoke 方式调用
chat_val = chat_prompt.invoke({"user": "ling", "user_input": "你好，我需要做什么"})
chat_str = chat_val.to_string()
chat_messages = chat_val.to_messages()
print(chat_val)
print(type(chat_val))
print(chat_str)
print(type(chat_str))
print(chat_messages)
print(type(chat_messages))
print("----3")

# 传入 SystemMessage HumanMessagePromptTemplate 实例
chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content=(
            "你是一个擅长制定计划的助手"
            "计划需要贴合用户需求，给出详细的时间节点和任务指标"
        )),
        HumanMessagePromptTemplate.from_template("{user_req}")
    ]
)
print(chat_template)
print(type(chat_template))
messages_o = chat_template.format_messages(user_req="我想要一个旅行计划")
print(messages_o)
print(type(messages_o))
