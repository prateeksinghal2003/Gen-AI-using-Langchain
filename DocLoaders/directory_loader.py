from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader


loader=DirectoryLoader(
    path='DocLoaders/books',

    #glob tells which files to load from the directory
    glob='*.pdf',

    #It tells DirectoryLoader which loader to use for each file
    loader_cls=PyPDFLoader
)


#  1. Only .txt files
# loader = DirectoryLoader(
#     path='DocLoaders',
#     glob='*.txt'
# )


#  2. Only .csv files
# loader = DirectoryLoader(
#     path='DocLoaders',
#     glob='*.csv'
# )


#  3. Multiple types (txt + csv)
# loader = DirectoryLoader(
#     path='DocLoaders',
#     glob='*.{txt,csv}'
# )

#  Reads both .txt and .csv

#  4. All files
# loader = DirectoryLoader(
#     path='DocLoaders',
#     glob='**/*'
# )

#  5. Only files in subfolders
# loader = DirectoryLoader(
#     path='DocLoaders',
#     glob='**/*.txt'
# )

#  Reads .txt from all nested folders


docs=loader.load()
print(len(docs))

print(docs[2].page_content)



