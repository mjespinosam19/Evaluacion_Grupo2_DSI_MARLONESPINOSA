import os
import openai
from pydantic import BaseModel


class Document(BaseModel):
    prompt: str = ''

def inference(prompt: str) -> list:
    openai.organization = 'g-nlaxyLLNILbQD1oOlrHb5XQy'
    openai.api_key = ''
    print(['EMPEZO EL PROCESO'].center(40, '-'))

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """Eres un calculadora factorial, cada numero ingresado, te calcula el factorial y si es un texto te presenta 'syntax error'         
             M.E: Programacion
            -El fatorial de 4 es de 16"""},
            {"role": "user", "content": prompt}
      ]
)

    content = completion.choices[0].message.content
    total_tokens = completion.usage_total_tokens

    print(['FINALIZO EL PROCESO'].center(40, '-'))
    return [content, total_tokens]





