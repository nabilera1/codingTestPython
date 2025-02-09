import sys
from PyQt5.QtWidgets import QApplication, QWidget

class BowlingScoreboardQt(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Bowling Scoreboard")
        self.setGeometry(300, 300, 600, 400)  # (x, y, width, height)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    scoreboard = BowlingScoreboardQt()
    sys.exit(app.exec_())  # 이벤트 루프 실행
