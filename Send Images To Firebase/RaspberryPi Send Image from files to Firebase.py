import RPi.GPIO as GPIO 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
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
image_name = "5.30.jpg" #Image path should be in the same folder with the code
print("get image")
storage.child(image_name).put(image_name)
print("Image sent")
sleep(2)

