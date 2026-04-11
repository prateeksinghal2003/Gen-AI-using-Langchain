#message placeholder is a placeholder for the set of messages that are passes to the model to provide the context of the conversation 
# and to provide you with a relevant response.
#MessagesPlaceholder = inject past chat into prompt dynamically

from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder


# create a chat template
chat_template=ChatPromptTemplate([
    ('system','You are a helpful customer support agent.'),
      MessagesPlaceholder(variable_name='chat_history'),
     ('human','{query}')
])

chat_history = []
# load chat history
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)


#create prompt
prompt = chat_template.invoke({'chat_history':chat_history, 'query':'Where is my refund'})

print(prompt)


# What does 'system', 'human', 'ai' mean?

# These are called roles in a chat.

# ('system', '...')
# ('human', '...')
# ('ai', '...')

# They tell the model who is speaking

#  Meaning of each
#  'system'
# ('system', 'You are a helpful assistant')

#  Sets behavior / rules of AI

# tone
# style
# personality

# ✔ Example:
# "Be short", "Explain simply", "Act like teacher"

#  'human'
# ('human', '{query}')

#  Represents user input

#  'ai'
# ('ai', 'Previous response')

#  Represents AI’s previous reply (used in history)

#  Why are they important?

#  LLM works like a conversation

# Without roles:
#  Model gets confused
#  With roles:

# knows who asked
# knows how to respond
# maintains context
#  Is it compulsory to write them?
#  Short Answer:

#  Yes (recommended) in chat-based models