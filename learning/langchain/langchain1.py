import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if api_key is not None:
    print("API key loaded successfully!")
    # Use the key, e.g.,
    # response = requests.get(f"https://api.example.com/data?key={api_key}")
else:
    print("API key not found")

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(temperature=0, model="gpt-4-turbo", max_tokens=1000,api_key=api_key)

output=llm.invoke("Hello, how are you?")

print(output)


