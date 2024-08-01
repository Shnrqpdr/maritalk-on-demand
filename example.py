import openai
import os
from dotenv import load_dotenv

load_dotenv()

maritalk_key = os.getenv("MARITALK_KEY")

print(maritalk_key)

client = openai.OpenAI(
  api_key=maritalk_key,
  base_url="https://chat.maritaca.ai/api",   # ** Esta linha de código que foi trocada **
)

messages = [
    { "role": "user", 
      "content": "Você sabe o que é um CNAE?"},
    {
      "role": "assistant",
      "content": "Sim, CNAE significa 'Classificação Nacional de Atividades Econômicas'. É um código utilizado no Brasil para identificar as atividades econômicas de empresas e outras organizações, além de ser utilizado na padronização dos dados sobre os setores econômicos brasileiros. O CNAE é uma ferramenta importante para a administração tributária e outras instituições públicas e privadas, pois facilita a categorização e a análise das atividades econômicas no país."
    },
    {
      "role": "user",
      "content": "O que o CNAE J-60 compreende?"
    }
]

response = client.chat.completions.create(
    model="sabia-2-medium",   # ** Esta linha de código que foi trocada **
    messages=messages,
    temperature=0.7,
    max_tokens=512,
)
answer = response.choices[0].message.content

print(answer)  # Deve imprimir algo como "25 + 27 é 52"