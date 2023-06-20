import tkinter as tk
import random

class RandomTeamGeneratorGUI:
    def __init__(self, master):
        self.master = master
        master.title("랜덤 팀 생성기")

        self.label = tk.Label(master, text="조원 리스트:")
        self.label.pack()

        self.listbox = tk.Listbox(master)
        self.listbox.pack()

        self.button = tk.Button(master, text="팀 생성", command=self.generate_team)
        self.button.pack()

        self.quit_button = tk.Button(master, text="종료", command=master.quit)
        self.quit_button.pack()

    def generate_team(self):
        # 조원 리스트
        members = ["김철수", "이영희", "박민수", "홍길동", "장영실", "안중근", "신사임당", "유관순", "서울우유", "김좌진",
                   "이봉창", "김구", "이승만", "윤봉길", "민영식", "홍범도", "안중범", "전봉준", "안창호", "윤동주"]

        # 리스트 셔플
        random.shuffle(members)

        # 리스트를 2개의 팀으로 분할
        team1 = members[:10]
        team2 = members[10:]

        # 리스트 박스 초기화
        self.listbox.delete(0, tk.END)

        # 각 팀원 출력
        self.listbox.insert(tk.END, "=== 1조 ===")
        for member in team1:
            self.listbox.insert(tk.END, member)

        self.listbox.insert(tk.END, "")

        self.listbox.insert(tk.END, "=== 2조 ===")
        for member in team2:
            self.listbox.insert(tk.END, member)

# GUI 생성
root = tk.Tk()
my_gui = RandomTeamGeneratorGUI(root)
root.mainloop()
