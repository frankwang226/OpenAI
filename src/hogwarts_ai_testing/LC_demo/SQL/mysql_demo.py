from urllib.parse import quote_plus

import sqlalchemy
from langchain.chains.sql_database.query import SQLInputWithTables
from langchain.globals import set_debug
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, text
from sqlalchemy.orm import sessionmaker

from langchain_community.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain_openai import ChatOpenAI
from langchain_community.tools.sql_database.tool import QuerySQLDataBaseTool

from operator import itemgetter

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

password = "nZCEPbDFJ#uu7k@I"
url = "mysql+pymysql://tempwrite:" + quote_plus(
    password) + "@bj-cdb-3kzmnwf8.sql.tencentcdb.com:61397/ezp-mall"  # password + "@bj-cdb-3kzmnwf8.sql.tencentcdb.com:61397/ezp-mall?charset=utf8"
engine = create_engine(url)

db = SQLDatabase.from_uri(url)

# Session = sessionmaker(bind=engine)
# session = Session()
#
# result = session.execute(text('SELECT FxType FROM mall_fx_person where brandid=739 order by id desc limit 1'))
# rows = result.fetchall()
# for row in rows:
#     print(row)
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, verbose=True)
set_debug(True)
# chain = create_sql_query_chain(llm, db)
# response = chain.invoke(SQLInputWithTables(
#     question="Please retrieve the first record from the 'mall_sales_order' table where BrandId is equal to 739",
#     table_names_to_use=['mall_sales_order', 'mall_sales_order_dtl']))
# print(response)
# print(db.run(response))
# print("=======")

# 打印prompt
# chain.get_prompts()[0].pretty_print()

execute_query = QuerySQLDataBaseTool(db=db)
write_query = create_sql_query_chain(llm, db)

answer_prompt = PromptTemplate.from_template(
    """Given the following user question, corresponding SQL query, and SQL result, answer the user question.

Question: {question}
SQL Query: {query}
SQL Result: {result}
Answer: """
)

answer = answer_prompt | llm | StrOutputParser()
chain = (
        RunnablePassthrough.assign(query=write_query).assign(
            result=itemgetter("query") | execute_query
        )
        | answer
)

# response = chain.invoke(SQLInputWithTables(
#     question="mall_sales_order是订单表，TotalMoney是订单金额，BrandId是品牌编号，请问品牌739，最近一个月的订单总金额是多少元？",
#     table_names_to_use=['mall_sales_order', 'mall_sales_order_dtl']))

# response = chain.invoke(SQLInputWithTables(
#     question="mall_sales_order表的Id关联mall_sales_order_dtl表的OrderId，请问品牌739，最近一个月的卖出最多的商品是哪件，给出商品名称？",
#     table_names_to_use=['mall_sales_order', 'mall_sales_order_dtl']))

response = chain.invoke(SQLInputWithTables(
    question="mall_sales_order表的Id关联mall_sales_order_dtl表的OrderId，请问品牌739，最近一个月的卖出最多的商品是哪件，给出商品名称？",
    table_names_to_use=['mall_sales_order', 'mall_sales_order_dtl']))
print(response)
