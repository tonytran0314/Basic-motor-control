'''
Motor control by keyboard
W - forward
S - backward
'''
# import libraries
import RPi.GPIO as GPIO
from time import sleep

# turn mode on
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# declare pins
# Note: pins 2,3,4 make motor auto rotate even when the program not executing
Ena = 2 
Enb = 17
In1, In2 = 3,4
In3, In4 = 22,27

# set pins are output pins
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

# declare sleep time and movement input
sleepTime = 0.25
moveMent = None

try:
    while True:
        #Wait for user to enter a letter
        moveMent = raw_input("Enter w, s or x: ") 

        # if user enters s or S, motor 1 rotates clockwise, the other rotates counter-clockwise
        if moveMent == "s" or moveMent == "S": 
            print("Backward")

            # 1 low 1 high so the motor can spin
            GPIO.output(In1, GPIO.LOW)
            GPIO.output(In2, GPIO.HIGH)
            pwmA.ChangeDutyCycle(100) # set motor speed to 100%
            GPIO.output(In3, GPIO.HIGH)
            GPIO.output(In4, GPIO.LOW)
            pwmB.ChangeDutyCycle(100)
            sleep(sleepTime)

        # if user enters w or W, motor 2 rotates clockwise, the other rotates counter-clockwise
        elif moveMent == "w" or moveMent == "W":
            print("Forward")
            GPIO.output(In1, GPIO.HIGH)
            GPIO.output(In2, GPIO.LOW)
            pwmA.ChangeDutyCycle(100)
            GPIO.output(In3, GPIO.LOW)
            GPIO.output(In4, GPIO.HIGH)
            pwmB.ChangeDutyCycle(100)
            sleep(sleepTime)

        # x or X to stop the motors
        elif moveMent == "x" or moveMent == "X":
            print("Motors have been stopped")
            pwmA.ChangeDutyCycle(0)
            pwmB.ChangeDutyCycle(0)
            sleep(sleepTime)

        # z or Z to exit the program
        elif moveMent == "z" or moveMent == "Z":
            print("Exit")
            exit()
        else:
            print("Only w, s or x")
except KeyboardInterrupt:
    print("\nThe program has been stopped")
finally:
    GPIO.cleanup()
