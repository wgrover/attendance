import keyboard  # pip install keyboard
import time

f = open("/home/wgrover/attendance/out.txt", "a")

def key_press(key):
    print(key.name)
    if key.name == "enter":
        f.write("\n")
    else:
        f.write(key.name)
    f.flush()

keyboard.on_press(key_press)

while True:
    time.sleep(1)

f.close()
