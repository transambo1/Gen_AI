import inspect

SURROUND = """
You are an expert Python developer.
Generate high-quality documentation for Python functions.
"""

SINGLE_TASK = """
Generate a Google-style Python docstring for the function below.
Return only the docstring.
"""

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def get_user_prompt(func: callable) -> str:
    source = inspect.getsource(func)
    prompt = f"""
{SINGLE_TASK}

Function code:
{source}
"""
    return prompt


if __name__ == "__main__":
    from openai import OpenAI
    from openai.types.chat import ChatCompletion

    # Dùng máy chủ ảo của GitHub để gọi gpt-4o-mini hoàn toàn miễn phí
    client: OpenAI = OpenAI(
        base_url="https://models.inference.ai.azure.com",
        api_key="api_key="da-xoa-key-de-bao-mat"" 
    )

    completion: ChatCompletion = client.chat.completions.create(
        model="gpt-4o-mini", # Quay trở lại dùng đúng model của đề bài
        messages=[
            {"role": "system", "content": SURROUND},
            {"role": "user", "content": get_user_prompt(recursive_fibonacci)},
        ],
    )

    print("Docstring:")
    print(completion.choices[0].message.content)