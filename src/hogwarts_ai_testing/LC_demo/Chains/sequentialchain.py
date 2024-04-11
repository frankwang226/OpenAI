import langchain
from langchain.chains.llm import LLMChain
# LangChain相关模块的导入

from langchain.prompts import ChatPromptTemplate
from langchain.chains import SequentialChain
from langchain_openai import ChatOpenAI

# 在全局范围开启详细模式，能将调用大模型时发送的数据打印到控制台，绿色文本
langchain.verbose = True


# 本示例中为了让结果更具有创造性，temperature设置为0.9
llm = ChatOpenAI(temperature=0.9)

# Chain1 语言转换，产生英文产品名
prompt1 = ChatPromptTemplate.from_template(
    "将以下文本翻译成英文: {product_name}"
)
chain1 = LLMChain(
    # 使用的大模型实例
    llm=llm,
    # prompt模板
    prompt=prompt1,
    # 输出数据变量名
    output_key="english_product_name",
)
# Chain2 根据英文产品名，生成一段英文介绍文本
prompt2 = ChatPromptTemplate.from_template(
    "Based on the following product, give an introduction text about 100 words: {english_product_name}"
)
chain2 = LLMChain(
    llm=llm,
    prompt=prompt2,
    output_key="english_introduce"
)
# Chain3 找到产品名所属的语言
prompt3 = ChatPromptTemplate.from_template(
    "下列文本使用的语言是什么?: {product_name}"
)
chain3 = LLMChain(
    llm=llm,
    prompt=prompt3,
    output_key="language"
)
# Chain4 根据Chain2生成的英文介绍，使用产品名称原本的语言生成一段概述
prompt4 = ChatPromptTemplate.from_template(
    "使用语言类型为: {language} ，为下列文本写一段不多于50字的概述: {english_introduce}"
)
chain4 = LLMChain(
    llm=llm,
    prompt=prompt4,
    output_key="summary"
)
# 标准版的序列Chain,SequentialChain,其中每个chain都支持多个输入和输出，
# 根据chains中每个独立chain对象，和chains中的顺序，决定参数的传递，获取最终的输出结果
overall_chain = SequentialChain(
    chains=[chain1, chain2, chain3, chain4],
    input_variables=["product_name"],
    output_variables=["english_product_name", "english_introduce", "language", "summary"],
    verbose=True
)
product_name = "黄油啤酒"
res = overall_chain(product_name)
print(res)
