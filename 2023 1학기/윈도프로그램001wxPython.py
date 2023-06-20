import wx

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super().__init__(parent, title=title, size=(300, 200))

        # 패널 생성
        panel = wx.Panel(self)

        # 라벨 생성
        label = wx.StaticText(panel, label="Hello, World!", pos=(20, 20))

        # 버튼 생성
        button = wx.Button(panel, label="Click me!", pos=(20, 50))
        button.Bind(wx.EVT_BUTTON, self.on_button_click)

    def on_button_click(self, event):
        # 버튼 클릭 시 호출되는 함수
        print("Button clicked")

if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame(None, title="My Window")
    frame.Show()
    app.MainLoop()
