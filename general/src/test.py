from dotenv import load_dotenv
import os
import openai

load_dotenv()

en_txt= "Hello, how are you?"

response= openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content": "You are helpful assistant."},
        {"role": "user", "content": f'Translate the following English text to French: "{en_txt}"'}
    ],
)

print(response.choices[0].message.content)