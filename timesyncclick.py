import os
import tkinter as tk
from tkinter import messagebox
import sys
import time
import threading
import pyautogui
import datetime
print("V0.4")
def check_libs():
    required_libs = ['pyautogui', 'datetime']
    for lib in required_libs:
        try:
            __import__(lib)
            print(f"Library {lib} is already installed.")
        except ImportError:
            print(f"Library {lib} is not installed. Installing...")
            os.system(f"pip install {lib}")
            print(f"Library {lib} installed successfully!")

def show_current_time(root, time_label):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1, lambda: show_current_time(root, time_label))

def set_click_time(hour, minute, second, millisecond, time_label):
    target_time = datetime.datetime.now()
    target_time = target_time.replace(hour=hour, minute=minute, second=second, microsecond=millisecond*1000)
    delay = (target_time - datetime.datetime.now()).total_seconds()
    time.sleep(delay)
    pyautogui.click()

def start_click():
    hour = int(hour_entry.get())
    minute = int(minute_entry.get())
    minute = int(minute_entry.get())
    second = int(second_entry.get())
    millisecond = int(millisecond_entry.get())
    threading.Thread(target=set_click_time, args=(hour, minute, second, millisecond, time_label)).start()

def main():
    check_libs()
    root = tk.Tk()
    root.title("Real-time Clock")

    time_label = tk.Label(root, font=('Helvetica', 24), fg='red')
    time_label.pack()

    show_current_time(root, time_label)

    frame = tk.Frame(root)
    frame.pack()

    tk.Label(frame, text="Hour:").pack(side=tk.LEFT)
    global hour_entry
    hour_entry = tk.Entry(frame, width=5)
    hour_entry.pack(side=tk.LEFT)

    tk.Label(frame, text="Minute:").pack(side=tk.LEFT)
    global minute_entry
    minute_entry = tk.Entry(frame, width=5)
    minute_entry.pack(side=tk.LEFT)

    tk.Label(frame, text="Second:").pack(side=tk.LEFT)
    global second_entry
    second_entry = tk.Entry(frame, width=5)
    second_entry.pack(side=tk.LEFT)

    tk.Label(frame, text="Millisecond:").pack(side=tk.LEFT)
    global millisecond_entry
    millisecond_entry = tk.Entry(frame, width=5)
    millisecond_entry.pack(side=tk.LEFT)

    start_button = tk.Button(root, text="Start", command=start_click)
    start_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()