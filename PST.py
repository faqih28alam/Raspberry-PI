#!/usr/bin/env python
# -*- coding: utf-8 -*-

import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint
import RPi.GPIO as GPIO
import time
from time import sleep
from picamera import PiCamera
import telepot

servoPIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)
pintu = 0
camera = PiCamera()
camera.rotation = 180

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

p.ChangeDutyCycle(2.5)
time.sleep(3)
p.ChangeDutyCycle(0)

# Handling message from Telegram
def handleMessage(msg):
    global id
    global command
    
    id = msg['chat']['id'];
    command = msg['text'];
    print ('Command ' + command + ' from chat id' + str(id)); 
    if (command == 'Mulai'):
        print("Mulai")
     
    while True:
        main()

bot = telepot.Bot(token="5088878755:AAGf9z5zDYyUJ97ewQOq9tEtwD1uyXjoYVA")
bot.message_loop(handleMessage);

def main():
    try:
        while True:
            ## Search for a finger
            ## Tries to initialize the sensor
            try:
                f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

                if ( f.verifyPassword() == False ):
                    raise ValueError('The given fingerprint sensor password is wrong!')

            except Exception as e:
                print('The fingerprint sensor could not be initialized!')
                print('Exception message: ' + str(e))
                #exit(1)

            ## Gets some sensor information
            print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

            ## Tries to search the finger and calculate hash
            try:
                print('Waiting for finger...')

                ## Wait that finger is read
                while ( f.readImage() == False ):
                    pass

                ## Converts read image to characteristics and stores it in charbuffer 1
                f.convertImage(0x01)

                ## Searchs template
                result = f.searchTemplate()

                positionNumber = result[0]
                accuracyScore = result[1]

                if ( positionNumber == -1 ):
                    print('No match found!')
                
                    print("pintu tertutup")
                    pintu==0
                    sendnotif(pintu)
                
                    #exit(0)
                else:
                    print('Found template at position #' + str(positionNumber))
                    print('The accuracy score is: ' + str(accuracyScore))

                ## OPTIONAL stuff
                ##

                ## Loads the found template to charbuffer 1
                f.loadTemplate(positionNumber, 0x01)

                ## Downloads the characteristics of template loaded in charbuffer 1
                characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

                ## Hashes characteristics of template
                print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())
            
                print("pintu terbuka")
                pintu==1
                sendnotif(pintu)
                p.ChangeDutyCycle(12.5)
                time.sleep(1.5)
                p.ChangeDutyCycle(0)
                time.sleep(3)
                p.ChangeDutyCycle(2.5)
                time.sleep(1.5)
                p.ChangeDutyCycle(0)

            except Exception as e:
                print('Operation failed!')
                print('Exception message: ' + str(e))
                # exit(1)
        
 
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
          
def sendnotif(pintu):
    
    global id
    
    if pintu==1:
        camera.start_preview()
        camera.capture('/home/pi/Pictures/images.jpg',resize=(640,640))
        time.sleep(2)
        camera.stop_preview()
        bot.sendPhoto(id,open('/home/pi/Pictures/images.jpg','rb'))
        
    elif pintu == 0:
        camera.start_preview()
        camera.capture('/home/pi/Pictures/images.jpg',resize=(640,640))
        time.sleep(2)
        camera.stop_preview()
        bot.sendPhoto(id,open('/home/pi/Pictures/images.jpg','rb'))
