import tkinter as tk

# 윈도우 생성
window = tk.Tk()

# 윈도우 크기 설정
window.geometry("300x200")

# 제목 설정
window.title("My Window")

# 라벨 추가
label = tk.Label(window, text="Hello, World!")
label.pack()

# 윈도우 실행
window.mainloop()
