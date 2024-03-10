import serial
from time import sleep

uart1 = serial.Serial('COM5', baudrate=115200) # Initalize the serial port.
uart1.write(bytes([0xA5, 0x25])) # Send command to stop scanning.
sleep(0.1) # Wait for the scan to stop.
uart1.flushInput() # Clears the input buffer on the serial port.
uart1.write(bytes([0xA5, 0x20])) # Send command to start scanning in standard mode.
sleep(0.002) # Waits for the Response Descriptor (must be > 0.002, standard mode).
print(uart1.read(7)) # Read and Print the Response Descriptor.
sleep(0.8)# Wait for the Data Response to initialize (must be > 0.8 at 0x20, standard mode).

while True:
    message = uart1.read(5) # Read the data.
    if len(message) == 5: # Checks the size of the data.
        print(bin(message[0]))
        if (message[0] & 0b01) == 0b01: # Checks the type of scan and whether it is valid.
            print('New scan.')
        elif (message[0] & 0b10) == 0b10:
            print('Current scan.')
        else :
            print('Failure in the data check one.')
            break
        print(bin(message[2]), bin(message[1]), bin(message[4]), bin(message[3])) # Prints the angle and distance of the data.
        if(message[1] & 0b1) != 0b1: # Checks the data check bit.
            print('Failure in the data check two.')
            break
        angl = (message[2] << 7) | (message[1] >> 1) # Extract the angle from data.
        dist = (message[4] << 8) | message[3] # Extract the distance from data.
        print(bin(angl), bin(dist)) # Print the raw angle and distance.
        print('Angle: ' + str(angl/64) + ' Grades' + ' Distance: ' + str(dist/40) + ' cm') # Print the real angle and distance.
    else:
        print('Data size is invalid.')
        break
uart1.write(bytes([0xA5, 0x25])) # Send command to stop scanning.