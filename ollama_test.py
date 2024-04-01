from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import Ollama

prompt_template = "What is a good name for a company that makes {product}?"

# prompt_template = "Where is the capital of China?"

ollama_llm = Ollama(model="llama2:latest")
llm_chain = LLMChain(
    llm=ollama_llm,
    prompt=PromptTemplate.from_template(prompt_template) 
)
print(llm_chain("colorful socks"))

# print(llm_chain("capital"))
