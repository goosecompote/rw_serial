#python3 serial_write.py /dev/ttyUSB0

import serial
import sys
import time

while True:
    ser = serial.Serial(
	port = str(sys.argv[1]),
	baudrate = 9600,
	rtscts = True
    )

    ser.write(str.encode(ser.name + '\n'))
    ser.close()
    time.sleep(1)