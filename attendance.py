import keyboard  # pip install keyboard
import time, random, string

f=open('/home/wgrover/attendance/'+
        "".join(random.choices(string.ascii_lowercase+string.digits, k=8))+
        ".csv", "w")

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
