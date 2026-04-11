#chatbot code using langchain-google-genai
# API Key = your identity (who you are)
# 👉 Model = the service you want to use (what you use)


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

# model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')
#model=ChatGoogleGenerativeAI(model='gemini-2.5-flash-preview-tts')
model=ChatGroq(model="openai/gpt-oss-120b")
#System message is used to set the context of the conversation and to provide instructions to the model.
# Human message is used to represent the message of the user and AI message is used to represent the message of the assistant.


chathistroy=[
     SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input=input('You:')
    # chathistroy.append(user_input)
    chathistroy.append(HumanMessage(content=user_input)) 

    if user_input.lower() == "exit":
        break

    # result=model.invoke(user_input)
    result=model.invoke(chathistroy) # passing the chat history to the model so that it can understand
    # the context of the conversation and provide you with a relevant response.

    chathistroy.append(AIMessage(content=result.content)) 

    print("AI:", result.content)

print(chathistroy)    

# ''' This much code is enough to create a chatbot using langchain-google-genai.
#      but the problem is that it will give you a very generic response. 
#      It will not be able to understand the context of the conversation and will not be able to provide you with a relevant response.
#      like which one is greater 2 or 5, AI answers 5 , then i ask multiply the geater number by 2, it will not be able to understand 
#      that the greater number is 5 and it will give you a generic response like 10x.'''
#    so create chat history 

# chat history list is created to store the messages of the conversation between the user and the AI.
# but it does not store who has send  what message , so later on it becomes difficult for the model to understand 
# the context of the conversation and provide you with a relevant response.
# so we can store the messages in the form of a dictionary with two keys 'role' and   
# 'content' where 'role' can be 'user' or 'assistant' and 'content' is the message of the user or the assistant.
# this problem is solved by langchain 



