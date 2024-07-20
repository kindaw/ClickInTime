import time
import threading
import pyautogui

print("v0.2")
def set_click_time(hour, minute, second, millisecond):
    # the delay until the next click
    now = time.time()
    target_time = time.mktime((time.localtime().tm_year, time.localtime().tm_mon, time.localtime().tm_mday, hour, minute, second, 0, 0, 0)) + millisecond / 1000
    delay = target_time - now
    if delay < 0:
        delay += 24 * 3600

    # wait for the delay
    time.sleep(delay)

    # mouse click
    pyautogui.click()
    print("success")

def main():
    hour = int(input("Enter the hour for the click (0-23): "))
    minute = int(input("Enter the minute for the click (0-59): "))
    second = int(input("Enter the second for the click (0-59): "))
    millisecond = int(input("Enter the millisecond for the click (0-999): "))

    # Create a thread to handle the click
    click_thread = threading.Thread(target=set_click_time, args=(hour, minute, second, millisecond))
    click_thread.daemon = True
    click_thread.start()

    # Wait for the click thread to finish
    click_thread.join()

    # Start over again
    print("Restarting...")
    main()

if __name__ == "__main__":
    main()