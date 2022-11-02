import os
import argparse
import openai
import sys

SMART_QUESTION_PREAMBLE = 'The following is a dialogue where a very intelligent artificial intelligence answers questions truthfully and to the best of its abilities. Q: %s A:'
SMART_EXPLANATION_PREAMBLE = 'The following is a short essay by a very intelligent artificial intelligence who explains and summarizes, truthfully and to the best of his abilities, the following topic. Topic: %s'
TUTORIAL_PREAMBLE = 'The following is a tutorial where a very intelligent person explains how to solve a problem. Problem: %s Solution: Let\'s think step by step.'

def format_prompt(mode, prompt):
  if mode == 1:
    return SMART_QUESTION_PREAMBLE % prompt
  elif mode == 2:
    return SMART_EXPLANATION_PREAMBLE % prompt
  elif mode == 3:
    return TUTORIAL_PREAMBLE % prompt
  else:
    return prompt

def request_completion(final_prompt, model_name = "text-davinci-002", temperature=.7):
  openai.api_key = os.getenv("OPENAI_API_KEY")

  response = openai.Completion.create(
    model=model_name,
    prompt=final_prompt,
    temperature=temperature,
    max_tokens=512,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  return response

def answer_prompt(mode, request_prompt):
  final_prompt = format_prompt(mode, request_prompt)
  print(final_prompt)
  response = request_completion(final_prompt)
  answer_text = response['choices'][0]['text']
  return answer_text

parser = argparse.ArgumentParser(
                    prog = 'Answer Machine',
                    description = 'Wrapper around GPT-3 API. Get answers to questions, explanations and more.',
                    epilog = 'Usage:\npython complete-prompt.py $MODE $PROMPT\nModes: \n1 - QUESTION\n2 - EXPLANATION\n3 - TUTORIAL')

parser.add_argument('mode', metavar='mode', type=int,
                    help='Prompt mode. An int from 0 to 3 (0 for free prompt).')
parser.add_argument('prompt', help="A text prompt for GPT-3")

args = parser.parse_args()
mode = args.mode
request_prompt = args.prompt
final_answer = answer_prompt(mode, request_prompt)
print(final_answer)