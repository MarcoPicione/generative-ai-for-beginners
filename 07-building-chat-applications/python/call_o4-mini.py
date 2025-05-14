import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
  azure_endpoint = os.environ["AZURE_OPENAI_ENDPOINT"], 
  api_key=os.environ['AZURE_OPENAI_API_KEY'],  
  api_version = os.environ["AZURE_OPENAI_API_VERSION"]
  )

"""
endpoint = "https://generativeaicoursepicione.openai.azure.com/"
model_name = "o4-mini"
deployment = "o4-mini"

subscription_key = "<your-api-key>"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)
"""

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?",
        }
    ],
    max_completion_tokens=10000,
    model=os.environ["AZURE_OPENAI_DEPLOYMENT"]
)

print(response.choices[0].message.content)