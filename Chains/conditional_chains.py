from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.runnables import RunnableParallel,RunnableBranch,RunnableLambda




load_dotenv()
model=ChatGroq(model="openai/gpt-oss-120b")
parser=StrOutputParser()


class Feedback(BaseModel):
    sentiment: Literal["positive","negative"] = Field(description="The sentiment of the feedback, either positive or negative")


parser2 = PydanticOutputParser(pydantic_object=Feedback)

template= PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n{format_instructions}',
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)


# classifier_chain = template | model |parser
#printng the result of the chain of any feedback , would give the sentiment of the feedback
#but the output of the LLM is not controlled by us .
#since the ouptut  returned by it can be in any format and we want it to be in a specific format so that we can use it for further processing
#so we use pydantic

classifier_chain = template | model |parser2

#print(classifier_chain.invoke({'feedback':'This is a wonerful smartphone'}))

#now make the branching , which is used by RunnableBranch
#Branch Chain


template2=PromptTemplate(
    template="Write  an appropriate response to this positive feedback \n {feedback}",
    input_variables=["feedback"]
)

template3=PromptTemplate(
    template="Write  an appropriate response to this negative feedback \n {feedback}",
    input_variables=["feedback"]
)


 #inside tuples of RunnableBranch condition is given , if condition holds , run the chain 
 # x represents the result after this---classifier_chain.invoke({'feedback':'This is a wonerful smartphone'})
 # x-->sentiment='positive'/'negative'


 #RunnableLamda converts lamda function into Runnable , which can be used as chain

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', template2 | model | parser),
    (lambda x:x.sentiment == 'negative', template3 | model | parser),
     RunnableLambda(lambda x: "could not find sentiment")
)
 



final_chain = classifier_chain | branch_chain

result=final_chain.invoke({"feedback":"This is  a terrible phone"})

print(result)

