from openai import OpenAI

# 1. Khởi tạo kết nối với Groq (Dùng lại key cũ của bạn)
client = OpenAI(
    api_key=("GROQ_API_KEY"), 
    base_url="https://api.groq.com/openai/v1"
)

# 2. Định nghĩa vai trò của AI
system_prompt = "You are a Python refactoring tool. Format the given code to include Type Hints and standard Docstrings. Strictly return ONLY the Python code, nothing else."

# 3. KỸ THUẬT FEW-SHOT: Đưa ví dụ mẫu vào để AI bắt chước
messages = [
    {"role": "system", "content": system_prompt},
    
    # --- VÍ DỤ MẪU 1 ---
    {"role": "user", "content": "def add(a, b):\n    return a + b"},
    {"role": "assistant", "content": 'def add(a: int, b: int) -> int:\n    """Adds two integers."""\n    return a + b'},
    
    # --- TÁC VỤ THỰC TẾ (AI sẽ nhìn ví dụ trên để làm cái này) ---
    {"role": "user", "content": "def calculate_discount(price, discount_percent):\n    return price - (price * discount_percent / 100)"}
]

# 4. Gọi AI xử lý
print("Đang gửi code tới AI để định dạng theo phương pháp Few-Shot...\n")
completion = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=messages,
    temperature=0.1
)

print("=== KẾT QUẢ TỪ AI ===")
print(completion.choices[0].message.content)