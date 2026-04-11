from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

#chain is ues to convert series of steps into a single step, it is used to create a pipeline of prompts and output parsers.

load_dotenv()


model=ChatGroq(model="openai/gpt-oss-120b")

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 2 line summary on the following text. /n {text}',
    input_variables=['text']
)


#creating an output parser
parser=StrOutputParser()

#parser is used to convert the output of the model into a specific format, in this case we are converting the output into a string format.
#parser is used with chain 
chain = template1 | model | parser | template2 | model | parser

result=chain.invoke({'topic':"Black Hole"})

print(result)