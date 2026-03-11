from openai import OpenAI

client = OpenAI(
    api_key="API_KEY_HERE",
    base_url="https://models.inference.ai.azure.com"
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": "Explain the FizzBuzz problem"}
    ]
)

print(response.choices[0].message.content)