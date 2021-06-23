# Display warning for deprecated Picamera functions (since v1.8) / affiche alerte si une fonction depreciee est utilisee 
import warnings
import pygame #keyboard controls
import picamera
import sys
import requests
import json
import random
from PIL import Image, ImageDraw

warnings.filterwarnings('default', category=DeprecationWarning)

pics_taken = 0
vid_taken = 0


# Init pygame and screen / initialise pygame et ecran
pygame.init()
res = pygame.display.list_modes() # return the resolution of your monitor / resolution du moniteur

screen = pygame.display.set_mode([1000, 1000])
#pygame.display.toggle_fullscreen()
pygame.mouse.set_visible = False

# Picamera object / objet Picamera
camera = picamera.PiCamera()
#camera.resolution = (1280, 720)
camera.framerate = float(24)

# Define functions / fonctions
def take_pic():
    global pics_taken
    pics_taken += 1
    camera.capture('image.jpg')
    call_nanonets()
    
def call_nanonets():
    url = 'https://app.nanonets.com/api/v2/ObjectDetection/Model/c321d3be-f280-4bf2-8210-36c10b935ee7/LabelFile/'
    data = {'file': open('image.jpg', 'rb')}
    response = requests.post(url, auth=requests.auth.HTTPBasicAuth('rgA9CBC-NcNMtz7tBD7UdfBC8yIv9UCz', ''), files=data)
    #print(response.text)
    
    # ' ' actually not needed around the json file to work
    # x='{"message":"Success","result":[{"message":"Success","input":"image.jpg","prediction":[{"id":"","label":"squirrels","xmin":210,"ymin":204,"xmax":477,"ymax":438,"score":0.8680766}],"page":0,"request_file_id":"8ce7febf-749f-4c6b-8538-03d92724c069","filepath":"uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg","id":"3b33fa6f-d2ae-11eb-824b-0e66107fc08f","rotation":0}],"signed_urls":{"uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg":{"original":"https://nnts.imgix.net/uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg?expires=1624307538\u0026or=0\u0026s=30819415cdb71e30c029a1c23e4fb55e","original_compressed":"https://nnts.imgix.net/uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg?auto=compress\u0026expires=1624307538\u0026or=0\u0026s=9472ec91afa426fb33494702d8605386","thumbnail":"https://nnts.imgix.net/uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg?auto=compress\u0026expires=1624307538\u0026w=240\u0026s=fcc3688fc480bc642d787eb836839435","acw_rotate_90":"https://nnts.imgix.net/uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg?auto=compress\u0026expires=1624307538\u0026or=270\u0026s=9222dc43f052a67afe7749848098841c","acw_rotate_180":"https://nnts.imgix.net/uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg?auto=compress\u0026expires=1624307538\u0026or=180\u0026s=92e10a3480d6c7132a3e8cacd470bfe4","acw_rotate_270":"https://nnts.imgix.net/uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg?auto=compress\u0026expires=1624307538\u0026or=90\u0026s=398d48f1fbb5028755d7b4ee9d263c71","original_with_long_expiry":"https://nnts.imgix.net/uploadedfiles/c321d3be-f280-4bf2-8210-36c10b935ee7/PredictionImages/53887725.jpeg?expires=1639845138\u0026or=0\u0026s=6d13194ffbea55b243f57dd91325e141"}}}+'

    x= response.text # no () for text method
    y=json.loads(x)
    #https://stackoverflow.com/questions/16129652/accessing-json-elements
    
    print(y["message"])
    print(y['result'][0]['prediction'][0]['xmax'])
    print(y['result'][0]['prediction'][0]['ymax'])
    
    rect(y['result'][0]['prediction'][0]['xmax'], y['result'][0]['prediction'][0]['ymax'], y['result'][0]['prediction'][0]['xmin'], y['result'][0]['prediction'][0]['ymin'])
    #print(y["result"]["prediction"]["score"])
    

#https://www.blog.pythonlibrary.org/2021/02/23/drawing-shapes-on-images-with-python-and-pillow/
def rect(x1, y1, x2, y2):
    image = Image.open('image.jpg')
    draw = ImageDraw.Draw(image)
    
    draw.rectangle((x1, y1, x2, y2), outline="yellow", width=3)
    
    image.save('result_image.jpg')

def take_video() :
    global vid_taken
    vid_taken += 1
    camera.start_recording('video_' + str(vid_taken) + '.h264')
    #Recording duration / duree enregistrement (15s)
    camera.wait_recording(15)
    camera.stop_recording()

def quit_app():
    camera.close()
    pygame.quit()
    print "You've taken", pics_taken, " pictures ", vid_taken, " videos. Don't forget to back them up (or they'll be overwritten next time)"
    sys.exit(0)

#Start camera preview / Demarre affichage en direct
camera.start_preview()

#line(50, 50, 100, 100)

while(True):
  pygame.display.update()
  for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          quit_app()
        elif event.key == pygame.K_SPACE:
          take_pic()
        elif event.key == pygame.K_BACKSPACE:
          take_video()
        elif event.key == pygame.K_TAB:
           camera.start_preview()