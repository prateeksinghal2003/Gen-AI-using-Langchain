#using hugging face API for open models

from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import  load_dotenv
import os
print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))

load_dotenv()

llm=HuggingFaceEndpoint(
    # repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
    repo_id="zai-org/GLM-5.1",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)


model=ChatHuggingFace(llm=llm)

result=model.invoke("who is the current president in USA?")
print(result.content)