import openai

openai.api_key = "sk-proj-i5z0zxbb6Ff6pcD73r4dT3BlbkFJRqsSSy7iUmsCHJGiunDC"  # Add your OpenAI API key here

def generate_description(input):
    messages = [
        {"role": "user",
         "content": """As a Product Description Generator, Generate multi paragraph rich text product description with emojis from the information provided to you' \n"""},
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply
