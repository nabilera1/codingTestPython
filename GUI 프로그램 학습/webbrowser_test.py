# # Tkinter 기반 웹사이트 열기 GUI 예제
#
# import tkinter as tk
# import webbrowser
#
# def open_naver():
#     url = 'https://www.naver.com'
#     webbrowser.open(url)
#
# # 기본 창 생성
# root = tk.Tk()
# root.title("웹 열기 예제")
# root.geometry("300x100")
#
# # 버튼 추가
# btn = tk.Button(root, text="네이버 열기", command=open_naver)
# btn.pack(pady=20)
#
# # GUI 실행
# root.mainloop()


import wx
import webbrowser

class MyFrame(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='웹 열기 예제', size=(300, 150))

        panel = wx.Panel(self)
        vbox = wx.BoxSizer(wx.VERTICAL)

        self.button = wx.Button(panel, label='네이버 열기')
        self.button.Bind(wx.EVT_BUTTON, self.open_naver)

        vbox.Add(self.button, 0, wx.ALL | wx.CENTER, 20)
        panel.SetSizer(vbox)

        self.Centre()
        self.Show()

    def open_naver(self, event):
        webbrowser.open('https://www.naver.com')

if __name__ == '__main__':
    app = wx.App(False)
    frame = MyFrame()
    app.MainLoop()
