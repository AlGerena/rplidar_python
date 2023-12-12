import serial
from time import sleep

uart1 = serial.Serial('/dev/ttyUSB0', baudrate=115200) # Initalize the serial port.
uart1.write(bytes([0xA5, 0x20])) # Send command to start scanning in standard mode.
sleep(0.002) # Waits for the Response Descriptor (must be > 0.002).
print(uart1.read(7)) # Read the Response Descriptor.
sleep(0.8)# Wait for the Data Response to initialize (must be > 0.8 at 0x20).

while True:
    message = uart1.read(5) # Read the data.
    if len(message) == 5: # Check the size of the data.
        if (message[0] & 0b11) == 1: # Check the type of measurement and whether it is valid.
            print('New scan.')
        elif (message[0] & 0b11) == 2:
            print('Current scan.')
        else :
            print('Failure in the data check.')
            break
        print(bin(message[2]), bin(message[1]), bin(message[0]), bin(message[0] & 0b11)) # Print the data. 
        angl = ( (message[2]<< 7)) | (message[1] >> 1) # Extract the angle from data.
        dist = (message[4] << 8) | (message[3]) # Extract the distance from data.
        print(bin(angl), angl, len(bin(angl))) # Print the raw angle and distance.
        print('Angle:', angl/64, 'Distance:', dist/40) # Print the corrected angle and distance.
    else:
        print('Data size is invalid.')
        break
uart1.write(bytes([0xA5, 0x25])) # Send command to stop scanning.
sleep(0.5)
uart1.read()