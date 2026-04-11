from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
model=ChatGroq(model="openai/gpt-oss-120b")


template= PromptTemplate(
    template="Generate 1 fact about the {topic}" ,
    input_variables=["topic"]
)

parser=StrOutputParser()

chain = template |model |parser

result=chain.invoke({"topic":"moon"})
print(result)

