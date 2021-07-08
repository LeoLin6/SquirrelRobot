import RPi.GPIO as GPIO
from time import sleep

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
p = GPIO.PWM(motor1e, 1000)
p2 = p = GPIO.PWM(motor2e, 1000)
p1.start(100)
p2.start(100)

# turn on ultrasonic sensor
TRIG = 21
ECHO = 20

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.output(TRIG, False)

#############################################
# the loop
#############################################
while True:
    distance = get_distance()

    if distance < 25:
        print("obsacle detected at ", distance, "cm")
        drive_right()
    else:
        print("no object, drive forward")
        time.sleep(0.015)
        drive_forward()


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


def get_distance():  # use ultrasonic sensor
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()
    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150
    distance = round(distance + 1.15, 2)

    return distance
