from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
#  from  typing import TypedDict
from typing import TypedDict,Annotated,Optional,Literal


model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')



# schema
class Review(TypedDict):

    # summary:str
    # sentimental:str
    # number_of_words:int

    #now we will add description to each field in the schema using Annotated from typing module.
    #so LLM knows what each field means and can generate more accurate output.
     
    # summary:Annotated[str,"A concise summary of the review, capturing the main points and overall sentiment."]
    # sentimental:Annotated[str,"The overall sentiment of the review, categorized as positive, negative, or neutral."]
    # number_of_words:Annotated[int,"The total count of words in the review, providing insight into the length and detail of the feedback."]


    #now add key themes as well to the schema to get more insights from the review.
    key_themes: Annotated[list[str], "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str, "A brief summary of the review"]
    # sentiment: Annotated[str, "Return sentiment of the review either negative, positive or neutral"]
    sentiment: Annotated[Literal["pos", "neg"], "Return sentiment of the review either negative, positive or neutral"]

    #Optional fields are used when we are not sure if the LLM will be able to generate the output for that field or not.
    pros: Annotated[Optional[list[str]], "Write down all the pros inside a list"]
    cons: Annotated[Optional[list[str]], "Write down all the cons inside a list"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]

structured_model=model.with_structured_output(Review)    
result=structured_model.invoke("The hardware is great, but the software feels bloated.There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.")

print(result)