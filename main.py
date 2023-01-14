#!/usr/local/bin/python

import os
import openai
import json
import argparse, sys
import logging
# from datetime import datetime
import uuid

id = uuid.uuid4()

# Modified from: https://stackoverflow.com/a/17558764/5079258
extra = {'id': id}
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(id)s - %(message)s',  '%m/%d/%Y %I:%M:%S %p')
logger.setLevel(logging.DEBUG)
fileHandler = logging.FileHandler('chatgpt.log')
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger = logging.LoggerAdapter(logger, extra)

logger.info("Starting...")

parser=argparse.ArgumentParser()

parser.add_argument("--prompt", help="Prompt")
parser.add_argument("--temp", help="Temperature", type=int, default=0.9)
parser.add_argument("--maxTokens", help="Max tokens", type=int, default=48)

args=parser.parse_args()

openai.api_key_path = "./openai_api_key"

if args.prompt:
  prompt = args.prompt
else:  
  prompt = input("Enter prompt: ")

logger.info(f"Prompt: {prompt} - Temperature: {args.temp} - Max tokens: {args.maxTokens}")

response = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt,
  temperature=args.temp,
  max_tokens=args.maxTokens
)

textResponse = response.choices[0].text.strip()

logger.info(f"Response: {textResponse}")
print(textResponse)

prompt_tokens = response.usage.prompt_tokens
completion_tokens = response.usage.completion_tokens
total_tokens = response.usage.total_tokens

print("\n---\n")

usageLog = f"Token usage - Prompt: {prompt_tokens} - Completion: {completion_tokens} - Total: {total_tokens}"

logger.info(usageLog)
print(usageLog)

logger.info("Done.")