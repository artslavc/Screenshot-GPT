from g4f.client import Client

def neiro_zapros(message_text, type):
    print("! Идет Генерация...")

    client = Client()

    response = client.chat.completions.create(
        model="gemini-1.5-pro",
        messages=[{"role": "user", "content": 'Ответь на русском RUSSIA. ' + type + f' {message_text}'}],
    )
    return response.choices[0].message.content