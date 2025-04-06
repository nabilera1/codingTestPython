# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
# class BowlingScoreboardQt(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setWindowTitle("Bowling Scoreboard")
#         self.setGeometry(300, 300, 600, 400)  # (x, y, width, height)
#         self.show()
#
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     scoreboard = BowlingScoreboardQt()
#     sys.exit(app.exec_())  # 이벤트 루프 실행


# ///////////////////////
# 기본 코드

# import sys
# from PyQt5.QtWidgets import QApplication, QWidget
#
# app = QApplication(sys.argv)
# window = QWidget()
# window.show()
#
# sys.exit(app.exec_()) # 를 사용하여 프로그램 종료
# # sys.exit(app.exec_())


# PySimpleGUI 사용해보기

import PySimpleGUI as sg

class BowlingScoreboardPSG:
    def __init__(self):
        self.initUI()

    def initUI(self):
        layout = [[sg.Text("Bowling Scoreboard")],
                  [sg.Button("Close")]]

        window = sg.Window("Bowling Scoreboard", layout, size=(600, 400))

        while True:
            event, values = window.read()
            if event == sg.WIN_CLOSED or event == "Close":
                break

        window.close()

if __name__ == "__main__":
    scoreboard = BowlingScoreboardPSG()