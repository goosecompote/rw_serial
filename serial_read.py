#python3 serial_read.py /dev/ttyUSB0

import serial
import sys

while True:
    ser = serial.Serial(
	port = str(sys.argv[1]),
	baudrate = 9600,
	rtscts = True
    )

    print(ser.readline().decode())
