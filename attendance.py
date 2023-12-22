import keyboard  # pip install keyboard
import time

def key_press(key):
    print(key.name)
    if key.name.isnumeric():
        print("NUMBERWANG")


keyboard.on_press(key_press)

while True:
    time.sleep(1)


