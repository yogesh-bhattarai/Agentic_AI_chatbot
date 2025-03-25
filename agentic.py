import os
GROQ_API_KEY= os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY= os.environ.get("TAVILY_API_KEY")
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import create_react_agent
system_prompt="act as a AI chatbot that who is smart enought to provide me an answer to any question i ask"

groq_llm= ChatGroq(model= "llama-3.3-70b-versatile",api_key= "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")
search = TavilySearchResults(max_results= 2,tavily_api_key="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")
agent= create_react_agent(
    model= groq_llm,
    tools=[search],
    state_modifier= system_prompt)
query="tell me the current trend in the nepal stock market"
state={"message": query}
response= agent.invoke(state)
print(response)