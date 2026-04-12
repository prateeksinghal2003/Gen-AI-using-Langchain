
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence

load_dotenv()

template = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

model=ChatGroq(model="openai/gpt-oss-120b")

parser = StrOutputParser()

template2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

chain = RunnableSequence(template, model, parser, template2, model, parser)

print(chain.invoke({'topic':'AI'}))