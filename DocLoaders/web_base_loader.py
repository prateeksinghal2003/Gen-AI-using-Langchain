from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv


load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

parser = StrOutputParser()

template = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)



url="https://guides.lib.purdue.edu/c.php?g=1371380&p=10135074"
loader=WebBaseLoader(url)

docs=loader.load()

# print(docs[0].page_content)

chain = template|model|parser
result=chain.invoke({'question':'What are the guidelines by IEEE','text':docs[0].page_content})
print(result)