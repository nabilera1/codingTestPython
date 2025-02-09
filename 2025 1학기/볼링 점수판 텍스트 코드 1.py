import random


class BowlingGame:
    def __init__(self):
        self.frames = [[] for _ in range(10)]  # 10 프레임 생성
        self.scores = [0] * 10  # 각 프레임별 점수 저장

    def play(self):
        for frame in range(10):
            if frame == 9:  # 10번째 프레임 (3번까지 기회 가능)
                self.frames[frame] = self.play_final_frame()
            else:
                self.frames[frame] = self.play_frame()

        self.calculate_scores()
        self.display_scoreboard()

    def play_frame(self):
        """ 일반 프레임 플레이 (2번 투구 가능) """
        first = random.randint(0, 10)
        if first == 10:  # 스트라이크
            return ["X"]
        second = random.randint(0, 10 - first)
        return [first, "/" if first + second == 10 else second]

    def play_final_frame(self):
        """ 10번째 프레임 플레이 (최대 3번 투구 가능) """
        first = random.randint(0, 10)
        if first == 10:  # 첫 투구가 스트라이크
            second = random.randint(0, 10)
            if second == 10:  # 두 번째 투구도 스트라이크
                third = random.randint(0, 10)
            else:
                third = random.randint(0, 10 - second)
            return ["X", "X" if second == 10 else second, "X" if third == 10 else third]

        second = random.randint(0, 10 - first)
        if first + second == 10:  # 스페어
            third = random.randint(0, 10)
            return [first, "/", third]

        return [first, second]  # 오픈 프레임

    def calculate_scores(self):
        """ 점수 계산 """
        for i in range(10):
            frame = self.frames[i]

            if "X" in frame:  # 스트라이크
                self.scores[i] = 10 + self.strike_bonus(i)
            elif "/" in frame:  # 스페어
                self.scores[i] = 10 + self.spare_bonus(i)
            else:  # 일반 점수
                self.scores[i] = sum(frame if isinstance(frame, list) else [frame])

    def strike_bonus(self, frame_index):
        """ 스트라이크 보너스 계산 """
        if frame_index >= 9:
            return 0  # 10프레임이면 추가 점수 없음

        next_frame = self.frames[frame_index + 1]
        if "X" in next_frame:  # 다음 프레임도 스트라이크라면
            if frame_index + 1 == 9:  # 마지막 프레임이면 다음 점수 하나만 반영
                return 10 + (next_frame[1] if isinstance(next_frame[1], int) else 10)
            second_frame = self.frames[frame_index + 2]
            return 10 + (second_frame[0] if isinstance(second_frame[0], int) else 10)

        return next_frame[0] + (next_frame[1] if isinstance(next_frame[1], int) else 10)

    def spare_bonus(self, frame_index):
        """ 스페어 보너스 계산 """
        if frame_index >= 9:
            return 0  # 10프레임이면 추가 점수 없음
        next_frame = self.frames[frame_index + 1]
        return next_frame[0] if isinstance(next_frame[0], int) else 10

    def display_scoreboard(self):
        """ 점수판 출력 """
        print("\n🎳 Bowling Scoreboard 🎳")
        for i in range(10):
            frame_str = " | ".join(map(str, self.frames[i]))
            print(f"Frame {i + 1}: {frame_str}  ==>  Score: {self.scores[i]}")
        print(f"\n🏆 Final Score: {sum(self.scores)} 🎉")


if __name__ == "__main__":
    game = BowlingGame()
    game.play()
