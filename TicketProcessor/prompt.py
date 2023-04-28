import openai
import os

openai.api_key = os.getenv("OPEN_AI_KEY")

def processUserQuery(userQuery):
    query= userQuery

    response= openai.Completion.create(engine="text-davinci-001", 
                                    prompt=query, max_tokens=50)  
    return response