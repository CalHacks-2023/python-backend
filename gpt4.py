import requests
from dotenv import dotenv_values

env = dotenv_values(".env.local")

def gpt4_call(prompt):
    url = 'https://api.openai.com/v1/chat/completions'
    api_key = 'YOUR_OPENAI_API_KEY_HERE'

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }

    payload = {
        'model': 'gpt-4',
        'messages': [{'role': 'user', 'content': '{}'.format(prompt)}],
        'temperature': 0.7
    }

    response = requests.post(url, headers=headers, json=payload)

    data = response.json()
    print(data)

    reply = data['choices'][0]['message']['content']

    return reply


