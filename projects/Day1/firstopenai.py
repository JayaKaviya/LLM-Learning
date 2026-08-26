import os
from dotenv import load_dotenv
# from scraper import fetch_website_contents
from IPython.display import Markdown, display
from openai import OpenAI

from projects.scraper import fetch_website_contents 


# Load environment variables in a file called .env

load_dotenv(override=True)
api_key = os.getenv('OPENAI_API_KEY')


# Check the key

if not api_key:
    print("No API key was found - please head over to the troubleshooting notebook in this folder to identify & fix!")
elif not api_key.startswith("sk-proj-"):
    print("An API key was found, but it doesn't start sk-proj-; please check you're using the right key - see troubleshooting notebook")
elif api_key.strip() != api_key:
    print("An API key was found, but it looks like it might have space or tab characters at the start or end - please remove them - see troubleshooting notebook")
else:
    print("API key found and looks good so far!") 
    
    
# To give you a preview -- calling OpenAI with these messages 
#Openai key is not free to access
   
message = "Hello, GPT! This is my first ever message to you! Hi!"
messages = [{"role": "user", "content": message}]
openai = OpenAI()
response = openai.chat.completions.create(
    model="gpt-5-nano",
    messages=messages
)
print(response.choices[0].message.content)
 
 
# Let's try out this utility

ed = fetch_website_contents("https://aivorajk.vercel.app")
print(ed)