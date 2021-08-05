import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
Ena, In1, In2 = 2,3,4
GPIO.setup(Ena,GPIO.OUT)
GPIO.setup(In1,GPIO.OUT)
GPIO.setup(In2,GPIO.OUT)
pwm = GPIO.PWM(Ena, 100)
pwm.start(0)

sleepTime = 3
'''
#counterclockwise
#increasing speed
for i in range(0, 100, 10):
    GPIO.output(In1, GPIO.HIGH)
    GPIO.output(In2, GPIO.LOW)
    pwm.ChangeDutyCycle(i)
    print(i)
    sleep(sleepTime)
    
#decreasing speed
for j in range(100, -10, -10):
    GPIO.output(In1, GPIO.HIGH)
    GPIO.output(In2, GPIO.LOW)
    pwm.ChangeDutyCycle(j)
    print(j)
    sleep(sleepTime)
    
#clockwise
#increasing speed
for i in range(0, 100, 10):
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    pwm.ChangeDutyCycle(i)
    print(i)
    sleep(sleepTime)
    
#decreasing speed
for j in range(100, -10, -10):
    GPIO.output(In1, GPIO.LOW)
    GPIO.output(In2, GPIO.HIGH)
    pwm.ChangeDutyCycle(j)
    print(j)
    sleep(sleepTime)
    
exit()
'''

GPIO.output(In1, GPIO.HIGH)
GPIO.output(In2, GPIO.LOW)
pwm.ChangeDutyCycle(100)
sleep(sleepTime)

pwm.ChangeDutyCycle(0)
sleep(sleepTime)

GPIO.output(In1, GPIO.LOW)
GPIO.output(In2, GPIO.HIGH)
pwm.ChangeDutyCycle(100)
sleep(sleepTime)

exit()