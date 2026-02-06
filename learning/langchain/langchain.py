import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if api_key is not None:
    print("API key loaded successfully!")
    # Use the key, e.g.,
    # response = requests.get(f"https://api.example.com/data?key={api_key}")
else:
    print("API key not found.")

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(temperature=0, model="gpt-4-turbo", max_tokens=1000,api_key="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")

llm.invoke("Hello, how are you?")
