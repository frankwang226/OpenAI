'''
OpenAI 函数输出解析器
LangChain 支持解析 OpenAI 提供的函数调用，并提供了以下四种形式来处理输出结果：

JsonOutputFunctionsParser：生成 JSON 格式的结果。
JsonKeyOutputFunctionsParser：指定 JSON 中某个 key 对应的 value。
PydanticOutputFunctionsParser：解析 Pydantic 模型的结构。
PydanticAttrOutputFunctionsParser：直接输出模型中某个参数的值。
'''
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.utils.function_calling import convert_to_openai_function
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers.openai_functions import JsonOutputFunctionsParser, JsonKeyOutputFunctionsParser

# 调用大模型
model = ChatOpenAI()
# 提示词模板
prompt = ChatPromptTemplate.from_template("出给一个关于 {goods} 的广告宣传语")
# 自定义函数
functions = [
    {
        "name": "advertisement",
        "description": "一段广告词",
        "parameters": {
            "type": "object",
            "properties": {
                "goods": {"type": "string", "description": "要进行广告的产品"},
                "ads": {"type": "string", "description": "广告词"},
            },
            "required": ["goods", "ads"],
        },
    }
]

'''
JsonOutputFunctionsParser
'''
# 创建调用链 包含输出解析器
chain_json_with_parser = prompt | model.bind(function_call={"name": "advertisement"},
                                             functions=functions) | JsonOutputFunctionsParser()
res_json_with_parser = chain_json_with_parser.invoke({"goods": "冰淇淋"})
print(res_json_with_parser)
print(type(res_json_with_parser))
print("======1")

'''
JsonKeyOutputFunctionsParser
'''
# 创建调用链 包含输出解析器
chain_key_parser = prompt | model.bind(function_call={"name": "advertisement"},
                                       functions=functions) | JsonKeyOutputFunctionsParser(key_name='ads')
res_key_parser = chain_key_parser.invoke({"goods": "摩托车"})
print(res_key_parser)
print(type(res_key_parser))
print("======2")

'''
Pydantic 模型
'''
# 导入 V1 版本
from pydantic.v1 import BaseModel, Field


class Advertisement(BaseModel):
    goods: str = Field(description="物品")
    ads: str = Field(description="宣传语")


'''
PydanticOutputFunctionsParser
'''
from langchain_core.output_parsers.openai_functions import PydanticOutputFunctionsParser

# 调用大模型
model = ChatOpenAI()
# 提示词模板
prompt = ChatPromptTemplate.from_template("出给一个关于 {goods} 的广告宣传语")
# 定义解析器
parser = PydanticOutputFunctionsParser(pydantic_schema=Advertisement)
# 调用函数
openai_functions = [convert_to_openai_function(Advertisement)]
# 创建调用链
chain_pydantic_parser = prompt | model.bind(functions=openai_functions) | parser
# 输出大模型执行结果
res_pydantic_parser = chain_pydantic_parser.invoke({"goods": "饮料"})
print(res_pydantic_parser)
print(type(res_pydantic_parser))
print("======3")

'''
PydanticAttrOutputFunctionsParser
'''
from langchain_core.output_parsers.openai_functions import PydanticAttrOutputFunctionsParser

# 定义 pydantic 参数输出解析器，传入 Pydantic 模型和需要输出的属性名
parser = PydanticAttrOutputFunctionsParser(pydantic_schema=Advertisement, attr_name='ads')
# 调用函数
openai_functions = [convert_to_openai_function(Advertisement)]
# 创建调用链 包含输出解析器
chain_pydantic_parser = prompt | model.bind(functions=openai_functions) | parser
# 传入参数执行
res_pydantic_parser = chain_pydantic_parser.invoke({"goods": "饮料"})
print(res_pydantic_parser)
print(type(res_pydantic_parser))
