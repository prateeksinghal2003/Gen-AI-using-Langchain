# from langchain_openai import OpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings


from dotenv import load_dotenv

load_dotenv()

#embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions=32)
embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

result = embedding_model.embed_documents(documents)

print(str(result))