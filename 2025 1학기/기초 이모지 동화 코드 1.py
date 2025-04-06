import time

def print_short_story():
    story = [
        "🐱✨ 작은 고양이가 🎩마법의 모자를 발견했어요!. 🐈💬💫 '야옹~' 하고 울자…",
        "🎩➡️🐲 펑! 고양이는 커다란 용이 되었어요! 🐉🔥",
        "🏰🐉 하늘을 날며 성 위를 지나며 모두에게 마법과 행복을 퍼트렸어요! ✨🎠🎆"
    ]

    for line in story:
        print(line)
        time.sleep(2)  # 2초 간격으로 출력

if __name__ == "__main__":
    print_short_story()
