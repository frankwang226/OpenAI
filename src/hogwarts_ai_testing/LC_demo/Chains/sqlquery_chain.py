from langchain_openai import ChatOpenAI
from langchain.chains import create_sql_query_chain
from langchain_community.utilities import SQLDatabase

db = SQLDatabase.from_uri("sqlite:///Chinook.db")
# url: str = '127.0.0.1:8902', user: str = 'root', password: str = '', tenant: str = 'cnosdb', database: str = 'public'
llm = ChatOpenAI(temperature=0, verbose=True)
chain = create_sql_query_chain(llm, db)
response = chain.invoke({"question": "How many employees are there"})
print(response)