from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableBranch, RunnableLambda

load_dotenv()

template = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)
model = ChatGroq(model="openai/gpt-oss-120b")

parser = StrOutputParser()

report_gen_chain =RunnableSequence(template,model,parser)

branch_chain = RunnableBranch(

    #if this condition is true execute after colon (:) part
    #Pipe is just a cleaner way to write RunnableSequence
    (lambda x: len(x.split())>300, template2 | model | parser),

    #this is the default condition, which must be passed
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))
    

