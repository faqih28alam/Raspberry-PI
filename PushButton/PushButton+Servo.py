import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
Servo_pin  = 11  #Set the GPIO.BOARD pin number of Motor Servo, 2   

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_UP)#Button to GPIO23
GPIO.setup(Servo_pin, GPIO.OUT)                           # Declaring the output pin

Servo = GPIO.PWM(Servo_pin, 50) # GPIO.BOARD 11 for PWM with 50Hz
Servo.start(2.5)                # Initialization

Servo.ChangeDutyCycle(2.5)
time.sleep(3)
Servo.ChangeDutyCycle(0)

try:
    while True:
         button_state = GPIO.input(15)
         if button_state == False:
            print('Button Pressed...')
            time.sleep(0.2)
            print("pintu terbuka")
            print("pintu terbuka")
            Servo.ChangeDutyCycle(11.5)
            time.sleep(1.5)
            Servo.ChangeDutyCycle(0)
            time.sleep(6)
            Servo.ChangeDutyCycle(2.5)
            time.sleep(1.5)
            Servo.ChangeDutyCycle(0)
                     
except:
    GPIO.cleanup()
