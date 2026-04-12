#Runnable is a class 

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

template = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)

model = ChatGroq(model="openai/gpt-oss-120b")

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(template, model, parser),
    'linkedin': RunnableSequence(template2, model, parser)
})

result = parallel_chain.invoke({'topic':'AI'})

print(result['tweet'])
print(result['linkedin'])