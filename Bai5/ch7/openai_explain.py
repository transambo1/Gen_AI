from openai import OpenAI

SURROUND = """you are provided with:
1. A Dockerfile enclosed with {{{ DOCKERFILE }}}
2. A line from the file enclosed with {{{ LINE }}}."""
SINGLE_TASK = "Your task is to explain the purpose of the line."

def get_user_prompt(path: str, line: str) -> str:
    with open(path, 'r') as file:
        dockerfile_content = file.read()
    return f"""
    DOCKERFILE: {{{{{{ {dockerfile_content} }}}}}}
    LINE: {{{{{{ {line} }}}}}}
    EXPLANATION:
    """

if __name__ == "__main__":
    # 1. ĐÃ SỬA: Thêm api_key và chỉnh lại lề thẳng hàng
    client = OpenAI(
        api_key="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", 
        base_url="https://api.groq.com/openai/v1"
    )
    
    system_prompt = f"{SURROUND} {SINGLE_TASK}"
    user_prompt = get_user_prompt('ch7/Dockerfile', 'EXPOSE 5000')

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    
    print("\nKết quả giải thích từ OpenAI:\n")
    print(completion.choices[0].message.content)