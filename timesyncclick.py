import os
import tkinter as tk
from tkinter import messagebox
import sys
import time
import threading
import pyautogui
import datetime

print("V1.0") 

# Check if required libraries are installed
def check_libs():
    required_libs = ['pyautogui', 'datetime']
    for lib in required_libs:
        try:
            __import__(lib)
            print(f"Library {lib} is already installed.")  # Print success message
        except ImportError:
            print(f"Library {lib} is not installed. Installing...")  # Print installation message
            os.system(f"pip install {lib}")  # Install the library
            print(f"Library {lib} installed successfully!")  # Print success message

# Update the current time label every second
def show_current_time(root, time_label):
    current_time = datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3]
    time_label.config(text=current_time)
    root.after(1, lambda: show_current_time(root, time_label))  # Call this function again after 1000 milliseconds (1 second)

# Set the click time and update the time left label
def set_click_time(hour, minute, second, millisecond, time_label, time_left_label):
    target_time = datetime.datetime.now()
    target_time = target_time.replace(hour=hour, minute=minute, second=second, microsecond=millisecond*1000)
    delay = (target_time - datetime.datetime.now()).total_seconds()
    def update_time_left():
        nonlocal delay
        if delay > 0:
            time_left_label.config(text=f"Time left: {int(delay)} seconds")  # Update the time left label
            delay -= 1  # Decrement the delay
            root.after(1000, update_time_left)  # Call this function again after 1000 milliseconds (1 second)
        else:
            pyautogui.click()  # Perform the click action
    update_time_left()

# Start the click timer
def start_click(time_label, time_left_label):
    try:
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())
        second = int(second_entry.get())
        millisecond = int(millisecond_entry.get())
        threading.Thread(target=set_click_time, args=(hour, minute, second, millisecond, time_label, time_left_label)).start()  # Start the click timer in a separate thread
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid hour, minute, second, and millisecond values.")

# Toggle the "stay on top" behavior
def toggle_stay_on_top():
    if root.attributes("-topmost"):
        root.attributes("-topmost", False)
        stay_on_top_button.config(text="Toggle Stay on Top")  # Update the button text
    else:
        root.attributes("-topmost", True)
        stay_on_top_button.config(text="Toggle Not on Top")  # Update the button text

def main():
    check_libs()  # Check for required libraries
    global root
    root = tk.Tk()
    root.title("Real-time Clock")  # Set the window title

    time_label = tk.Label(root, font=('Helvetica', 24), fg='red')
    time_label.pack()  # Create and pack the current time label

    show_current_time(root, time_label)  # Start updating the current time label

    frame = tk.Frame(root)
    frame.pack()  # Create and pack the input frame

    tk.Label(frame, text="Hour:").pack(side=tk.LEFT)
    global hour_entry
    hour_entry = tk.Entry(frame, width=5)
    hour_entry.pack(side=tk.LEFT)  # Create and pack the hour input field

    tk.Label(frame, text="Minute:").pack(side=tk.LEFT)
    global minute_entry
    minute_entry = tk.Entry(frame, width=5)
    minute_entry.pack(side=tk.LEFT)  # Create and pack the minute input field

    tk.Label(frame, text="Second:").pack(side=tk.LEFT)
    global second_entry
    second_entry = tk.Entry(frame, width=5)
    second_entry.pack(side=tk.LEFT)  # Create and pack the second input field

    tk.Label(frame, text="Millisecond:").pack(side=tk.LEFT)
    global millisecond_entry
    millisecond_entry = tk.Entry(frame, width=5)
    millisecond_entry.pack(side=tk.LEFT)  # Create and pack the millisecond input field

    start_button = tk.Button(root, text="Start", command=lambda: start_click(time_label, time_left_label))
    start_button.pack()  # Create and pack the start button

    global time_left_label
    time_left_label = tk.Label(root, font=('Helvetica', 18), fg='blue')
    time_left_label.pack()  # Create and pack the time left label

    global stay_on_top_button
    stay_on_top_button = tk.Button(root, text="Toggle Stay on Top", command=toggle_stay_on_top)
    stay_on_top_button.pack()  # Create and pack the stay on top button

    root.mainloop()  # Start the GUI event loop

if __name__ == "__main__":
    main()  # Call the main function