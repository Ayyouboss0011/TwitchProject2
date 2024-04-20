from openai import OpenAI

def api_call(prompt):
  client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

  completion = client.chat.completions.create(
    model="local-model", # this field is currently unused
    messages=[
      {"role": "system", "content": prompt},
      {"role": "user", "content": "write a very short chat message without any quotes """}
    ],
    temperature=0.7,
  )
  #print(completion.choices[0].message)
  return completion.choices[0].message.content
