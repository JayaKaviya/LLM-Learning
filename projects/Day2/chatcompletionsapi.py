# Raw REST API Approach (Using requests)

import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv(override=True)
api_key = os.getenv("GEMINI_API_KEY")

# -------------------------------------------------------------------
# 1. Check API Key Validation
# -------------------------------------------------------------------
if not api_key:
    print("No Gemini API key was found.")
elif api_key.strip() != api_key:
    print("Gemini API key has spaces or tabs at the beginning or end.")
else:
    print("Gemini API key found and looks good so far!")

# -------------------------------------------------------------------
# 2. OpenAI Chat Completions Example (Commented Out for Reference)
# -------------------------------------------------------------------
# # gpt-4o-mini is OpenAI code, commented out to avoid costs/errors:
#
# headers = {
#     "Authorization": f"Bearer {api_key}",
#     "Content-Type": "application/json"
# }
#
# payload = {
#     "model": "gpt-4o-mini",
#     "messages": [
#         {"role": "user", "content": "Tell me a fun fact"}
#     ]
# }
#
# response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
# print(response.json()["choices"][0]["message"]["content"])

# -------------------------------------------------------------------
# 3. Native Gemini REST API Call

# APPROACH 1: RAW REST API
# Python requests -> Google Gemini API -> Gemini Response

# -------------------------------------------------------------------
# Gemini uses Content-Type header only (key is passed in URL)
headers = {
    "Content-Type": "application/json"
}

# Gemini uses contents → parts instead of OpenAI's messages array
payload = {
    "contents": [
        {
            "parts": [
                {"text": "Tell me a fun fact"}
            ]
        }
    ]
}

print("Payload:", payload)

# Execute HTTP POST request passing API Key in the URL query parameter
response = requests.post(
    f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}",
    headers=headers,
    json=payload
)

# Print raw JSON output
print(response.json())

# OpenAI extraction style (commented out):
# print(response.json()["choices"][0]["message"]["content"]) 

# Gemini extraction style:
print(response.json()["candidates"][0]["content"]["parts"][0]["text"]) 

#------------------------------------------------------------------------------------------------------------------------------

# 1.USING Open ai - You have an existing app built for OpenAI and want to swap models to Gemini with minimal code changes.
# APPROACH 2: OPENAI-COMPATIBLE GEMINI
# OpenAI SDK -> Google's Gemini Endpoint -> Gemini Response


from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[{"role": "user", "content": "Hello!"}]
)

print(response.choices[0].message.content)



# 2.Google Gen AI SDK Approach (Recommended)  - for Gemini alone
# APPROACH 3: OFFICIAL GEMINI SDK
# Google Gen AI SDK -> Google Gemini API -> Gemini Response

import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv(override=True)

# Initialize the client (automatically reads GEMINI_API_KEY from environment)
client = genai.Client()

message = "Hello, Tell me a fun fact"

# Generate response using official SDK
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=message,
)

print("FUN FACT : ", response.text) 


#----------------------------------------------------------------------------------------------------------------------------------------------- 
# APPROACH 4: OLLAMA
# Python + OpenAI SDK -> Local Ollama Server -> Llama / DeepSeek Response

import ollama


# -------------------------------------------------------------------
# 1. Health Check (Verify Ollama is running)
# -------------------------------------------------------------------
try:
    health_check = requests.get("http://localhost:11434")
    print("Ollama Server Status:", health_check.text.strip())
except requests.exceptions.ConnectionError:
    print("Error: Ollama server is not running. Please start Ollama first.")
    exit(1)

# -------------------------------------------------------------------
# 2. Pull & Run Llama 3.2 using OpenAI Compatibility Layer
# -------------------------------------------------------------------
print("\n--- Pulling llama3.2:1b ---")
ollama.pull("llama3.2:1b")  #

OLLAMA_BASE_URL = "http://localhost:11434/v1"
client = OpenAI(base_url=OLLAMA_BASE_URL, api_key="ollama")

print("\n--- Generating Fun Fact (Llama 3.2) ---")
response = client.chat.completions.create(
    model="llama3.2:1b",
    messages=[{"role": "user", "content": "Tell me a fun fact"}]
)
print( "Llama fun fact : ",response.choices[0].message.content)

# -------------------------------------------------------------------
# 3. Pull & Run DeepSeek R1
# -------------------------------------------------------------------
print("\n--- Pulling deepseek-r1:1.5b ---")
ollama.pull("deepseek-r1:1.5b")  #

print("\n--- Generating Fun Fact (DeepSeek R1) ---")
response_ds = client.chat.completions.create(
    model="deepseek-r1:1.5b",
    messages=[{"role": "user", "content": "Tell me a fun fact"}]
)
print("DeepSeek fun fact : ", response_ds.choices[0].message.content)