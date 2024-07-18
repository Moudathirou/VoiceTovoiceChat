import os

from groq import Groq



def generate_response(prompt):
    
   client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
    )

   chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": prompt,
        }
    ],
    model="llama3-8b-8192",
    temperature=0.7,
    max_tokens=100,
    top_p=1,
    stream=True,
    stop=None,

   )

   response=" "
   for chunk in chat_completion:
      response+=(chunk.choices[0].delta.content or "")

   return response


