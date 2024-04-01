from langchain.output_parsers import ResponseSchema, StructuredOutputParser
from langchain_core.messages import SystemMessage
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser, PydanticOutputParser
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic.v1 import BaseModel, Field

'''
String解析器
'''
# 定义模型
model = ChatOpenAI()
# 提示词模板
messages = ChatPromptTemplate.from_messages([
    SystemMessage(content="你是一个翻译各种语言的助手"),
    HumanMessagePromptTemplate.from_template("把 {poetry} 的原文诗翻译为英文")
])
# 输出解析器
parser = StrOutputParser()
# 调用链
chain_with_parser = messages | model | parser  # 使用输出解析器
res_with_parser = chain_with_parser.invoke({"poetry": "静夜思"})
print(res_with_parser)
print(type(res_with_parser))
print("======1")

'''
Json解析器
'''
# 定义模型
model = ChatOpenAI()
# Json输出解析器
parser = JsonOutputParser()
# 模板提示，输出 json 格式的回答
prompt = PromptTemplate(
    template="根据用户的输入，给出一段中文宣传语 \n{format_instructions}\n{ads}\n",
    input_variables=["ads"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
# 调用链 包含json输出解析器
chain_with_parser = prompt | model | parser
res_with_parser = chain_with_parser.invoke({"ads": "音乐节"})
print(res_with_parser)
print(type(res_with_parser))
print("======2")


'''
Pydantic解析器
Pydantic 的功能，例如数据验证、序列化和反序列化等
'''


class Translation(BaseModel):
    origin_str: str = Field(description="原始输入的值")
    trans_str: str = Field(description="翻译后的值")


# 定义一个模型
model = ChatOpenAI(temperature=0)
# 使用 pydantic 输出解析器解析 Translation 类
parser = PydanticOutputParser(pydantic_object=Translation)
# 提示模板
prompt = PromptTemplate(
    template="翻译用户输入的内容为英文\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
# 包含解析器的调用链
chain_with_parser = prompt | model | parser
res_parser = chain_with_parser.invoke({"query": "赏花"})
# 输出返回的内容及类型
print(res_parser)
print(type(res_parser))
print("======3")

'''
结构化输出解析器
'''
response_schemas = [
    ResponseSchema(name="slogan", description="宣传语内容"),
    ResponseSchema(name="req", description="宣传语限制在10个字符内"),
]
output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
prompt = PromptTemplate(
    template="根据用户输入的主题给出宣传语\n{format_instructions}\n{topics}",
    input_variables=["topics"],
    partial_variables={"format_instructions": output_parser.get_format_instructions()},
)

model = ChatOpenAI(temperature=0)
chain_with_parser = prompt | model | output_parser
res_with_parser = chain_with_parser.invoke({"topics": "音乐节"})
print(res_with_parser)
print(type(res_with_parser))

