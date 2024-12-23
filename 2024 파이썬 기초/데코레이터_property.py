class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise ValueError("Width must be positive.")

# 에러 처리 코드
rect = Rectangle(4, 5)

try:
    rect.width = -10  # setter로 값을 변경 시도
except ValueError as e:
    print(f"Error: {e}")  # 에러 메시지를 출력

print(rect.width)  # 정상적인 값 출력


