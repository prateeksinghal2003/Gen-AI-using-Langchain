from langchain_community.document_loaders import TextLoader

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

loader=TextLoader('DocLoaders/cricket.txt',encoding='utf-8')
docs=loader.load()

# utf-8 is a text encoding format
#  Simple meaning:
#  It tells Python how to read text from file
#  Why needed?
# Files store data in binary (0s and 1s)
# So Python needs to know:
#  “How to convert binary → readable text?”
# That’s what encoding='utf-8' does.


# loader is just a variable (object)
#  It stores an instance of TextLoader
#  Simple meaning:
#  loader = tool that knows how to read your file

#  Flow:
# 1. Create loader
# loader = TextLoader(...)
# No file reading yet 
# Just prepares the loader 

# 2. Load data
# docs = loader.load()
# Now file is actually read 
# Converted into LangChain Document objects

#docs is a list
#each element is a document object 
#print(docs[0].page_content)

load_dotenv()
model=ChatGroq(model="openai/gpt-oss-120b")
parser=StrOutputParser()


template=PromptTemplate(
    template="Write a summary for the poem - \n {poem}",
    input_variables=['poem']
)

chain = template | model | parser
result=chain.invoke({"poem":docs[0].page_content})
print(result)

