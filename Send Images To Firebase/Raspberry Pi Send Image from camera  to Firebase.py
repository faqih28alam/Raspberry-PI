import RPi.GPIO as GPIO 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
GPIO.setup(12, GPIO.IN)     # Declaring the input pin
from datetime import datetime
from picamera import PiCamera
from time import sleep
import os

import pyrebase

firebaseConfig = {
    'apiKey': ".....",
    'authDomain': ".....",
    'databaseURL': ".....",
    'projectId': ".....",
    'storageBucket': ".....",
    'messagingSenderId': ".....",
    'appId': ".....",
    'measurementId': "....."

}

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()

camera = PiCamera()

while True: 
  try:
    if GPIO.input(12) == GPIO.LOW:
        print("pushed")
        now = datetime.now()
        dt = now.strftime("%d%m%Y%H:%M:%S")
        name = dt+".jpg"
        camera.capture(name)
        print(name+" saved")
        storage.child(name).put(name)
        print("Image sent")
        os.remove(name)
        print("File Removed")
        sleep(2)
        
        
  except:
        camera.close()
