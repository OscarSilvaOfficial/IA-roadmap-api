import openai, os
from dotenv import load_dotenv

load_dotenv() 

class IAService:
  def __init__(self) -> None:
    pass
  
  def create_roadmap(self, topic):
    openai.api_key = os.getenv('API_KEY')

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "user", "content": f"Poderia gerar um roadmap para {topic}"},
      ]
    )

    choices = response['choices']

    answers = choices[0]['message']['content'].split('\n\n')
    return answers #[1: -1]