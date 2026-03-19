import nltk
from nltk.corpus import reuters
from collections import Counter, defaultdict

# Tải dữ liệu mẫu từ Reuters
nltk.download('reuters')
words = reuters.words()
text = ' '.join(words).lower()

# 1. Tính tần suất các chữ cái đơn lẻ
char_counts = Counter(c for c in text if c.isalpha() or c.isspace())
total_chars = sum(char_counts.values())

# 2. Tính xác suất có điều kiện (Bigram)
# Ví dụ: Sau chữ 'q' thường là chữ 'u'
bi_counts = defaultdict(Counter)
for i in range(len(text) - 1):
    char1, char2 = text[i], text[i+1]
    if (char1.isalpha() or char1.isspace()) and (char2.isalpha() or char2.isspace()):
        bi_counts[char1][char2] += 1

# Hiển thị xác suất: Sau 'q' là chữ gì?
q_next = bi_counts['q']
total_q = sum(q_next.values())
for char, count in q_next.most_common(3):
    print(f"P({char}|q) = {count/total_q:.4f}")