import time
import serial
import keyboard

ser=serial.Serial(port="COM3", baudrate=9600, bytesize=8, timeout=2,
                  stopbits=serial.STOPBITS_ONE)

while True:
    ser.write("A".encode('Ascii'))
    receive=ser.read()
    print(receive.decode('Ascii'))
    time.sleep(1)
    if keyboard.is_pressed('q'):
        print("User need to Quit the application")
        break


ser.close()
