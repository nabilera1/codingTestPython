import sys
from PyQt5.QtWidgets import QApplication, QWidget
# QApplication : PyQt5 앱을 실행하는 데 필요해.
# QWidget : 기본 윈도우 역할을 하는 클래스.


class BowlingScoreboard(QWidget):
# QWidget 상속받아야 아래 initUI 내 메서드 호출 가능
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Bowling Scoreboard')
        self.setGeometry(100, 100, 600, 400)  # (x, y, width, height)
        self.show()

# setGeometry(x, y, width, height) : 창의 위치와 크기 지정.
# show() : 창을 화면에 표시.

if __name__ == '__main__':
    app = QApplication(sys.argv)
    scoreboard = BowlingScoreboard()
    sys.exit(app.exec_())
    # sys.exit(app.exec_()) : # 이벤트 루프 실행, 프로그램 실행 유지.