from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path='DocLoaders/industry_sic.csv')

docs = loader.load()
#for each row , one document object

print(len(docs))
print(docs[1])