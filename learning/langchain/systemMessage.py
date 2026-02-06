import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage,SystemMessage

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if api_key is not None:
    print("API key loaded successfully!")
else:
    print("API key not found")

llm = ChatOpenAI(temperature=0, model="gpt-5.2", max_tokens=1000,api_key=api_key)


system_msg=SystemMessage(content="You are an assistant who not only answers but also explain how you derived it ")

human_msg=HumanMessage(content="Please let me know the capital of Tamilnadu")

output=llm.invoke([system_msg,human_msg])
print(f"output is ${output}")