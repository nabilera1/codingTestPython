import time

def print_story():
    story = [
        "🌞 Once upon a time, in a beautiful forest, there was a small turtle. 🐢",
        "🐢 The turtle had a big dream: to reach the finish line 🏁 of the grand forest race!",
        "🏁 The journey was long, but the turtle never gave up. Step by step... 🐢",
        "🌳 The turtle passed by tall trees and flowing rivers. 🌊",
        "🐇 Suddenly, a fast rabbit 🐰 appeared and laughed at the turtle: 'You'll never make it!'",
        "🐢 But the turtle just smiled and kept moving forward...",
        "💨 The rabbit ran fast but soon got tired and took a nap. 💤",
        "🐢 Slowly and steadily, the turtle kept walking... step by step...",
        "🎉 Finally, the turtle reached the finish line! 🏁",
        "🏆 'Slow and steady wins the race!' said the turtle proudly. 🐢🎊"
    ]

    for line in story:
        print(line)
        time.sleep(2)  # 각 줄마다 2초씩 기다렸다가 출력

if __name__ == "__main__":
    print_story()
