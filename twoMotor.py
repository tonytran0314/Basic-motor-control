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

pwmA = GPIO.PWM(Ena, 100)
pwmA.start(0)

pwmB = GPIO.PWM(Enb, 100)
pwmB.start(0)

sleepTime = 3

GPIO.output(In1, GPIO.HIGH)
GPIO.output(In2, GPIO.LOW)
pwmA.ChangeDutyCycle(100)

GPIO.output(In3, GPIO.HIGH)
GPIO.output(In4, GPIO.LOW)
pwmB.ChangeDutyCycle(100)

sleep(sleepTime)


pwmA.ChangeDutyCycle(0)
pwmB.ChangeDutyCycle(0)
sleep(sleepTime)


GPIO.output(In1, GPIO.LOW)
GPIO.output(In2, GPIO.HIGH)
pwmA.ChangeDutyCycle(100)

GPIO.output(In3, GPIO.LOW)
GPIO.output(In4, GPIO.HIGH)
pwmB.ChangeDutyCycle(100)

sleep(sleepTime)


exit()