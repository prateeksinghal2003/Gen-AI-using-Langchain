from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader


loader=PyPDFLoader('DocLoaders/dl-curriculum.pdf')

#each page  each document object 
docs=loader.load()


# text="""Ethical hacking is the practice of testing systems, networks, and applications to identify security vulnerabilities in a legal and responsible way. Unlike malicious hacking, ethical hackers work with permission to help organizations strengthen their security and protect sensitive data. To get started, you should first build a strong foundation in networking, operating systems (especially Linux), and programming languages like Python. Then, you can learn about common vulnerabilities such as SQL injection and cross-site scripting, and practice using platforms like TryHackMe or Hack The Box. With consistent practice and the right approach, ethical hacking can become a valuable and rewarding skill in the cybersecurity field."""

splitter=CharacterTextSplitter(
    chunk_size=100,

    #between two chunks how many characters are overlapping
    #so that a word is not separated in two chunks
    #number of chunks would increase
    #generally 10-20 % of chunk size
    chunk_overlap=0,
    separator=' '
)


# result=splitter.split_text(text)

#it splits document objects
result=splitter.split_documents(docs)
#print(result)
print(result[0])