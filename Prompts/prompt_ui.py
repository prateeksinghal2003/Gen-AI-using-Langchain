
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

st.header("Research tool")

#  user_input=st.text_input("Enter your prompt")

# if st.button('Summarize'):
#     result=model.invoke(user_input)
#     st.write(result.content) """


# # after writing this much code, run the streamlit app using the command: streamlit run prompt_ui.py
# """ prompt is given by user and then passed to model  
# this prompt is static prompt since model response is dependent on the prompt given by user.
# it is not a good practice

# so,we will define a template and then pass the user input to the template and then pass the template to the model. 
# this is called dynamic prompt. 
# certain key values would be replaced by the user input and then passed to the model .

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

# creating a template for the prompt using PromptTemplate class from langchain_core.prompts module.
# exp at last 

# template = PromptTemplate(
#     template="Please summarize the research paper titled \"{paper_input}\" with the following specifications:\nExplanation Style: {style_input}  \nExplanation Length: {length_input}  \n1. Mathematical Details:  \n   - Include relevant mathematical equations if present in the paper.  \n   - Explain the mathematical concepts using simple, intuitive code snippets where applicable.  \n2. Analogies:  \n   - Use relatable analogies to simplify complex ideas.  \nIf certain information is not available in the paper, respond with: \"Insufficient information available\" instead of guessing.  \nEnsure the summary is clear, accurate, and aligned with the provided style and length.",

#     input_variables=[
#         "length_input",
#         "paper_input",
#         "style_input"
#     ],
    
# )

# we have created a template for the prompt in prompt_generator.py and then we will save this template in a json file and then we will load this template from the json file and then we will pass the user input to the template and then we will pass the template to the model.

template=load_prompt('template.json') # loading the template from the file where it is saved.


prompt =template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})

if st.button('Summarize'):
    result=model.invoke(prompt)
   
    st.write(result.content)    






""" PromptTemplate allows dynamic prompt creation by defining placeholders that are filled at runtime. 
It helps create reusable and structured prompts for LLMs.


1. template=...

This is the actual prompt text

"Please summarize the research paper titled "{paper_input}" ..."

👉 {paper_input}, {style_input}, {length_input}
are placeholders (variables)

🧠 Meaning
Static part + Dynamic values → Final prompt
🔸 2. input_variables=[...]

👉 List of variables used inside template

input_variables = [
    "length_input",
    "paper_input",
    "style_input"
]

👉 Tells LangChain:

"These values will be filled later"
🔹 Next part
prompt = template.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})
🔍 What happens here?

👉 You fill the template

Example:

If user selects:

paper_input = "BERT"
style_input = "Beginner-Friendly"
length_input = "Short"
Final prompt becomes:
Please summarize the research paper titled "BERT"
Explanation Style: Beginner-Friendly
Explanation Length: Short
...
🔸 template.invoke({...})

👉 Converts:

Template → Final prompt string
🔹 Passing to model
result = model.invoke(prompt)

👉 This sends the final generated prompt to Gemini """
