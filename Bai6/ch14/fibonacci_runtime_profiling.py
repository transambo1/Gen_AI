import time

def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

start = time.process_time()
n_value = 35
result = fibonacci_recursive(n_value)
end = time.process_time()

print(f"Kết quả Fibonacci({n_value}): {result}")
print(f"Thời gian thực thi: {end - start:.3f} giây")


