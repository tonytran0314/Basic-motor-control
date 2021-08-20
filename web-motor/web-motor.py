# Turn on/off motor thru web

#Server file

import RPi.GPIO as GPIO
from flask import Flask, render_template

GPIO.setmode(GPIO.BCM)

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

app = Flask(__name__)

@app.route("/")
def greeting():
    return render_template("index.html")

@app.route("/on")
def on():
    GPIO.output(In1, GPIO.HIGH)
    GPIO.output(In2, GPIO.LOW)
    pwm.ChangeDutyCycle(100)
    return render_template("on.html") # must have templates folder to contain html files

@app.route("/off")
def off():
    pwm.ChangeDutyCycle(0)
    return render_template("off.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
