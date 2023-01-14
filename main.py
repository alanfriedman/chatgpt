#!/usr/local/bin/python

import os
import openai
import json
import argparse, sys
import logging
import uuid

scriptPath = os.path.realpath(__file__)
scriptDir = os.path.dirname(scriptPath)

logFile = os.path.join(scriptDir, 'chatgpt.log')

id = uuid.uuid4()

# Modified from: https://stackoverflow.com/a/17558764/5079258
extra = {'id': id}
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(asctime)s - %(id)s - %(message)s',  '%m/%d/%Y %I:%M:%S %p')
logger.setLevel(logging.DEBUG)
fileHandler = logging.FileHandler(logFile)
fileHandler.setFormatter(formatter)
logger.addHandler(fileHandler)
logger = logging.LoggerAdapter(logger, extra)

logger.info("Starting...")

parser=argparse.ArgumentParser()

parser.add_argument("--prompt", help="Prompt")
parser.add_argument("--temp", help="Temperature", type=int, default=0.9)
parser.add_argument("--maxTokens", help="Max tokens", type=int, default=48)

args=parser.parse_args()

keyFile = os.path.join(scriptDir, 'openai_api_key')

openai.api_key_path = keyFile

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