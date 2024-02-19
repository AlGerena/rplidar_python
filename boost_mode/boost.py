import serial
from time import sleep

uart1 = serial.Serial('/dev/ttyUSB0', baudrate=115200) # Initalize the serial port.
uart1.write(bytes([0xA5, 0x25])) # Send command to stop scanning.
sleep(0.1) # Wait for the scan to stop.
uart1.flushInput() # Clears the input buffer on the serial port.
uart1.write(bytes([0xA5, 0x82, 0x05, 0x01, 0x00, 0x00, 0x00, 0x00, 0x23])) # Send command to start scanning in boost mode.