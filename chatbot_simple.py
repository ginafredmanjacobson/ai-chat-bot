import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Write an essay about love"}])
print(completion.choices[0].message.content)
