from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()
model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')




# chat_template=ChatPromptTemplate(
#     [SystemMessage(content="You are a helpful {domain} assistant."),
#      HumanMessage(content="Explain the concept of {concept} in simple terms."),
#     ]
# )

chat_template=ChatPromptTemplate(
    [
        ('system','You are a helpful {domain} assistant.'),
        ('human','Explain the concept of {concept} in simple terms.'),  
    ]
)

prompt=chat_template.invoke({
    'domain':'physics',
    'concept':'newton laws of motion'
})

print(prompt)

