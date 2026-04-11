from langchain_google_genai import GoogleGenerativeAIEmbeddings


from dotenv import load_dotenv


from sklearn.metrics.pairwise import cosine_similarity

import numpy as np

load_dotenv()

embedding =  GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

query = 'tell me about bumrah'

# embedding of documents is done
doc_embeddings = embedding.embed_documents(documents)
query_embedding = embedding.embed_query(query)   

scores=cosine_similarity([query_embedding], doc_embeddings)[0]

index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]


print(query)
print(documents[index])
print("similarity score is:", score)



"""🔹 Line 1
scores = cosine_similarity([query_embedding], doc_embeddings)[0]
🧠 What it does

👉 Calculates similarity between query and all documents

🔍 Keyword breakdown
🔸 cosine_similarity(...)

👉 Function from sklearn
👉 Measures how similar two vectors are

Output range: -1 to 1  
1 → very similar  
0 → not related  
🔸 [query_embedding]

👉 Your query vector wrapped in list

❗ Why list?

cosine_similarity expects 2D array

So:

query_embedding → [0.2, 0.5, ...] (1D)  
→ becomes [[0.2, 0.5, ...]] (2D)
🔸 doc_embeddings

👉 List of all document vectors

[
 [0.1, 0.3, ...],   # doc1  
 [0.4, 0.2, ...],   # doc2  
 ...
]
🔸 Output of cosine_similarity
[[0.2, 0.8, 0.5, 0.3, 0.95]]

👉 Similarity of query with each doc

🔸 [0]

👉 Extract first row

[0.2, 0.8, 0.5, 0.3, 0.95]

👉 Final scores

🔹 Line 2
index, score = sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]
🧠 What it does

👉 Finds most similar document

🔍 Keyword breakdown
🔸 enumerate(scores)

👉 Adds index to each score

[(0, 0.2), (1, 0.8), (2, 0.5), (3, 0.3), (4, 0.95)]
🔸 list(...)

👉 Converts to list (optional but used)

🔸 sorted(..., key=lambda x: x[1])

👉 Sorts based on score value

Sorted ascending:
[(0, 0.2), (3, 0.3), (2, 0.5), (1, 0.8), (4, 0.95)]
🔸 lambda x: x[1]

👉 Means:

Sort using second value (score)
🔸 [-1]

👉 Take last element (highest score)

(4, 0.95)
🔸 index, score = ...

👉 Unpacks tuple

index = 4  
score = 0.95 """