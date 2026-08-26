import os
from dotenv import load_dotenv
from scraper import fetch_website_contents
from openai import OpenAI
from IPython.display import Markdown, display
 
#Google Gemini models - gemini-2.5-flash, gemini-2.5-flash-lite, gemini-3.5-flash, gemini-3.5-flash-lite, gemini-4.0-flash, gemini-4.0-flash-lite

# Load environment variables from .env
load_dotenv(override=True)
api_key = os.getenv("GEMINI_API_KEY")


# Check the key
if not api_key:
    print("No Gemini API key was found.")
elif api_key.strip() != api_key:
    print("Gemini API key has spaces or tabs at the beginning or end.")
else:
    print("Gemini API key found and looks good so far!")


# Create Gemini client using the OpenAI-compatible API
openai = OpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)


# Send a message to Gemini
message = "Hello, Gemini! This is my first ever message to you! Hi!"
messages = [
    {
        "role": "user",
        "content": message
    }
]

response = openai.chat.completions.create( model="gemini-3.5-flash-lite",messages=messages )

print(response.choices[0].message.content)


# Let's try out this utility - getting content from the website
web = fetch_website_contents("https://www.w3schools.com/python/python_decorators.asp")
print(web) 



# Define our system prompt - you can experiment with this later, changing the last sentence to 'Respond in markdown in Spanish."
system_prompt = """
You are a snarky assistant that analyzes the contents of a website,
and provides a short, snarky, humorous summary, ignoring text that might be navigation related.
Respond in markdown. Do not wrap the markdown in a code block - respond just with the markdown.
""" 

# Define our user prompt
user_prompt_prefix = """
Here are the contents of a website.
Provide a short summary of this website.
If it includes news or announcements, then summarize these too.
""" 

messages = [
    {"role": "system", "content": "You are a snarky assistant"},
    {"role": "user", "content": "What is 2 + 2?"}
]

response = openai.chat.completions.create(model="gemini-3.5-flash-lite", messages=messages)
print(response.choices[0].message.content) 

# See how this function creates exactly the format above
def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_prefix + website}
    ]

# Try this out, and then try for a few more websites
print(messages_for(web)) 


# And now: call the Gemini API. You will get very familiar with this!

def summarize(url):
    website = fetch_website_contents(url)
    response = openai.chat.completions.create(
        model="gemini-3.5-flash-lite",
        messages = messages_for(website)
    )
    return response.choices[0].message.content 

print(summarize("https://www.geeksforgeeks.org/python/python-oops-concepts"))  

#FUN Task 

# Step 1: Create your prompts

system_prompt = """
You are a hilariously snarky email-summary assistant. Summarize the email briefly in markdown, focusing only on the important announcement and key details. Add a little playful humor, but keep the summary clear and professional enough to understand. Do not invent facts.
"""

user_prompt = """
    Dear JayaKaviya,

Congratulations! 🎉 We are delighted to share that you have been selected by Apple for the Software Development Engineer (SDE) position.

This is a fantastic achievement and a well-deserved recognition of your skills and hard work. Looks like Apple decided they needed some extra coding power! 🍎💻

Wishing you great success in your new role at Apple. May your code compile on the first try and your bugs be few!

Best wishes,
Congratulations once again!

"""

# Step 2: Make the messages list

messages = [
    { "role":"system", "content" : system_prompt },
    { "role":"user", "content" : user_prompt }
    ] 

# Step 3: Call OpenAI
response = openai.chat.completions.create(model="gemini-3.5-flash-lite", messages=messages)
# Step 4: print the result
print(response.choices[0].message.content)