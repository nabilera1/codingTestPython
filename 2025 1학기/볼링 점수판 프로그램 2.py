import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QGridLayout


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
            layout.addWidget(frame_label, 0, i)  # (row=0, column=i)

        # 점수 입력 칸 추가
        self.score_inputs = []
        for i in range(10):
            score_input = QLineEdit()
            self.score_inputs.append(score_input)
            layout.addWidget(score_input, 1, i)  # (row=1, column=i)

        self.setLayout(layout)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    scoreboard = BowlingScoreboard()
    sys.exit(app.exec_())
