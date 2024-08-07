import tkinter as tk
from tkinter import messagebox
import sched
import time
import threading

class Pedometer:
    def __init__(self, daily_goal):
        self.daily_goal = daily_goal
        self.steps = 0

    def add_steps(self, steps):
        self.steps += steps

    def reset_steps(self):
        self.steps = 0

    def check_goal(self):
        if self.steps >= self.daily_goal:
            return True
        else:
            return False

def update_steps_display():
    steps_label.config(text=f"Today's Steps: {pedometer.steps}")

def add_steps():
    try:
        steps = int(steps_entry.get())
        pedometer.add_steps(steps)
        update_steps_display()
        messagebox.showinfo("Info", f"{steps} steps added.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def reset_steps():
    pedometer.reset_steps()
    update_steps_display()
    messagebox.showinfo("Info", "Steps have been reset.")

def check_goal():
    if pedometer.check_goal():
        messagebox.showinfo("Congratulations!", "You have reached your daily goal!")
    else:
        remaining_steps = pedometer.daily_goal - pedometer.steps
        messagebox.showinfo("Keep Going!", f"You need {remaining_steps} more steps to reach your goal.")

def check_evening_goal():
    if pedometer.steps >= 5000:
        messagebox.showinfo("Congratulations!", "You have walked 5000 steps today! Great job!")
    else:
        messagebox.showinfo("Keep Going!", "Keep walking to reach 5000 steps today!")

def schedule_evening_check():
    s = sched.scheduler(time.time, time.sleep)
    # Calculate the time remaining until 9 PM
    now = time.localtime()
    evening_time = time.mktime((now.tm_year, now.tm_mon, now.tm_mday, 21, 0, 0, now.tm_wday, now.tm_yday, now.tm_isdst))
    if evening_time < time.time():
        evening_time += 86400  # Move to the next day if 9 PM has passed

    delay = evening_time - time.time()
    s.enter(delay, 1, check_evening_goal)
    s.run()

def start_scheduler():
    threading.Thread(target=schedule_evening_check).start()

# Create main application window
root = tk.Tk()
root.title("Pedometer")

# Set daily step goal
daily_goal = 10000  # Example goal
pedometer = Pedometer(daily_goal)

# Create and place widgets
steps_label = tk.Label(root, text="Today's Steps: 0", font=("Helvetica", 16))
steps_label.pack(pady=10)

steps_entry = tk.Entry(root, font=("Helvetica", 14))
steps_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Steps", command=add_steps, font=("Helvetica", 14))
add_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset Steps", command=reset_steps, font=("Helvetica", 14))
reset_button.pack(pady=5)

goal_button = tk.Button(root, text="Check Goal", command=check_goal, font=("Helvetica", 14))
goal_button.pack(pady=5)

# Start the scheduler to check the goal at 9 PM
start_scheduler()

# Run the main event loop
root.mainloop()
