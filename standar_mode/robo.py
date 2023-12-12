import serial
from time import sleep

uart1 = serial.Serial('COM3', baudrate=115200) # Initalize the serial port.
uart1.write(bytes([0xA5, 0x20])) # Send command to start scanning in standard mode.
sleep(0.002) # Waits for the Response Descriptor (must be > 0.002).
print(uart1.read(7)) # Read the Response Descriptot.
sleep(0.8)# Waits for the Response data (must be > 0.8 to 0x20).

while True:
    message = uart1.read(5)
    if len(message) == 5:
        if (message[0] & 0b11) == 1:
            print('New scan.')
        elif (message[0] & 0b11) == 2:
            print('Current scan')
        else :
            print('Error in samplimg.')
            break
        print(bin(message[2]), bin(message[1]), bin(message[0]), bin(message[0] & 0b11))
        angl = ( (message[2]<< 7)) | (message[1] >> 1)
        dist = (message[4] << 8) | (message[3])
        print(bin(angl), angl, len(bin(angl)))
        print('Angulo:', angl/64, 'Distancia:', dist/40)
    else:
        print('Message size is invalid.')
        break
uart1.write(bytes([0xA5, 0x25]))
sleep(0.5)
uart1.read()