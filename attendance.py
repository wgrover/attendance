import keyboard  # pip install keyboard
import time

f = open("/home/wgrover/attendance/out.txt", "a")

def key_press(key):
    print(key.name)
    f.write(key.name)
    f.flush()
    if key.name.isnumeric():
        print("NUMBERWANG")


keyboard.on_press(key_press)

while True:
    time.sleep(1)

f.close()
