import random
import tkinter as tk

def generate_lotto_numbers():
    # 1~45 중 6개 랜덤 샘플링
    numbers = random.sample(range(1, 46), 6)
    numbers.sort()

    # 보너스 번호 선택 (중복 없이)
    remaining_numbers = list(set(range(1, 46)) - set(numbers))
    bonus = random.choice(remaining_numbers)

    # 결과 출력
    result_text.set(f"당첨번호: {numbers}  |  보너스: {bonus}")

# Tkinter 윈도우 생성
root = tk.Tk()
root.title("로또 번호 뽑기")
root.geometry("400x200")

# 결과 표시할 텍스트 변수
result_text = tk.StringVar()
result_text.set("버튼을 눌러 로또 번호를 뽑으세요!")

# 라벨 (결과 표시)
label = tk.Label(root, textvariable=result_text, font=("Arial", 12))
label.pack(pady=20)

# 버튼 (클릭 시 번호 생성)
button = tk.Button(root, text="로또 번호 뽑기", command=generate_lotto_numbers, font=("Arial", 14))
button.pack(pady=10)

# 메인루프
root.mainloop()
