import tkinter as tk
from tkinter import messagebox
import threading
import pyautogui
import datetime

print("V1.1")

# Function to update the current time label every millisecond
def show_current_time(time_label):
    def update():
        current_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
        time_label.config(text=current_time)
        time_label.after(1, update)  # Update every millisecond for smooth display

    update()

# Function to set click time and update the time left label
def set_click_time(hour, minute, second, millisecond, time_label, time_left_label, debug_label):
    target_time = datetime.datetime.now().replace(hour=hour, minute=minute, second=second, microsecond=millisecond*1000)
    delay = (target_time - datetime.datetime.now()).total_seconds()

    def update_time_left():
        nonlocal delay
        if delay > 0:
            time_left_label.config(text=f"Time left: {int(delay)} seconds")
            delay -= 1
            time_left_label.after(1000, update_time_left)  # Update every second
        else:
            pyautogui.click()  # Perform the click action
            click_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
            debug_label.config(text=f"Clicked at: {click_time}")  # Update the debug label
            print(f"Clicked at: {click_time}")  # Print to terminal
            time_left_label.config(text="Time's up!")

    update_time_left()

# Function to start the click timer
def start_click(hour_entry, minute_entry, second_entry, millisecond_entry, time_label, time_left_label, debug_label):
    try:
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())
        second = int(second_entry.get())
        millisecond = int(millisecond_entry.get())
        threading.Thread(target=set_click_time, args=(hour, minute, second, millisecond, time_label, time_left_label, debug_label)).start()
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid hour, minute, second, and millisecond values.")

# Function to toggle the "stay on top" behavior
def toggle_stay_on_top(root, stay_on_top_button):
    if root.attributes("-topmost"):
        root.attributes("-topmost", False)
        stay_on_top_button.config(text="Toggle Stay on Top")
    else:
        root.attributes("-topmost", True)
        stay_on_top_button.config(text="Toggle Not on Top")

def main():
    global root  # Declare root as global to access it in toggle_stay_on_top
    root = tk.Tk()
    root.title("Real-time Clock")

    time_label = tk.Label(root, font=('Helvetica', 24), fg='red')
    time_label.pack()
    show_current_time(time_label)

    frame = tk.Frame(root)
    frame.pack()

    tk.Label(frame, text="Hour:").pack(side=tk.LEFT)
    hour_entry = tk.Entry(frame, width=5)
    hour_entry.pack(side=tk.LEFT)

    tk.Label(frame, text="Minute:").pack(side=tk.LEFT)
    minute_entry = tk.Entry(frame, width=5)
    minute_entry.pack(side=tk.LEFT)

    tk.Label(frame, text="Second:").pack(side=tk.LEFT)
    second_entry = tk.Entry(frame, width=5)
    second_entry.pack(side=tk.LEFT)

    tk.Label(frame, text="Millisecond:").pack(side=tk.LEFT)
    millisecond_entry = tk.Entry(frame, width=5)
    millisecond_entry.pack(side=tk.LEFT)

    time_left_label = tk.Label(root, font=('Helvetica', 18), fg='blue')
    time_left_label.pack()

    debug_label = tk.Label(root, font=('Helvetica', 14), fg='green')
    debug_label.pack()

    start_button = tk.Button(root, text="Start", command=lambda: start_click(hour_entry, minute_entry, second_entry, millisecond_entry, time_label, time_left_label, debug_label))
    start_button.pack()

    stay_on_top_button = tk.Button(root, text="Toggle Stay on Top", command=lambda: toggle_stay_on_top(root, stay_on_top_button))
    stay_on_top_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
