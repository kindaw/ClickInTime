import time
import threading
import pyautogui
import os
import tkinter as tk
import datetime

print("v0.3")

def show_current_time(root, time_label):
    current_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    time_label.config(text=current_time)
    root.after(1, lambda: show_current_time(root, time_label))

def set_click_time(hour, minute, second, millisecond, time_label):
    # the delay until the next click
    now = datetime.datetime.now()
    target_time = now.replace(hour=hour, minute=minute, second=second, microsecond=millisecond * 1000)
    if target_time < now:
        target_time += datetime.timedelta(days=1)

    delay = (target_time - now).total_seconds()

    # wait for the delay
    time.sleep(delay)

    # mouse click
    pyautogui.click()
    print("success")

def main():
    root = tk.Tk()
    root.title("Real-time Clock")
    time_label = tk.Label(root, font=("Helvetica", 24), fg="red")
    time_label.pack()

    input_frame = tk.Frame(root)
    input_frame.pack()

    tk.Label(input_frame, text="Hour (0-23):").pack(side=tk.LEFT)
    hour_entry = tk.Entry(input_frame, width=5)
    hour_entry.pack(side=tk.LEFT)

    tk.Label(input_frame, text="Minute (0-59):").pack(side=tk.LEFT)
    minute_entry = tk.Entry(input_frame, width=5)
    minute_entry.pack(side=tk.LEFT)

    tk.Label(input_frame, text="Second (0-59):").pack(side=tk.LEFT)
    second_entry = tk.Entry(input_frame, width=5)
    second_entry.pack(side=tk.LEFT)

    tk.Label(input_frame, text="Millisecond (0-999):").pack(side=tk.LEFT)
    millisecond_entry = tk.Entry(input_frame, width=5)
    millisecond_entry.pack(side=tk.LEFT)

    def start_click():
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())
        second = int(second_entry.get())
        millisecond = int(millisecond_entry.get())

        # Create a thread to handle the click
        click_thread = threading.Thread(target=set_click_time, args=(hour, minute, second, millisecond, time_label))
        click_thread.daemon = True
        click_thread.start()

    tk.Button(input_frame, text="Start", command=start_click).pack(side=tk.LEFT)

    show_current_time(root, time_label)
    root.mainloop()

if __name__ == "__main__":
    main()