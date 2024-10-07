#!/bin/bash
import os
#import openai
import pyjokes

os.system("clear")

# openai.api_key = "Bob"

# def generate_ai_joke():
#     respones =openai.Completion.create(
#         engine = "text-davinci-003",
#         prompt = "Give me a joke",
#         max_tokens = 50
#     )
#     return respones.choices[0].text.strip()

# print(generate_ai_joke())

#get_joke(en, netural)
print (pyjokes.get_joke("en", "neutral"))
