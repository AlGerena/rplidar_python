import serial
from time import sleep

uart1 = serial.Serial('COM3', baudrate=115200) # Initalize the serial port.
uart1.write(bytes([0xA5, 0x25])) # Send command to stop scanning.
sleep(0.1) # Wait for the scan to stop.
uart1.flushInput() # Clears the input buffer on the serial port.
uart1.write(bytes([0xA5, 0x82, 0x05, 0x02, 0x00, 0x00, 0x00, 0x00, 0x20])) # Send command to start scanning in express mode legacy version.
sleep(0.002)

print(uart1.read(7))

sleep(0.001)

a = 0

while a < 2:
    #a = a + 1
    message = uart1.read(132)
    if(len(message)) == 132:
        print(bin(message[0]), bin(message[1]))
        #print(message)
    else:
        print('message size is invalid.')

uart1.write(bytes([0xA5, 0x25])) # Send command to stop scanning.
