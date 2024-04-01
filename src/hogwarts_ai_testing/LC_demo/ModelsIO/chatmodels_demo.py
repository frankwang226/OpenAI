from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import ChatOpenAI

'''
基础消息类型
'''
# ChatGPT模型调用对象
model = ChatOpenAI()
# 消息列表
messages = [
    {"role": "system", "content": "你是一个制定方案的助手"},
    {"role": "user", "content": "请给出我一个旅行方案，在北京的一日游"},
]
message_1 = [
    {"role": "system", "content": "你是一个制定方案的助手"},
    {"role": "user", "content": "请给出我一个旅行方案，在北京的一日游"},
]
message_2 = [
    {"role": "system", "content": "你是一个制定方案的助手"},
    {"role": "user", "content": "请给出我一个考雅思方案，备考时间三个月"},
]
# invoke 调用
res = model.invoke(messages)
# batch 调用
res_list = model.batch([message_1, message_2])
print(res)
print("=======")
print(res_list)
print("=======1")


'''
指定消息类型
'''
# ChatGPT 调用对象
model = ChatOpenAI()
# 消息列表，指定消息类型
messages = [
    SystemMessage(content="你是一个翻译各种语言的助手"),
    HumanMessage(content="把静夜思这首诗翻译为英文")
]
messages_1 = [
    SystemMessage(content="你是一个给出广告词的助手"),
    HumanMessage(content="给出耳机的广告词")
]
messages_2 = [
    SystemMessage(content="你是一个给出宣传语的助手"),
    HumanMessage(content="宣传音乐节")
]
# invoke 方式调用
res = model.invoke(messages)
# batch 方式调用
res_batch = model.batch([messages_1, messages_2])
print(res)
print("=======")
print(res_batch)
print("=======2")

'''
结合模版
'''
# ChatGPT 调用对象
model = ChatOpenAI()
# 消息提示模板
messages = ChatPromptTemplate.from_messages([
    SystemMessage(content="你是一个翻译各种语言的助手"),
    HumanMessagePromptTemplate.from_template("把 {poetry} 的原文诗翻译为英文")
])
# 将模板和模型调用组合为调用链
chain = messages | model
# 发送请求
res = chain.invoke({"poetry": "静夜思"})
print(res)

'''
使用Runnable简化输入
'''
model = ChatOpenAI()
prompt = ChatPromptTemplate.from_messages([
    SystemMessage(content="你是一个翻译各种语言的助手"),
    HumanMessagePromptTemplate.from_template("把 {poetry} 的原文诗翻译为英文")
])
chain1 = RunnableParallel(poetry=RunnablePassthrough()) | prompt | model | StrOutputParser()
res_simplify = chain1.invoke("静夜思")
print(res_simplify)
