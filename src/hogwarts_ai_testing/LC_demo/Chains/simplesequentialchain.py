# LangChain相关模块的导入
from langchain.chains.llm import LLMChain
from langchain.prompts import ChatPromptTemplate
from langchain.chains import SimpleSequentialChain
from langchain_openai import ChatOpenAI

# 创建OpenAI调用实例
# temperature用来设置大模型返回数据的随机性和创造性，较低的数值返回的数据就更贴近现实。
llm = ChatOpenAI(temperature=0.9)
# 第一个LLM请求的prompt模板
first_prompt = ChatPromptTemplate.from_template(
    "请给生产 {product} 的工厂起一个恰当的厂名"
)
# 第一个Chain，接收外部输入，根据模版请求大模型获取输出，作为第二个Chain的输入
chain_one = LLMChain(llm=llm, prompt=first_prompt, verbose=True)
# 第二个大模型请求的prompt模版
second_prompt = ChatPromptTemplate.from_template(
    "为厂名写一段不少于20字的广告语: {company_name}"
)
# 第二个Chain，接收第一个Chain的输出，根据模版请求大模型获取输出
chain_two = LLMChain(llm=llm, prompt=second_prompt, verbose=True)
# 将请求拆分成两个Chain，可以针对每段请求细化相应的prompt内容，得到更准确更合理的结果，并且也可以复用其中的每个Chain实例
# 使用SimpleSequentialChain将两个Chain串联起来，其中每个Chain都只支持一个输入和一个输出，根据chains列表中的顺序，将前一个Chain的输出作为下一个Chain的输入
overall_simple_chain = SimpleSequentialChain(
    chains=[chain_one, chain_two],
    verbose=True
)
# 第一个Chain需要的输入
product = "IPhone999 Pro Max Ultra"
# 通过run方法，传入参数，逐个运行整个Chain后，获取最终的结果
res = overall_simple_chain.invoke(product)
print(res)
