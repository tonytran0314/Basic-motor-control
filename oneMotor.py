# This is the main file
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

Ena, In1, In2 = 17,27,22

GPIO.setup(Ena,GPIO.OUT)
GPIO.setup(In1,GPIO.OUT)
GPIO.setup(In2,GPIO.OUT)
pwm = GPIO.PWM(Ena, 100)

workingTime = 0.1
breakTime = 3

pwm.start(0)


try:
    while True:
        GPIO.output(In1, GPIO.HIGH)
        GPIO.output(In2, GPIO.LOW)
        pwm.ChangeDutyCycle(25)
        sleep(workingTime)

        pwm.ChangeDutyCycle(0)
        sleep(breakTime)

        GPIO.output(In1, GPIO.LOW)
        GPIO.output(In2, GPIO.HIGH)
        pwm.ChangeDutyCycle(25)
        sleep(workingTime)
        
        pwm.ChangeDutyCycle(0)
        sleep(breakTime)

except KeyboardInterrupt:
    print("\nThe program has been stopped")

finally:
    GPIO.cleanup()
