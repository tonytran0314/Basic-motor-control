# This is the main file
import RPi.GPIO as GPIO
from time import sleep

# Set mode and turn warnings off
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pins declaration
Ena, In1, In2 = 17,27,22

# Declare output
GPIO.setup(Ena,GPIO.OUT)
GPIO.setup(In1,GPIO.OUT)
GPIO.setup(In2,GPIO.OUT)
pwm = GPIO.PWM(Ena, 100)

# Declare workingTime and breakTime
workingTime = 0.05
breakTime = 3

# Motor stop before running
pwm.start(0)


try:
    while True:
        # Motor rotate
        GPIO.output(In1, GPIO.HIGH)
        GPIO.output(In2, GPIO.LOW)
        # Motor speed: 40%
        pwm.ChangeDutyCycle(40) 
        sleep(workingTime)

        # Motor stop completely (speed = 0)
        pwm.ChangeDutyCycle(0)
        sleep(breakTime)
        
        # Motor rotate reversely
        GPIO.output(In1, GPIO.LOW)
        GPIO.output(In2, GPIO.HIGH)
        pwm.ChangeDutyCycle(40)
        sleep(workingTime)
        
        pwm.ChangeDutyCycle(0)
        sleep(breakTime)

# print this when press Ctrl C
except KeyboardInterrupt:
    print("\nThe program has been stopped")

# clean up all status before end the program
finally:
    GPIO.cleanup()
