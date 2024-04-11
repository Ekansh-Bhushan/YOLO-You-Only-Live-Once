from openai import OpenAI
import os

client = OpenAI(
#   api_key=os.environ['OPENAI_API_KEY'],  # this is also the default, it can be omitted
  api_key="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"  # this is also the default, it can be omitted
)
chat_completion = openai.ChatCompletion.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)

print(chat_completion)

