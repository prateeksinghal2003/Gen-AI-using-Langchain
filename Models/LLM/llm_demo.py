# outdated code now 

# from langchain_openai import OpenAI
from langchain_groq import ChatGroq
import os

from dotenv import load_dotenv
load_dotenv()

# llm=OpenAI(model="gpt-3.5-turbo-instruct")
# result=llm.invoke("What is the capital of France?")
# print(result)








llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY")

)

result=llm.invoke("What is the capital of France?")
print(result.content)