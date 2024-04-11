from urllib.parse import quote_plus

import sqlalchemy
import yaml
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


def mysql(self, question):
    yaml_data = yaml.safe_load(open("../../data/password.yaml"))
    password = yaml_data['password']
    url = "mysql+pymysql://tempwrite:" + quote_plus(
        password) + "@bj-cdb-3kzmnwf8.sql.tencentcdb.com:61397/ezp-mall"
    engine = create_engine(url)

    db = SQLDatabase.from_uri(url)

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    set_debug(True)

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

    response = chain.invoke(SQLInputWithTables(
        question=question,
        table_names_to_use=['mall_sales_order', 'mall_sales_order_dtl']))
    print(response)



if __name__ == '__main__':
    mysql("mall_sales_order表的Id关联mall_sales_order_dtl表的OrderId，请问品牌739，最近一个月的卖出最多的商品是哪件，给出商品名称？")
