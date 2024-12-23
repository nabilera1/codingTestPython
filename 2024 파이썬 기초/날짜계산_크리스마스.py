import tkinter as tk
from datetime import datetime

# 날짜 계산 함수
def calculate_days_left():
    # 오늘 날짜
    today = datetime.now()

    # 2024년 크리스마스 날짜
    christmas2024 = datetime(2024, 12, 25)

    # 두 날짜 사이의 차이 계산
    days_left = (christmas2024 - today).days

    # 결과를 레이블에 표시
    result_label.config(text=f"There are {days_left} days left until Christmas 2024!")

# GUI 설정
root = tk.Tk()
root.title("Days Until Christmas 2024")

# 창의 크기 설정
root.geometry("300x200")

# 설명 텍스트 레이블
info_label = tk.Label(root, text="How many days until Christmas 2024?", font=("Arial", 14))
info_label.pack(pady=20)

# 결과를 출력할 레이블
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# 버튼 생성
calculate_button = tk.Button(root, text="Calculate", command=calculate_days_left)
calculate_button.pack(pady=10)

# GUI 실행
root.mainloop()

