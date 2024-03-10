import serial
from time import sleep

uart1 = serial.Serial('COM3', baudrate=115200) # Initalize the serial port.
uart1.write(bytes([0xA5, 0x25])) # Send command to stop scanning.
sleep(0.1) # Wait for the scan to stop.
uart1.flushInput() # Clears the input buffer on the serial port.
uart1.write(bytes([0xA5, 0x82, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00, 0x22])) # Send command to start scanning in express mode legacy version.
sleep(0.002)

print(uart1.read(7))

sleep(0.001)

print(uart1.read(84))
print(uart1.read(1))

"""
uart1.write(bytes([0xA5, 0x59])) # Send command to start scanning in express mode legacy version.
sleep(0.002)
print(uart1.read(7))
sleep(0.002)
print(uart1.read(4))
"""