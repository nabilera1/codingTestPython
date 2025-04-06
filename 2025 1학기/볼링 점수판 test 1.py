import sys
import random
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QPushButton,
                             QGridLayout, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import Qt

# 실행 중간에 꺼져 버리는 현상

class BowlingScoreboard(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bowling Scoreboard")
        self.initUI()

        self.frame = 1
        self.rolls = []
        self.scores = [0] * 10  # 각 프레임별 점수
        self.total_score = 0

    def initUI(self):
        main_layout = QVBoxLayout()

        # 점수판 레이블
        self.score_labels = []
        grid_layout = QGridLayout()
        for i in range(11):  # 10프레임 + 총점
            label = QLabel("0")
            label.setAlignment(Qt.AlignCenter)
            self.score_labels.append(label)
            if i < 10:
                grid_layout.addWidget(label, 0, i)
            else:
                grid_layout.addWidget(label, 1, 9)  # 총점은 마지막 열에 표시
        main_layout.addLayout(grid_layout)

        # "Roll Ball" 버튼
        roll_button = QPushButton("Roll Ball ")
        roll_button.clicked.connect(self.roll_ball)
        button_layout = QHBoxLayout()
        button_layout.addWidget(roll_button)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)
        self.setGeometry(100, 100, 600, 300)
        self.show()

    def roll_ball(self):
        if self.frame > 10:
            return  # 게임 종료

        # 각 프레임마다 2번의 기회 (스트라이크 시 1번)
        pins_left = 10
        if len(self.rolls) % 2 == 0:  # 첫 번째 투구
            roll = random.randint(0, pins_left)
            self.rolls.append(roll)
            pins_left -= roll
            if roll == 10:  # 스트라이크
                self.rolls.append(0)  # 두 번째 투구는 0
                self.frame += 1
        else:  # 두 번째 투구
            roll = random.randint(0, pins_left)
            self.rolls.append(roll)
            self.frame += 1

        self.update_score()

    def update_score(self):
        frame_index = 0
        for i in range(len(self.rolls)):
            if i % 2 == 0:  # 첫 번째 투구
                if self.rolls[i] == 10:  # 스트라이크
                    self.scores[frame_index] += 10
                    if i < len(self.rolls) - 2:  # 다음 두 번의 투구 점수 추가
                        self.scores[frame_index] += self.rolls[i+2]
                        if (i+3) % 2 == 0: #그 다음 투구가 스트라이크일경우
                            self.scores[frame_index] += self.rolls[i + 4]
                        else:
                            self.scores[frame_index] += self.rolls[i + 3]
                    frame_index += 1
                else:  # 일반 투구
                    self.scores[frame_index] += self.rolls[i]
            else:  # 두 번째 투구
                if self.rolls[i-1] != 10 and self.rolls[i-1] + self.rolls[i] == 10:  # 스페어
                    self.scores[frame_index] += 10
                    if i < len(self.rolls) - 1:  # 다음 투구 점수 추가
                        self.scores[frame_index] += self.rolls[i+1]
                else:  # 일반 투구
                    self.scores[frame_index] += self.rolls[i]
                frame_index += 1

        self.total_score = sum(self.scores)

        # 점수판 업데이트
        for i in range(10):
            self.score_labels[i].setText(str(self.scores[i]))
        self.score_labels[10].setText(str(self.total_score))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    scoreboard = BowlingScoreboard()
    sys.exit(app.exec_())