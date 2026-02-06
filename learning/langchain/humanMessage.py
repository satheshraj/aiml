import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if api_key is not None:
    print("API key loaded successfully!")
else:
    print("API key not found")

llm = ChatOpenAI(temperature=0, model="gpt-5.2", max_tokens=1000,api_key=api_key)
prompt=[HumanMessage("Please let me know the capital of Tamilnadu")]

output=llm.invoke(prompt)
print(f"Output is ${output}")


