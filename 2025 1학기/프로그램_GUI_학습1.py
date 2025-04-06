import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("이미지와 버튼 예제")

# 캔버스 생성 및 이미지 로드
# canvas = tk.Canvas(root, width=300, height=300)
img = Image.open("./image/image_spin.png")
img_width, img_height = img.size  # 이미지의 가로, 세로 길이
print(img.size)

# 이미지 크기에 맞게 캔버스 생성
canvas = tk.Canvas(root, width=img_width, height=img_height)
canvas.pack() # 캔버스를 창에 배치

tk_img = ImageTk.PhotoImage(img)
# canvas.create_image(150, 150, image=tk_img)
canvas.create_image(img_width // 2, img_height // 2, image=tk_img)

# 버튼 생성 및 배치
button = tk.Button(root, text="클릭", command=lambda: print("버튼 클릭됨"))
button.pack(pady=10)

root.mainloop()
