# 점수 계산 기능 추가

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout, QPushButton, QMessageBox


class BowlingScoreboard(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Bowling Scoreboard')
        self.setGeometry(100, 100, 800, 200)

        layout = QGridLayout()

        # 프레임 번호 추가 (1~10)
        for i in range(10):
            frame_label = QLabel(f'Frame {i + 1}')
            layout.addWidget(frame_label, 0, i)

        # 점수 입력 칸 추가
        self.score_inputs = []
        for i in range(10):
            score_input = QLineEdit()
            self.score_inputs.append(score_input)
            layout.addWidget(score_input, 1, i)

        # 점수 합산 버튼 추가
        self.calc_button = QPushButton("계산")
        self.calc_button.clicked.connect(self.calculate_score)
        layout.addWidget(self.calc_button, 2, 4)  # 버튼 위치 지정

        self.setLayout(layout)
        self.show()

    def calculate_score(self):
        total_score = 0
        try:
            for txt in self.score_inputs:
                score = int(txt.text()) if txt.text() else 0
                total_score += score

            QMessageBox.information(self, "Total Score", f"Your total score: {total_score}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid numbers!")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    scoreboard = BowlingScoreboard()
    app.exec_()
    # sys.exit(app.exec_())
