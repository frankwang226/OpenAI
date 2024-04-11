from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
# 数据导入
loader = WebBaseLoader("https://docs.smith.langchain.com/overview")
docs = loader.load()
# 数据切分
text_splitter = RecursiveCharacterTextSplitter()
documents = text_splitter.split_documents(docs)
# 创建embedding
embeddings = OpenAIEmbeddings()
# 通过向量数据库存储
vector = FAISS.from_documents(documents, embeddings)
# 查询检索
# 创建 prompt
prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:
<context>
{context}
</context>
Question: {input}""")
# 创建模型
llm = ChatOpenAI()
# 创建 document 的chain， 查询
document_chain = create_stuff_documents_chain(llm, prompt)

# # 直接使用传入的文本内容
# from langchain_core.documents import Document
# print(document_chain.invoke({
#     "input": "how can langsmith help with testing?",
#     "context": [Document(page_content="langsmith can let you visualize test results")]
# }))

from langchain.chains import create_retrieval_chain
# # 创建搜索chain 返回值为 VectorStoreRetriever
retriever = vector.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)
# # 执行请求
response = retrieval_chain.invoke({"input": "how can langsmith help with testing?"})
print(response["answer"])
