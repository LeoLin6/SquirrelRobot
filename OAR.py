import RPi.GPIO as GPIO
from time import sleep
import time

# turn on motor
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motor1a = 23
motor1b = 24
motor1e = 25
motor2a = 17
motor2b = 27
motor2e = 22

GPIO.setup(motor1a, GPIO.OUT)
GPIO.setup(motor1b, GPIO.OUT)
GPIO.setup(motor1e, GPIO.OUT)
GPIO.setup(motor2a, GPIO.OUT)
GPIO.setup(motor2b, GPIO.OUT)
GPIO.setup(motor2e, GPIO.OUT)
# set enable pins for power
p1 = GPIO.PWM(motor1e, 1000)
p2 = p = GPIO.PWM(motor2e, 1000)
p1.start(100)
p2.start(100)

# turn on ultrasonic sensor
TRIG1 = 21
ECHO1 = 20

GPIO.setup(TRIG1, GPIO.OUT)
GPIO.setup(ECHO1, GPIO.IN)
GPIO.output(TRIG1, False)

# turn on second ultrasonic sensor
TRIG2 = 26
ECHO2 = 19

GPIO.setup(TRIG2, GPIO.OUT)
GPIO.setup(ECHO2, GPIO.IN)
GPIO.output(TRIG2, False)


def drive_forward():  # driving functions
    GPIO.output(motor1a, GPIO.LOW)
    GPIO.output(motor1b, GPIO.HIGH)
    GPIO.output(motor1e, GPIO.HIGH)
    GPIO.output(motor2a, GPIO.LOW)
    GPIO.output(motor2b, GPIO.HIGH)
    GPIO.output(motor2e, GPIO.HIGH)
    print("forward")


def stop_drive():
    GPIO.output(motor1a, GPIO.LOW)
    GPIO.output(motor1b, GPIO.LOW)
    GPIO.output(motor1e, GPIO.LOW)
    GPIO.output(motor2a, GPIO.LOW)
    GPIO.output(motor2b, GPIO.LOW)
    GPIO.output(motor2e, GPIO.LOW)
    print("stop")


def drive_right():
    GPIO.output(motor1a, GPIO.HIGH)
    GPIO.output(motor1b, GPIO.LOW)
    GPIO.output(motor1e, GPIO.HIGH)
    GPIO.output(motor2a, GPIO.LOW)
    GPIO.output(motor2b, GPIO.HIGH)
    GPIO.output(motor2e, GPIO.HIGH)
    print("turn right")

def drive_left():
    GPIO.output(motor1a,GPIO.LOW)
    GPIO.output(motor1b,GPIO.HIGH)
    GPIO.output(motor1e,GPIO.HIGH)
    GPIO.output(motor2a,GPIO.HIGH)
    GPIO.output(motor2b,GPIO.LOW)
    GPIO.output(motor2e,GPIO.HIGH)

def get_distance(trigSensor, echoSensor):  # use ultrasonic sensor
    GPIO.output(trigSensor, True)
    time.sleep(0.00001)
    GPIO.output(trigSensor, False)

    while GPIO.input(echoSensor) == 0:
        pulse_start = time.time()
    while GPIO.input(echoSensor) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance + 1.15, 2)

    return distance


#############################################
# the loop
#############################################
while True:
    leftDis = get_distance(TRIG1, ECHO1)
    rightDis = get_distance(TRIG2, ECHO2)
    
    if leftDis < 50:
        #print("obsacle detected at ", distance, "cm")
        print("turn right")
        drive_right()
        time.sleep(0.7)
    elif rightDis < 50:
        print("turn left")
        drive_left()
        time.sleep(0.7)
    else:
        print("no object, drive forward")
        time.sleep(0.015)
        drive_forward()

