import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers.openai_functions import JsonKeyOutputFunctionsParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_openai import ChatOpenAI

# 提示词模板
prompt = ChatPromptTemplate.from_template("出给一个关于 {goods} 的广告宣传语")
# ChatGPT模型调用对象
model = ChatOpenAI()
# 将两个对象使用顺序组合创建一个调用链，实现提示词组装，模型调用的功能
chain = prompt | model
# 输入提示词模版中的变量部分，调用链会自动完成后续的调用和解析
res = chain.invoke({"goods": "冰淇淋"})
print(res)
print("----")

# 创建模型链，并且加上 “,” 作为停止符，意为当输入结果包含 “,” 时，立即停止生成
chain_stop = prompt | model.bind(stop=["，"]) | StrOutputParser()
res_stop = chain_stop.invoke({"goods": "冰淇淋"})
print(res_stop)
print("----")

# 附加函数调用信息
functions = [
    {
        "name": "advertisement",
        "description": "一段广告词",
        "parameters": {
            "type": "object",
            "properties": {
                "goods": {"type": "string", "description": "要进行广告的产品"},
                "ad": {"type": "string", "description": "广告词"},
            },
            "required": ["goods", "ad"],
        },
    }
]
# 创建调用链 将模板和模型连接起来 并且附带一个函数的调用
# chain_function = prompt | model.bind(function_call={"name": "advertisement"}, functions=functions)
# res_function = chain_function.invoke({"goods": "冰淇淋"})
# print(res_function)
chain_function = prompt | model.bind(function_call={"name": "advertisement"},
                                     functions=functions) | JsonKeyOutputFunctionsParser(key_name='ad')
res_function = chain_function.invoke({"goods": "冰淇淋"})
print(res_function)
print("----")

# 简化输入
# 输入提示字典
map_ = RunnableParallel(goods=RunnablePassthrough())
chain = (
        map_
        | prompt
        | model.bind(function_call={"name": "advertisement"}, functions=functions)
        | JsonKeyOutputFunctionsParser(key_name="ad")
)
# res = chain.invoke({"goods": "冰淇淋"})
res_simplify = chain.invoke("冰淇淋")
print(res_simplify)
