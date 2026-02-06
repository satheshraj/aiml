import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if api_key is not None:
    print("API key loaded successfully!")
else:
    print("API key not found")


llm = ChatOpenAI(temperature=0, model="gpt-5.2", max_tokens=1000,api_key=api_key)

output=llm.invoke("Hello, how are you?")

print(output)


