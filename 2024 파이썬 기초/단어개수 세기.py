text = "파이썬은 쉽고 강력한 프로그래밍 언어입니다. 파이썬은 다양한 분야에서 활용됩니다. 파이썬은 데이터 분석, 웹 개발, 인공지능 등 다양한 분야에서 사용됩니다."

word_counts = {}
words = text.split()

for word in words:
    word = word.strip(".,")  # 문장 부호 제거
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

print(word_counts)