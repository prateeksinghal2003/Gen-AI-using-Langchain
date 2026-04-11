from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableParallel
#it used to run multiple chains in parallel

load_dotenv()
model=ChatGroq(model="openai/gpt-oss-120b")
parser=StrOutputParser()
model2=ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

# Use \n when you want:
# not mandatory
# Better formatting
# Clean prompts for LLM
# Separation between instruction & input

template=PromptTemplate(
    template="Generate short and simple notes for \n {text}",
    input_variables=["text"]
)

template2=PromptTemplate(
    template="Generate 5 short and simple questions based on the  \n {text}",
    input_variables=["text"]
)

template3=PromptTemplate(
    template="Merge the provided notes and questions into a single text. \n Notes: {notes} \n Questions: {questions}",
    input_variables=["notes","questions"]
)


#parallel chain is made with the help of RunnableParallel

parallel_chain = RunnableParallel(
    {
        "notes": template | model | parser,
        "questions" : template2 | model2 | parser
    }
)


#merging chain 
merge_chain = template3 | model | parser

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""


chain = parallel_chain | merge_chain

result=chain.invoke({"text":text})
print(result)





