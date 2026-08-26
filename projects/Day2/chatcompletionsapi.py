#CHAT COMPLETIONS API 

# 1. The simplest way to call an LLM
# 2. It's called Chat Completions because it's saying: "here is a conversation, please predict what should come next"
# 3. The Chat Completions API was invented by OpenAI, but it's so popular that everybody uses it!

import os
from dotenv import load_dotenv 

load_dotenv(override=True)
api_key = os.getenv('GEMINI_API_KEY')


# Check the key

if not api_key:
    print("No Gemini API key was found.")
elif api_key.strip() != api_key:
    print("Gemini API key has spaces or tabs at the beginning or end.")
else:
    print("Gemini API key found and looks good so far!")