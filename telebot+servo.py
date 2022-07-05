#coder :- Salman Faris

#import sys
import time
import telepot
import RPi.GPIO as GPIO
from picamera import PiCamera

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(11, GPIO.OUT)

#CAMERA START
camera = PiCamera()
#camera.rotation = 180

#SERVO START
servoPIN = 11
p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

p.ChangeDutyCycle(2.5)
time.sleep(3)
p.ChangeDutyCycle(0)

#SERVO
def on(pin):
        #GPIO.output(pin,GPIO.HIGH)
        print("ON")
        print("pintu terbuka")
        p.ChangeDutyCycle(10.5)
        time.sleep(1.5)
        p.ChangeDutyCycle(0)
        time.sleep(3)
        p.ChangeDutyCycle(2.5)
        time.sleep(1.5)
        p.ChangeDutyCycle(0)
        return
        
def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)

    if command == 'Open':
        bot.sendMessage(chat_id, on(11))
       
    elif command == 'Capture':
        camera.start_preview()
        camera.capture('/home/pi/Pictures/Notif.jpg',resize=(640,640))
        time.sleep(2)
        camera.stop_preview()
        bot.sendPhoto(chat_id, open('/home/pi/Pictures/Notif.jpg','rb'))
    
    elif command == "Mulai":
        main()
        

def main():
    print("mendeteksi orang")
    time.sleep(2)
    print("terdeteksi orang asing")
    

bot = telepot.Bot('5088878755:AAGf9z5zDYyUJ97ewQOq9tEtwD1uyXjoYVA')
bot.message_loop(handle)
print('I am listening...')