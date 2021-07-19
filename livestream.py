import cv2
import numpy as np
import time
import requests
import json
from json import loads

url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/c321d3be-f280-4bf2-8210-36c10b935ee7/LabelFile/'
   
#turn on motor
import RPi.GPIO as GPIO

#GPIO.setwarnings(False)

#set GPIO numbering mode and define output pins
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
motor1a = 23
motor1b = 24
motor1e = 25

motor2a = 17
motor2b = 27
motor2e = 22

GPIO.setup(motor1a,GPIO.OUT)
GPIO.setup(motor1b,GPIO.OUT)
GPIO.setup(motor1e,GPIO.OUT)
GPIO.setup(motor2a,GPIO.OUT)
GPIO.setup(motor2b,GPIO.OUT)
GPIO.setup(motor2e,GPIO.OUT)

p=GPIO.PWM(motor1e,1000)
p.start(100)

p2=GPIO.PWM(motor2e,1000)
p2.start(100)
#motor code ends


def detection(image):
    cv2.imwrite("image.jpg", image) 
    data = {'file': open('image.jpg', 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('rgA9CBC-NcNMtz7tBD7UdfBC8yIv9UCz', ''), files=data)
   
    # ' ' actually not needed around the json file to work
    # x='{"message":"Success","result":[{"message":"Success","input":"image.jpg","prediction":[{"id":"","label":"squirrels","xmin":210,"ymin":204,"xmax":477,"ymax":438,"score":0.8680766}],"page":0,"request_file_id":"8ce7febf-749f-4c6b-8538-03d92724c069","filepath":"uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg","id":"3b33fa6f-d2ae-11eb-824b-0e66107fc08f","rotation":0}],"signed_urls":{"uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg":{"original":"https://nnts.imgix.net/uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg?expires=1624307538\u0026or=0\u0026s=30819415cdb71e30c029a1c23e4fb55e","original_compressed":"https://nnts.imgix.net/uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg?auto=compress\u0026expires=1624307538\u0026or=0\u0026s=9472ec91afa426fb33494702d8605386","thumbnail":"https://nnts.imgix.net/uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg?auto=compress\u0026expires=1624307538\u0026w=240\u0026s=fcc3688fc480bc642d787eb836839435","acw_rotate_90":"https://nnts.imgix.net/uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg?auto=compress\u0026expires=1624307538\u0026or=270\u0026s=9222dc43f052a67afe7749848098841c","acw_rotate_180":"https://nnts.imgix.net/uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg?auto=compress\u0026expires=1624307538\u0026or=180\u0026s=92e10a3480d6c7132a3e8cacd470bfe4","acw_rotate_270":"https://nnts.imgix.net/uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg?auto=compress\u0026expires=1624307538\u0026or=90\u0026s=398d48f1fbb5028755d7b4ee9d263c71","original_with_long_expiry":"https://nnts.imgix.net/uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg?expires=1639845138\u0026or=0\u0026s=6d13194ffbea55b243f57dd91325e141"}}}+'

    x= response.text # no () for text method
    y=json.loads(x)
    #https://stackoverflow.com/questions/16129652/accessing-json-elements
    
    #print(y)
    #for i in y['result']:
       # print(i['prediction'])
    for i in y['result'][0]['prediction']:
        try:
           print(i['score'])
           if i['score']>0.7:
               print("driving")
               #add timer
               running_time=3
               for i in range(running_time):
                   driveForward()
                   time.sleep(1)
               stopDrive()
        except Exception:
            continue
       
def driveForward():
    GPIO.output(motor1a,GPIO.LOW)
    GPIO.output(motor1b,GPIO.HIGH)
    GPIO.output(motor1e,GPIO.HIGH)
    GPIO.output(motor2a,GPIO.LOW)
    GPIO.output(motor2b,GPIO.HIGH)
    GPIO.output(motor2e,GPIO.HIGH)
    print("forward")
    
def stopDrive():
    GPIO.output(motor1a,GPIO.LOW)
    GPIO.output(motor1b,GPIO.LOW)
    GPIO.output(motor1e,GPIO.LOW)
    GPIO.output(motor2a,GPIO.LOW)
    GPIO.output(motor2b,GPIO.LOW)
    GPIO.output(motor2e,GPIO.LOW)
    print("stop")

def driveRight():
    GPIO.output(motor1a,GPIO.HIGH)
    GPIO.output(motor1b,GPIO.LOW)
    GPIO.output(motor1e,GPIO.HIGH)
    GPIO.output(motor2a,GPIO.LOW)
    GPIO.output(motor2b,GPIO.HIGH)
    GPIO.output(motor2e,GPIO.HIGH)
    print("turn right")
    
    
cap = cv2.VideoCapture(0)
while True:
  #time.sleep(1)
  _, frame = cap.read()

  #cv2.imshow("Frame", frame)
  # Put your code here
  detection(frame)
  driveRight()
  time.sleep(0.1)
  stopDrive()
  time.sleep(0.1)
  

  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
  
  #time.sleep(1)

cap.release()
cv2.destroyAllWindows()