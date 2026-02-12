import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()


api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key = api_key)


def chatBot(prompt):
  response = client.chat.completions.create(
    model = "llama-3.3-70b-versatile",
    messages = [{"role":"user","content":prompt}]
  )
  return response.choices[0].message.content.strip()

if __name__ == "__main__":
  while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit","bye"]:
      break
    reply = chatBot(user_input)
    print("Bot: ",reply)