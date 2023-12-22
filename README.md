# Attendance
Reads and records HID Prox Card IDs for classroom attendance tracking

## Hardware
Raspberry Pi (I'm using the Zero W, but others should work fine) connected via USB to a 125 kHz RFID card reader that connects to a computer as a keyboard (I'm using [this card reader from Amazon](https://www.amazon.com/gp/product/B07TMNZPXK/) but others should work with some tweaking).

## Setup
```
pip install keyboard
sudo cp attendance.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable attendance.service
```
