from gpiozero import Servo
from time import sleep
from gpiozero import AngularServo

#servo = Servo(9)
#servo = Servo(10)
servo1=AngularServo(10, min_angle=0, max_angle=180, min_pulse_width=0.0006, max_pulse_width=0.0024)

#upper motor
servo2 = AngularServo(9, min_angle=0, max_angle=180, min_pulse_width=0.0006, max_pulse_width=0.0024)
#servo.value = 1

def turn_servo2():
    sleep(0.5)
    servo2.value=0.1
    sleep(0.5)
    servo2.value=0.7
    sleep(0.5)
    
#turn_servo2()

try:
    servo1.min()
    turn_servo2()
    servo1.mid()
    turn_servo2()
    servo1.max()
    turn_servo2()
    
except KeyboardInterrupt:
    print("Program stopped")

