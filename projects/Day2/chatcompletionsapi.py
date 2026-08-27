#CHAT COMPLETIONS API 

# 1. The simplest way to call an LLM
# 2. It's called Chat Completions because it's saying: "here is a conversation, please predict what should come next"
# 3. The Chat Completions API was invented by OpenAI, but it's so popular that everybody uses it!

import os
from dotenv import load_dotenv 
import requests

load_dotenv(override=True)
api_key = os.getenv('GEMINI_API_KEY')


# Check the key

if not api_key:
    print("No Gemini API key was found.")
elif api_key.strip() != api_key:
    print("Gemini API key has spaces or tabs at the beginning or end.")
else:
    print("Gemini API key found and looks good so far!") 
    
    



# #gpt-5-nano is openai, the below code is openai , it costs so using gemini model 

# import requests

# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }

# payload = {
#     "model": "gpt-4o-mini",
#     "messages": [
#         {"role": "user", "content": "Tell me a fun fact"}
#     ]
# }

# response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
# print(response.json()["choices"][0]["message"]["content"])





# Gemini uses the API key in the URL
headers = {
    "Content-Type": "application/json"
}

# Gemini uses contents → parts instead of messages
payload = {
    "contents": [{
            "parts": [
                {"text": "Tell me a fun fact"}
            ]
        }
    ]
}

print("Payload:", payload) 

response = requests.post(
    f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}",
    headers=headers,
    json=payload
)

print(response.json())
#openai
# print(response.json()["choices"][0]["message"]["content"]) 

#gemini
print(response.json()["candidates"][0]["content"]["parts"][0]["text"])