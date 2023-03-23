import openai
import json
import os

from .post_generation_gpt_prompt import post_generation_gpt_prompt

openai.api_key = os.getenv("OPENAI_API_KEY")

def parse_generated_posts(posts_text):
  try:
    return json.loads(posts_text.replace('\n', ''))
  except json.JSONDecodeError as e:
    print("Error: Unable to parse the generated posts JSON string.")
    return None

def generate_posts(topic, model="gpt-3.5-turbo"):
  response = openai.ChatCompletion.create(
    model=model,
    messages=[
      *post_generation_gpt_prompt,
      {
        "role": "user",
        "content": f"Generate me some posts with a theme contained in the context of \"{topic}\"."
      },
    ],
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.85,
  )

  return parse_generated_posts(response.choices[0].message.content.strip())
