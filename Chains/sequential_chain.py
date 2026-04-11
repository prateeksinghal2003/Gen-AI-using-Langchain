from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
model=ChatGroq(model="openai/gpt-oss-120b")
parser=StrOutputParser()


template=PromptTemplate(
    template="Generate 10 lines for the {topic}",
    input_variables=["topic"]
)

template2=PromptTemplate(
    template ="Summarize the following text in 1 line: {text}",
    input_variables=["text"]
)

chain = template | model | parser | template2 | model | parser

result=chain.invoke({"topic":"sun"})
print(result)

