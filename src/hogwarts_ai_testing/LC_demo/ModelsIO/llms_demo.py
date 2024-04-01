# ChatGPT模型调用对象
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

llm = OpenAI()
# 输入提示词模版中的变量部分，调用链会自动完成后续的调用和解析
res = llm.invoke("出给一个宣传语")  # invoke 调用
res_batch = llm.batch(["出给一个宣传语", "将静夜思翻译为英文"])  # batch 调用
print(res)
print("======1")
print(res_batch)
print("======2")


'''
结合模版
'''
# 提示词模板
prompt = PromptTemplate.from_template("给出一个关于{goods}的宣传语")
# 将提示词模板与大模型组合为一个调用链
chain = prompt | llm
# 输入提示词模版中的变量部分，调用链会自动完成后续的调用和解析
res = chain.invoke({"goods": "鲜花"})  # invoke 调用
res_batch = chain.batch([{"goods": "鲜花"}, {"goods": "冰淇淋"}])  # batch 调用
print(res)
print("======3")
print(res_batch)
