import requests

url = "http://localhost:11434/api/generate"

# CASE 1: Model gốc
prompt1 = "Write a Python function to solve quadratic equation ax^2 + bx + c = 0"

response1 = requests.post(url, json={
    "model": "phi3",
    "prompt": prompt1,
    "stream": False
})

print("=== CASE 1: MODEL GỐC ===")
print(response1.json()["response"])


# CASE 2: Giả lập fine-tune
prompt2 = """You are a coding assistant. Only return code. No explanation. No comments.

FUNCTION: def solve_quadratic(a, b, c)
CODE:
"""

response2 = requests.post(url, json={
    "model": "phi3",
    "prompt": prompt2,
    "stream": False
})

print("\n=== CASE 2: AFTER FINE-TUNE ===")
print(response2.json()["response"])