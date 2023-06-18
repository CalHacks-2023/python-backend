import os
import openai
import requests

def gpt4_call(prompt):
    url = 'https://api.openai.com/v1/chat/completions'
    api_key = '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'

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

    reply = data['choices'][0]['message']['content']

    return reply


