import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel


class FactorialCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 레이아웃 설정
        layout = QVBoxLayout()

        # 숫자 입력 필드
        self.input_edit = QLineEdit(self)
        self.input_edit.setPlaceholderText("Enter a number")
        layout.addWidget(self.input_edit)

        # 결과 표시 라벨
        self.result_label = QLabel("Result will be shown here", self)
        layout.addWidget(self.result_label)

        # 계산 버튼
        calc_button = QPushButton("Calculate Factorial", self)
        calc_button.clicked.connect(self.calculate_factorial)
        layout.addWidget(calc_button)

        self.setLayout(layout)
        self.setWindowTitle('Factorial Calculator')
        self.setGeometry(300, 300, 300, 200)

    def calculate_factorial(self):
        try:
            number = int(self.input_edit.text())
            if number < 0:
                raise ValueError("Enter a non-negative integer")
            result = self.factorial(number)
            self.result_label.setText(f"Factorial of {number} is {result}")
        except ValueError as e:
            self.result_label.setText(str(e))

    def factorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)


def main():
    app = QApplication(sys.argv)
    ex = FactorialCalculator()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
