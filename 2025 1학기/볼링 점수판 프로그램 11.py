import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout, QLineEdit

class BowlingGame(QWidget):
    def __init__(self):
        super().__init__()
        self.init_game()
        self.initUI()

    def init_game(self):
        """ 게임 초기화 (데이터 초기화) """
        self.frames = [[] for _ in range(10)]
        self.scores = [0] * 10
        self.current_frame = 0
        self.game_over = False  # 게임 종료 여부 추가

    def initUI(self):
        self.setWindowTitle('🎳 Bowling Scoreboard')
        self.setGeometry(100, 100, 900, 400)

        self.layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        labels = ["투구 1", "투구 2", "총점"]
        for row, text in enumerate(labels):
            label = QLabel(text)
            self.grid_layout.addWidget(label, row + 1, 0)

        self.frame_labels = []
        self.score_inputs = []
        self.total_scores = []

        for i in range(10):
            frame_label = QLabel(f"Frame {i+1}")
            self.grid_layout.addWidget(frame_label, 0, i + 1)
            self.frame_labels.append(frame_label)

            first_input = QLineEdit()
            second_input = QLineEdit()
            first_input.setReadOnly(True)
            second_input.setReadOnly(True)

            self.grid_layout.addWidget(first_input, 1, i + 1)
            self.grid_layout.addWidget(second_input, 2, i + 1)

            self.score_inputs.append((first_input, second_input))

            total_score = QLineEdit()
            total_score.setReadOnly(True)
            self.grid_layout.addWidget(total_score, 3, i + 1)
            self.total_scores.append(total_score)

        self.layout.addLayout(self.grid_layout)

        self.play_button = QPushButton("Roll Ball 🎳")
        self.play_button.clicked.connect(self.play_frame)
        self.layout.addWidget(self.play_button)

        self.reset_button = QPushButton("Restart Game 🔄")
        self.reset_button.clicked.connect(self.reset_game)
        self.layout.addWidget(self.reset_button)

        self.final_score_label = QLabel("🏆 Final Score: 0")
        self.layout.addWidget(self.final_score_label)

        self.setLayout(self.layout)

    def play_frame(self):
        if self.game_over:
            return  # 게임이 종료된 경우 버튼 클릭을 무시

        if self.current_frame < 10:
            print(f"\n🎳 Frame {self.current_frame + 1} 시작...")

            if self.current_frame == 9:
                frame_scores = self.play_final_frame()
            else:
                frame_scores = self.play_normal_frame()

            first = frame_scores[0] if frame_scores[0] is not None else 0
            second = frame_scores[1] if len(frame_scores) > 1 and frame_scores[1] is not None else ""

            self.score_inputs[self.current_frame][0].setText(str(first))
            self.score_inputs[self.current_frame][1].setText(str(second) if second != "/" else "/")

            self.frames[self.current_frame] = frame_scores
            print(f"  - 투구 결과: {frame_scores}")

            self.calculate_scores()
            self.update_ui()

            print(f"  - 현재 총점: {sum(self.scores)}")
            self.print_scoreboard()

            self.current_frame += 1

        if self.current_frame == 10:
            print("\n🎉 게임 종료! 최종 점수:", sum(self.scores))
            self.play_button.setEnabled(False)
            self.game_over = True  # 게임 종료 상태로 설정

    def reset_game(self):
        """ 게임을 완전히 다시 시작 """
        print("\n🔄 게임 리셋 중...")

        self.init_game()  # 게임 데이터 초기화
        self.play_button.setEnabled(True)
        self.game_over = False  # 다시 시작 가능하게 설정

        # UI 리셋
        for i in range(10):
            self.score_inputs[i][0].clear()
            self.score_inputs[i][1].clear()
            self.total_scores[i].clear()
            self.frames[i] = []
            self.scores[i] = 0

        self.final_score_label.setText("🏆 Final Score: 0")
        print("✅ 게임이 정상적으로 리셋되었습니다!")

    def play_normal_frame(self):
        first = random.randint(0, 10)
        if first == 10:
            return ["X"]
        second = random.randint(0, 10 - first)
        return [first, "/" if first + second == 10 else second]

    def play_final_frame(self):
        first = random.randint(0, 10)
        second = random.randint(0, 10 if first == 10 else 10 - first)
        third = random.randint(0, 10) if first + second >= 10 else 0
        frame = [first, second if second != 10 else "X", third if third != 10 else "X"]
        print(f"  - 🎯 10프레임 보너스 투구 결과: {frame}")
        return frame

    def calculate_scores(self):
        for i in range(10):
            frame = self.frames[i]
            if "X" in frame:
                self.scores[i] = 10 + (self.scores[i + 1] if i + 1 < 10 else 0)
            elif "/" in frame:
                self.scores[i] = 10 + (self.scores[i + 1] if i + 1 < 10 else 0)
            else:
                self.scores[i] = sum(frame)

        self.final_score_label.setText(f"🏆 Final Score: {sum(self.scores)}")

    def update_ui(self):
        for i in range(10):
            total_score_text = str(self.scores[i]) if self.scores[i] else ""
            self.total_scores[i].setText(total_score_text)

    def print_scoreboard(self):
        print("\n📋 현재 점수판:")
        for i in range(10):
            frame_text = " | ".join(map(str, self.frames[i])) if self.frames[i] else "--"
            print(f"  Frame {i+1}: {frame_text}  ==>  Score: {self.scores[i]}")
        print("-" * 50)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = BowlingGame()
    game.show()
    sys.exit(app.exec_())
