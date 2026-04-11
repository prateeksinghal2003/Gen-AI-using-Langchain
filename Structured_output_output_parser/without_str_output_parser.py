#using hugging face API for open models


from langchain_groq import ChatGroq
from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import  load_dotenv
from langchain_core.prompts import PromptTemplate
import os
print(os.getenv("HUGGINGFACEHUB_API_TOKEN"))

load_dotenv()

# llm=HuggingFaceEndpoint(
#     # repo_id="meta-llama/Meta-Llama-3-8B-Instruct",
#     # repo_id="zai-org/GLM-5.1",
#     repo_id="google/gemma-2-2b-it",
#     task="text-generation",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")
# )


# model=ChatHuggingFace(llm=llm)

model=ChatGroq(model="openai/gpt-oss-120b")



template1=PromptTemplate(template='Write a detailed report on {topic}',
                         input_variables=['topic'])

template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

prompt1=template1.invoke({'topic':"Global Warming"})

result=model.invoke(prompt1)


prompt2=template2.invoke({'text':result})

result2=model.invoke(prompt2)

# print(result)
print(result2.content)






