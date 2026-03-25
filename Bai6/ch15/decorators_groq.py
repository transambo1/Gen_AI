from groq import Groq

# 1. Dán mã API Key của Groq vào đây
client = Groq(api_key="MA API CUA BAN")

# 2. Đọc nội dung file fizzbuzz_printer.py
try:
    with open("fizzbuzz_printer.py", "r", encoding="utf-8") as file:
        fizzbuzz_code = file.read()
except FileNotFoundError:
    print("Lỗi: Không tìm thấy file fizzbuzz_printer.py trong thư mục này!")
    exit()
    
# 3. Tạo Prompt yêu cầu AI sửa code theo đúng kỹ thuật Few-Shot & Wraps
prompt = f"""
I am working on a Python project. Please add 3 decorators:
1. Logging arguments.
2. Incrementing a counter.
3. Validating 'limit' is an int between 0-500.

IMPORTANT: You must use @wraps from functools for all decorators to preserve metadata.
Here is the code:
{fizzbuzz_code}
Return ONLY the full updated Python code.
"""
# 4. Gọi API Groq (Dùng model Llama 3.3 cực giỏi viết code)
print("Đang kết nối AI qua Groq API... Rất nhanh thôi...")
chat_completion = client.chat.completions.create(
    messages=[{"role": "user", "content": prompt}],
    model="llama-3.3-70b-versatile",
)
# 5. In kết quả ra màn hình
print("\n" + "="*50)
print("KẾT QUẢ TỰ ĐỘNG TỪ AI (DÙNG GROQ):")
print("="*50 + "\n")
print(chat_completion.choices[0].message.content)