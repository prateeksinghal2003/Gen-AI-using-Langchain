#embedding models are used for semantic search

#from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings


from dotenv import load_dotenv

load_dotenv()

# embedding_model = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)
embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

result=embedding_model.embed_query("Delhi is the capital of India")
print(str(result))

