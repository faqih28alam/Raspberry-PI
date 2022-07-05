import hashlib
import RPi.GPIO as GPIO
import time
from time import sleep
from picamera import PiCamera
import telepot

servoPIN = 17
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
    elif(command=='Buka'):
        print("Buka")
        pintu = 1
        sendnotif(pintu)
    elif(command=='Tutup'):
        print("Tutup")
        pintu = 0
        sendnotif(pintu)
        
    while True:
        main()

bot = telepot.Bot(token="5088878755:AAGf9z5zDYyUJ97ewQOq9tEtwD1uyXjoYVA")
bot.message_loop(handleMessage);

def main():
    try:
        while True:
            if(pintu == 1):
                print("pintu terbuka")
                p.ChangeDutyCycle(12.5)
                time.sleep(1.5)
                p.ChangeDutyCycle(0)
                time.sleep(3)
                p.ChangeDutyCycle(2.5)
                time.sleep(1.5)
                p.ChangeDutyCycle(0)
 
    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()
          
def sendnotif(pintu):
    
    global id
    
    if pintu==1:
        camera.start_preview()
        camera.capture('/home/pi/Pictures/Notif.jpg',resize=(640,640))
        time.sleep(2)
        camera.stop_preview()
        bot.sendPhoto(id,open('/home/pi/Pictures/Notif.jpg','rb'))
        
    elif pintu == 0:
        camera.start_preview()
        camera.capture('/home/pi/Pictures/Notif.jpg',resize=(640,640))
        time.sleep(2)
        camera.stop_preview()
        bot.sendPhoto(id,open('/home/pi/Pictures/Notif.jpg','rb'))