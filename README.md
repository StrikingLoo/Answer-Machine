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

- 0: Free prompt. Request a raw prompt.
- 1: Question (provide a question as prompt, obtain an answer).
- 2: Explanation (provide a topic or question, the prompt asks for a summary/explanation as an essay).
- 3: Tutorial (a tutorial for solving a problem. Uses the 'thinking step-by-step' trick). 

### Sample Outputs

```
complete.sh 0 'Convert the following text to JSON: "Anne is a female biology student who loves sushi and plays golf". JSON:'

Convert the following text to JSON: "Anne is a female biology student who loves sushi and plays golf". JSON:

{
	"name": "Anne",
	"gender": "female",
	"study": "biology",
	"hobbies": ["sushi", "golf"]
}

```

---

```
complete.sh 0 'Write a bulleted outline for an essay explaining the importance of Babylonian civilization to the current Western society. Outline:'
Write a bulleted outline for an essay explaining the importance of Babylonian civilization to the current Western society. Outline:


-Babylonian civilization is one of the oldest in the world, dating back to around 3000 BCE.

-Babylonian culture had a significant impact on the development of the Western world, particularly in the areas of law, religion, and science.

-Babylonian law was the first to codify the rules of conduct in a society, setting a precedent that would be followed by later cultures.

-Babylonian religion was influential in the development of Judaism and Christianity, two of the major religions of the Western world.

-Babylonian science was ahead of its time, making significant contributions to our understanding of astronomy, mathematics, and medicine.
```
