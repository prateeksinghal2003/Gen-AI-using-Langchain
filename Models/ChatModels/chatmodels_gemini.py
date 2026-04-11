"""1. LLM (Large Language Model)

 This is the brain

Example: Gemini, GPT
It understands + generates text
2. Model

 A specific version of LLM

gemini-2.5-flash = fast model
gpt-4.1 = another model

➡️ Think:
LLM = family
Model = one member

3. API

 A bridge to talk to LLM

You cannot access LLM directly
You send request using API

➡️ Think:
API = phone call to LLM

🔁 Now YOUR CODE FLOW (very easy)
Step 1: Load API key
load_dotenv()

Takes key from .env

GOOGLE_API_KEY = your_key
Step 2: Create model
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

 What happens:

You choose which model (LLM version)
It secretly takes your API key
Step 3: Ask question
result = model.invoke("What is the capital of Germany?")

Flow:

You → LangChain → API → Gemini LLM → Answer
Step 4: Behind the scenes (simple)
Your question goes to LangChain
LangChain adds API key
Sends request to Google (API call)
Gemini (LLM) thinks
Sends answer back

-------------------------------------------------------------------
 temperature controls randomness / creativity of the LLM output.

🎯 Easy understanding
Low temperature (0 – 0.3)
→ Same, predictable answers
→ More accurate / factual
Medium (0.5 – 0.7)
→ Balanced answers
High (0.8 – 1)
→ More creative / random
→ Answers may vary each time
🧠 Example
🔹 temperature = 0

Question: “Write a tagline for a coffee shop”
👉 Output:

Best coffee in town.
🔹 temperature = 0.9

👉 Output:

Awaken your soul with every sip of our magical brew! 


max_completion_tokens (simple)

👉 It controls how long the model’s answer can be
(= maximum number of tokens generated in output)

🧠 What is a token?
1 token ≈ 1 word (roughly)
Example:
"Capital of Germany is Berlin"
≈ 5 tokens

OpenAI → max_tokens
Gemini → max_output_tokens """




#from langchain_openai import ChatOpenAI
""" 1. langchain_google_genai

👉 A Python package (library)

Connects LangChain + Google Gemini (LLM)
Helps you talk to Gemini easily
2. ChatGoogleGenerativeAI

👉 A class (tool)

Used to create and use Gemini model
It handles:
API calls
Request/response
Formatting"""


from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv 

load_dotenv()

#model=ChatOpenAI(model ='gpt-4.1')
#model is an instance of LLM 
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash',max_output_tokens=1000)

result=model.invoke("Tell something about cricket")

print(result.content)