import RPi.GPIO as GPIO 
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 
from time import sleep
import os

import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyAMniwDKsFBnUk9E1d3Ac3BAUsCIN35lFc",
    'authDomain': "faqsendimages.firebaseapp.com",
    'databaseURL': "https://faqsendimages-default-rtdb.firebaseio.com",
    'projectId': "faqsendimages",
    'storageBucket': "faqsendimages.appspot.com",
    'messagingSenderId': "756140925503",
    'appId': "1:756140925503:web:2b676767423c9f912c4e8a",
    'measurementId': "G-BJYR2GCEZ3"

}

firebase = pyrebase.initialize_app(firebaseConfig)

storage = firebase.storage()
image_name = "5.30.jpg" #Image path should be in the same folder with the code
print("get image")
storage.child(image_name).put(image_name)
print("Image sent")
sleep(2)

