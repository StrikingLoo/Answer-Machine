# Answer Machine
A simple wrapper for the GPT-3 API. It comes with a few prompt formats that get nice answers.

## Before Using

```
pip3 install openai
export OPENAI_API_KEY=$YOUR_KEY
```

## Example Usage

`python3 complete-prompt.py 1 'What were the greatest technological achievements of the Ottoman Empire?'`

### Modes

- 1: Question (provide a question as prompt, obtain an answer).
- 2: Explanation (provide a topic or question, the prompt asks for a summary/explanation as an essay).
- 3: Tutorial (a tutorial for solving a problem. Uses the 'thinking step-by-step' trick). 
