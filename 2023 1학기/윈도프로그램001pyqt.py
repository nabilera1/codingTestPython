# Traceback (most recent call last):
#   File "C:\Users\user\PycharmProjects\codingTestPython\2023 1학기\윈도프로그램001pyqt.py", line 1, in <module>
#     from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton
# ModuleNotFoundError: No module named 'PyQt6'

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 윈도우 크기 설정
        self.setGeometry(100, 100, 300, 200)

        # 제목 설정
        self.setWindowTitle("My Window")

        # 라벨 추가
        label = QLabel(self)
        label.setText("Enter your name:")
        label.move(20, 20)

        # 텍스트 상자 추가
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 50)
        self.textbox.resize(200, 30)

        # 버튼 추가
        button = QPushButton(self)
        button.setText("Say Hello")
        button.move(20, 90)
        button.clicked.connect(self.say_hello)

    def say_hello(self):
        name = self.textbox.text()
        message = f"Hello, {name}!"
        print(message)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
