import openai
from decouple import config

openai.api_key = config("OPENAI_KEY")
start_sequence = "\nA:"
restart_sequence = "\n\nQ: "

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="give me a recipe to make lunch. I have tomatoes, rice, eggs and oninos",
  temperature=0,
  max_tokens=100,
)
print(response.choices[0].text)