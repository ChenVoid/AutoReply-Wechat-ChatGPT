# coding: utf-8
import openai

import textwrap

openai.api_key = "Your OpenAI API key"


def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-001",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message.strip()


if __name__ == '__main__':
    while True:
        input_message = input("Q: ")
        output_message = generate_response(input_message)
        file = open('test.txt', 'w')
        file.write(output_message)
        file.close()
        print(textwrap.fill(output_message, 100))
