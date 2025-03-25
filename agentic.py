import os
GROQ_API_KEY= os.environ.get("GROQ_API_KEY")
from langchain_groq import ChatGroq

groq_llm= ChatGroq(model= "llama-3.3-70b-versatile")
print(groq_llm)