import tkinter as tk # 간단한 윈도, 버튼, 레이블 등 구현용
from PIL import Image, ImageTk, ImageDraw # 이미지 편집 등
import math

# --- 설정 값 ---
IMAGE_SIZE = 400         # 돌림판 이미지 크기 (정사각형)
NUM_SECTORS = 8          # 돌림판의 구역 수
ROTATION_SPEED = 5       # 회전 속도 (1회 애니메이션마다 추가되는 각도)

# --- 돌림판 이미지 생성 함수 ---
def create_wheel_image(size, sectors):
    """지정한 크기와 구역 수에 따라 돌림판 이미지를 생성"""
    image = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    center = (size // 2, size // 2)
    radius = size // 2 - 10  # 약간의 여백
    angle_per_sector = 360 / sectors

    # 각 구역별 색상 (두 가지 색상을 번갈아 사용)
    colors = ["#FFCC00", "#FF6666"]

    for i in range(sectors):
        start_angle = i * angle_per_sector
        end_angle = start_angle + angle_per_sector
        draw.pieslice(
            [center[0]-radius, center[1]-radius, center[0]+radius, center[1]+radius],
            start=start_angle, end=end_angle,
            fill=colors[i % len(colors)], outline="black"
        )
        # 구역 중앙에 텍스트 (번호)를 그리려면
        mid_angle = math.radians(start_angle + angle_per_sector / 2)
        text_radius = radius * 0.6
        text_x = center[0] + text_radius * math.cos(mid_angle)
        text_y = center[1] + text_radius * math.sin(mid_angle)
        draw.text((text_x-10, text_y-10), str(i+1), fill="black")
    return image

# --- Tkinter 애플리케이션 ---
class SpinningWheelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("돌림판 회전 프로그램")

        # 돌림판 기본 이미지 생성
        self.base_image = create_wheel_image(IMAGE_SIZE, NUM_SECTORS)

        # 초기 회전 각도
        self.angle = 0
        self.spinning = True  # 회전 중 여부

        # Tkinter 캔버스 생성 및 초기 이미지 표시
        self.canvas = tk.Canvas(root, width=IMAGE_SIZE, height=IMAGE_SIZE)
        self.canvas.pack()
        self.tk_image = ImageTk.PhotoImage(self.base_image)
        self.image_on_canvas = self.canvas.create_image(IMAGE_SIZE//2, IMAGE_SIZE//2, image=self.tk_image)

        # 멈춤 버튼 추가
        self.stop_button = tk.Button(root, text="멈춤", command=self.stop_spinning, font=("Arial", 16))
        self.stop_button.pack(pady=10)

        # 애니메이션 시작
        self.update_animation()

    def update_animation(self):
        """돌림판 회전을 업데이트하는 함수"""
        if self.spinning:
            self.angle = (self.angle + ROTATION_SPEED) % 360
            # 이미지 회전 (expand=False: 크기가 바뀌지 않도록)
            rotated_image = self.base_image.rotate(-self.angle, resample=Image.BICUBIC)
            self.tk_image = ImageTk.PhotoImage(rotated_image)
            self.canvas.itemconfig(self.image_on_canvas, image=self.tk_image)
            # 일정 시간 후 재귀 호출 (여기서는 50ms)
            self.root.after(50, self.update_animation)

    def stop_spinning(self):
        """멈춤 버튼 클릭 시 호출되어 회전을 멈춤"""
        self.spinning = False

# --- 메인 실행 코드 ---
if __name__ == "__main__":
    root = tk.Tk()
    app = SpinningWheelApp(root)
    root.mainloop()
