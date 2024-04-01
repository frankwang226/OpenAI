import ollama
from langchain.llms import Ollama

llm = Ollama(
    base_url="http://localhost:11434",
    model="llama2:latest",
    verbose=True
)

prompt = "Hello, how are you?"
output = llm(prompt)
