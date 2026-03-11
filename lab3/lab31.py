# Part 1: Open the chat window and ask to explain the geometric mean.


# Part 2: Implement the geometric mean function for two floating-point numbers.
def geometric_mean(a: float, b: float) -> float:
    return (a * b) ** 0.5

# Part 3: Call
num1 = 4.0
num2 = 9.0

result = geometric_mean(num1, num2)

print("Geometric mean:", result)