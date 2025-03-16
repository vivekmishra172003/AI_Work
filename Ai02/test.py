from langchain_openai import OpenAI
from decouple import config
Secret_key = config('OPENAI_API_KEY')
llm = OpenAI(openai_api_key=Secret_key)
response = llm.invoke("Who is prime minister of india?")
print(response)