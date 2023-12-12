import serial
from time import sleep

uart1 = serial.Serial('COM5', baudrate=115200)

while True:
    uart1.read()