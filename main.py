#!/usr/local/bin/python

import os
import openai
import json
import argparse, sys

parser=argparse.ArgumentParser()

parser.add_argument("prompt", help="ChatGPT Prompt")
parser.add_argument("--temp", help="Temperature", default=0.9)
parser.add_argument("--maxTokens", help="Max tokens", default=48)

args=parser.parse_args()

openai.api_key_path = "./openai_api_key"

if args.prompt:
  prompt = args.prompt
else:  
  prompt = input("Enter prompt: ")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=args.temp,
  max_tokens=args.maxTokens
)

print(response.choices[0].text.strip())