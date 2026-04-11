from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

#from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema

#chain is ues to convert series of steps into a single step, it is used to create a pipeline of prompts and output parsers.

load_dotenv()


model=ChatGroq(model="openai/gpt-oss-120b")

#create a schema 

schema = [
    ResponseSchema(name='fact_1',description='fact about topic'),
     ResponseSchema(name='fact_1',description='fact about topic'),
      ResponseSchema(name='fact_1',description='fact about topic'),
]


#create a parser
parser =   StructuredOutputParser.from_response_schemas(schema)

template1=PromptTemplate(
    template='Give me 3 facts about {topic} \n {format_instructions}',
    input_variables=['topic'],
    partial_variables={'format_instructions':parser.get_format_instructions()}
)


prompt = template1.invoke({'topic':"Black Hole"})


result=model.invoke(prompt)
final_result=parser.parse(result.content)
print(final_result)




