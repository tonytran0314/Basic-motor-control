'''
Motor control by keyboard
W - forward
S - backward
'''

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Ena = 2 
Enb = 17
In1, In2 = 3,4
In3, In4 = 22,27

GPIO.setup(Ena,GPIO.OUT)
GPIO.setup(In1,GPIO.OUT)
GPIO.setup(In2,GPIO.OUT)

GPIO.setup(Enb,GPIO.OUT)
GPIO.setup(In3,GPIO.OUT)
GPIO.setup(In4,GPIO.OUT)

pwmA = GPIO.PWM(Ena, 1000)
pwmA.start(0)

pwmB = GPIO.PWM(Enb, 1000)
pwmB.start(0)

sleepTime = 3

moveMent = None
while True:
    moveMent = input("Enter w, s or x: ")

    if moveMent == "s" or moveMent == "S":
        print("Backward")
        GPIO.output(In1, GPIO.LOW)
        GPIO.output(In2, GPIO.HIGH)
        pwmA.ChangeDutyCycle(100)

        GPIO.output(In3, GPIO.HIGH)
        GPIO.output(In4, GPIO.LOW)
        pwmB.ChangeDutyCycle(100)

        sleep(sleepTime)
    elif moveMent == "w" or moveMent == "W":
        print("Forward")
        GPIO.output(In1, GPIO.HIGH)
        GPIO.output(In2, GPIO.LOW)
        pwmA.ChangeDutyCycle(100)

        GPIO.output(In3, GPIO.LOW)
        GPIO.output(In4, GPIO.HIGH)
        pwmB.ChangeDutyCycle(100)

        sleep(sleepTime)
    elif moveMent == "x" or moveMent == "X":
        print("Motors have been stopped")
        pwmA.ChangeDutyCycle(0)
        pwmB.ChangeDutyCycle(0)
        sleep(sleepTime)
        exit()
    else:
        print("Only w, s or x")

exit()