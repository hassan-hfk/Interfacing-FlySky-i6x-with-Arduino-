import serial
import time
import keyboard
import RPi.GPIO as gpio

# Channel 6
CS = 23
INC = 24
UD = 25

gpio.setmode(gpio.BCM)
gpio.setup(CS,gpio.OUT, initial = gpio.LOW)  # CS
gpio.setup(INC,gpio.OUT, initial = gpio.HIGH) # INC
gpio.setup(UD,gpio.OUT, initial = gpio.LOW) # U/D

# Channel 5 
CS_2 = 22
INC_2 = 17
UD_2 = 27

gpio.setup(CS_2,gpio.OUT, initial = gpio.LOW)  # CS
gpio.setup(INC_2,gpio.OUT, initial = gpio.HIGH) # INC
gpio.setup(UD_2,gpio.OUT, initial = gpio.LOW) # U/D

def up_2(): # Channel 5 
        gpio.output(CS_2,0)
        gpio.output(UD_2,1)
        gpio.output(INC_2,1)
        time.sleep(0.00002)
        gpio.output(INC_2,0)
        time.sleep(0.00002)
        gpio.output(INC_2,1)

def down_2(): # Channel 5 
        gpio.output(CS_2,0)
        gpio.output(UD_2,0)
        gpio.output(INC_2,1)
        time.sleep(0.00002)
        gpio.output(INC_2,0)
        time.sleep(0.00002)
        gpio.output(INC_2,1)


def up(): # Channel 6
        gpio.output(CS,0)
        gpio.output(UD,1)
        gpio.output(INC,1)
        time.sleep(0.00002)
        gpio.output(INC,0)
        time.sleep(0.00002)
        gpio.output(INC,1)

def down(): # Channel 6
        gpio.output(CS,0)
        gpio.output(UD,0)
        gpio.output(INC,1)
        time.sleep(0.00002)
        gpio.output(INC,0)
        time.sleep(0.00002)
        gpio.output(INC,1)

def channel_6_reset():
        for i in range(40):
                down()
                time.sleep(0.0002)

def channel_5_reset():
        for i in range(40):
                down_2()
                time.sleep(0.0002)


ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1)
ser.reset_input_buffer()

while True:
    if keyboard.is_pressed("w"):
        ser.write(b"w")
        print("w")
        time.sleep(0.007)

    if keyboard.is_pressed("s"):
        ser.write(b"s")
        print("s")
        time.sleep(0.007)

    if keyboard.is_pressed("a"):
        ser.write(b"a")
        print("a")
        time.sleep(0.007)

    if keyboard.is_pressed("d"):
        ser.write(b"d")
        print("d")
        time.sleep(0.007)

    if keyboard.is_pressed("q"):
        ser.write(b"q")
        print("q")
        time.sleep(0.004)

    if keyboard.is_pressed("e"):
        ser.write(b"e")
        print("e")
        time.sleep(0.004)

    if keyboard.is_pressed("n"):
        ser.write(b"n")
        print("n")
        time.sleep(0.002)

    if keyboard.is_pressed("m"):
        ser.write(b"m")
        print("m")
        time.sleep(0.002)

    if keyboard.is_pressed("1"):
        channel_5_reset()
        channel_6_reset()

    if keyboard.is_pressed("2"):
        channel_5_reset()
        channel_6_reset()
        for i in range(20):
            up_2()
            time.sleep(0.0002)

    if keyboard.is_pressed("3"):
        channel_5_reset()
        channel_6_reset()
        for i in range(40):
            up_2()

    if keyboard.is_pressed("4"):
        channel_5_reset()
        channel_6_reset()
        for i in range(40):
            up()

    if keyboard.is_pressed("5"):
        channel_5_reset()
        channel_6_reset()
        for i in range(40):
            up()
            if i < 20:
                up_2()

    if keyboard.is_pressed("6"):
        channel_5_reset()
        channel_6_reset()
        for i in range(350):
            up()
            up_2()
