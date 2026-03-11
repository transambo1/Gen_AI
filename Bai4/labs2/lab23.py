from openai import OpenAI

USER_PROMPT = """
Complete the following Python function that calculates the Fibonacci sequence.
"""

SYSTEM_PROMPT = "You are a helpful Python programming assistant."

def get_code_with_instructions(code: str) -> str:
    return code + "\n# Complete this code"

if __name__ == "__main__":

    client = OpenAI(
        api_key="API_KEY_HERE",
        base_url="https://models.inference.ai.azure.com"
    )

    incomplete_code = """
def fibonacci(n):
    # write your code here
"""

    prompt = USER_PROMPT + get_code_with_instructions(incomplete_code)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ]
    )

    output = completion.choices[0].message.content
    print("Suggested Code:")
    print(output)