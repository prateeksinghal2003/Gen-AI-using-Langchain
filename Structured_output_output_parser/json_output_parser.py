from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser

#chain is ues to convert series of steps into a single step, it is used to create a pipeline of prompts and output parsers.

load_dotenv()


model=ChatGroq(model="openai/gpt-oss-120b")

parser=JsonOutputParser()
#format_instructions is used to provide instructions to the model on how to format the output,
#  in this case we are providing instructions to format the output in json format.
# we are saying it partial variable because we are not providing the value of format_instructions at the time of creating the prompt, 
# we will provide it at the time of invoking the prompt.


# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Give me name , age , city of virat kohli \n {format_instructions}',
    input_variables=[],
    partial_variables={'format_instructions':parser.get_format_instructions()} 
)

#can use invoke also
# prompt=template1.format()

# print(prompt)
# result=model.invoke(prompt)
# final_result=parser.parse(result.content)
# print(final_result)


chain = template1 | model | parser
result=chain.invoke({})
print(result)


