import wx
import threading
import sched
import time

class Pedometer:
    def __init__(self, daily_goal):
        self.daily_goal = daily_goal
        self.steps = 0

    def add_steps(self, steps=1):
        self.steps += steps

    def reset_steps(self):
        self.steps = 0

    def check_goal(self):
        if self.steps >= self.daily_goal:
            return True
        else:
            return False

def check_evening_goal(pedometer):
    if pedometer.steps >= 5:
        wx.CallAfter(wx.MessageBox, "You have walked 5000 steps today! Great job!", "Congratulations!")
    else:
        wx.CallAfter(wx.MessageBox, "Keep walking to reach 5000 steps today!", "Keep Going!")

def schedule_evening_check(pedometer):
    s = sched.scheduler(time.time, time.sleep)
    now = time.localtime()
    evening_time = time.mktime((now.tm_year, now.tm_mon, now.tm_mday, 21, 0, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
    if evening_time < time.time():
        evening_time += 86400

    delay = evening_time - time.time()
    s.enter(delay, 1, check_evening_goal, argument=(pedometer,))
    s.run()

class PedometerApp(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(PedometerApp, self).__init__(*args, **kwargs)

        self.pedometer = Pedometer(daily_goal=5)

        self.InitUI()
        self.Centre()
        self.Show()

        threading.Thread(target=schedule_evening_check, args=(self.pedometer,)).start()

    def InitUI(self):
        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        self.steps_label = wx.StaticText(panel, label="Today's Steps: 0")
        vbox.Add(self.steps_label, flag=wx.ALIGN_CENTER | wx.TOP, border=15)

        self.add_button = wx.Button(panel, label='Add 1 Step')
        self.add_button.Bind(wx.EVT_BUTTON, self.OnAddSteps)
        vbox.Add(self.add_button, flag=wx.ALIGN_CENTER | wx.TOP, border=10)

        self.reset_button = wx.Button(panel, label='Reset Steps')
        self.reset_button.Bind(wx.EVT_BUTTON, self.OnResetSteps)
        vbox.Add(self.reset_button, flag=wx.ALIGN_CENTER | wx.TOP, border=10)

        self.goal_button = wx.Button(panel, label='Check Goal')
        self.goal_button.Bind(wx.EVT_BUTTON, self.OnCheckGoal)
        vbox.Add(self.goal_button, flag=wx.ALIGN_CENTER | wx.TOP, border=10)

        panel.SetSizer(vbox)

    def OnAddSteps(self, event):
        self.pedometer.add_steps()
        self.UpdateStepsDisplay()

    def OnResetSteps(self, event):
        self.pedometer.reset_steps()
        self.UpdateStepsDisplay()

    def OnCheckGoal(self, event):
        if self.pedometer.check_goal():
            wx.MessageBox("You have reached your daily goal!", "Congratulations!")
        else:
            remaining_steps = self.pedometer.daily_goal - self.pedometer.steps
            wx.MessageBox(f"You need {remaining_steps} more steps to reach your goal.", "Keep Going!")

    def UpdateStepsDisplay(self):
        self.steps_label.SetLabel(f"Today's Steps: {self.pedometer.steps}")

def main():
    app = wx.App(False)
    PedometerApp(None, title='Pedometer')
    app.MainLoop()

if __name__ == "__main__":
    main()
