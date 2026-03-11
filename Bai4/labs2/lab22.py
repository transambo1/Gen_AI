from openai import OpenAI

client = OpenAI(
    api_key="API_KEY_HERE",
    base_url="https://models.inference.ai.azure.com"
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful programming tutor."},
        {"role": "user", "content": "What is recursion?"},
        {"role": "user", "content": "Give a simple example in Python."}
    ]
)

print(response.choices[0].message.content)