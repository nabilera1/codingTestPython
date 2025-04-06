import sys
import random
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QGridLayout

# 현재 Roll Ball 버튼 누르면 화면 강제 종료되는 현상이 보임.
class BowlingGame(QWidget):
    def __init__(self):
        super().__init__()
        self.frames = [[] for _ in range(10)]  # 10 프레임 생성
        self.scores = [0] * 10  # 각 프레임 점수 저장
        self.current_frame = 0  # 현재 진행 중인 프레임
        self.initUI()

    def initUI(self):
        """ GUI 초기화 """
        self.setWindowTitle('🎳 Bowling Scoreboard')
        self.setGeometry(100, 100, 800, 400)

        # 메인 레이아웃
        self.layout = QVBoxLayout()

        # 프레임별 점수 표시 레이아웃
        self.grid_layout = QGridLayout()
        self.frame_labels = []

        # 프레임과 점수 레이블 생성
        for i in range(10):
            label = QLabel(f"Frame {i + 1}: ")
            self.grid_layout.addWidget(label, 0, i)
            self.frame_labels.append(label)

        self.layout.addLayout(self.grid_layout)

        # 버튼 추가 (플레이)
        self.play_button = QPushButton("Roll Ball 🎳")
        self.play_button.clicked.connect(self.play_frame)
        self.layout.addWidget(self.play_button)

        # 최종 점수 표시 레이블
        self.total_score_label = QLabel("🏆 Final Score: 0")
        self.layout.addWidget(self.total_score_label)

        self.setLayout(self.layout)

    def play_frame(self):
        """ 프레임 진행 """
        if self.current_frame < 10:
            if self.current_frame == 9:  # 마지막 프레임 (최대 3번 투구 가능)
                self.frames[self.current_frame] = self.play_final_frame()
            else:
                self.frames[self.current_frame] = self.play_normal_frame()

            self.calculate_scores()
            self.update_ui()
            self.current_frame += 1

        if self.current_frame == 10:
            self.play_button.setEnabled(False)  # 게임 종료 후 버튼 비활성화

    def play_normal_frame(self):
        """ 일반 프레임 (최대 2번 투구) """
        first = random.randint(0, 10)
        if first == 10:  # 스트라이크
            return ["X"]
        second = random.randint(0, 10 - first)
        return [first, "/" if first + second == 10 else second]

    def play_final_frame(self):
        """ 10번째 프레임 (최대 3번 투구 가능) """
        first = random.randint(0, 10)
        if first == 10:
            second = random.randint(0, 10)
            if second == 10:
                third = random.randint(0, 10)
            else:
                third = random.randint(0, 10 - second)
            return ["X", "X" if second == 10 else second, "X" if third == 10 else third]

        second = random.randint(0, 10 - first)
        if first + second == 10:
            third = random.randint(0, 10)
            return [first, "/", third]

        return [first, second]

    def calculate_scores(self):
        """ 점수 계산 """
        for i in range(10):
            frame = self.frames[i]
            if "X" in frame:  # 스트라이크
                self.scores[i] = 10 + self.strike_bonus(i)
            elif "/" in frame:  # 스페어
                self.scores[i] = 10 + self.spare_bonus(i)
            else:  # 오픈 프레임
                self.scores[i] = sum(frame if isinstance(frame, list) else [frame])

        self.total_score_label.setText(f"🏆 Final Score: {sum(self.scores)}")

    def strike_bonus(self, frame_index):
        """ 스트라이크 보너스 계산 """
        if frame_index >= 9:
            return 0
        next_frame = self.frames[frame_index + 1]
        if "X" in next_frame:
            if frame_index + 1 == 9:
                return 10 + (next_frame[1] if isinstance(next_frame[1], int) else 10)
            second_frame = self.frames[frame_index + 2]
            return 10 + (second_frame[0] if isinstance(second_frame[0], int) else 10)
        return next_frame[0] + (next_frame[1] if isinstance(next_frame[1], int) else 10)

    def spare_bonus(self, frame_index):
        """ 스페어 보너스 계산 """
        if frame_index >= 9:
            return 0
        next_frame = self.frames[frame_index + 1]
        return next_frame[0] if isinstance(next_frame[0], int) else 10

    def update_ui(self):
        """ GUI 업데이트 (점수 표시) """
        for i in range(10):
            frame_text = " | ".join(map(str, self.frames[i])) if self.frames[i] else ""
            self.frame_labels[i].setText(f"Frame {i + 1}: {frame_text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = BowlingGame()
    game.show()
    sys.exit(app.exec_())
