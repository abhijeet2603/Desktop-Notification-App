import time

from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title = "Please Drink Water",
            message = "About 15.5 cups (3.7 liters) of fluids a day for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            timeout=12
        )
        time.sleep(60*60)