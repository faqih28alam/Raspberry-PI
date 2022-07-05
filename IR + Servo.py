import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.IN)         #Read output from IR sensor pin 18

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo1.start(0)
print ("Waiting for 2 seconds")
time.sleep(2)

while True:
    i=GPIO.input(18)
    if i==1:                 #When output from IR sensor is LOW
        intruders = 0
        print ("No intruders",intruders)
        #GPIO.output(3, 0)  #Turn OFF LED
        servo1.ChangeDutyCycle(2)
        time.sleep(1.5)
        servo1.ChangeDutyCycle(0)
        time.sleep(1.5)
    elif i==0:               #When output from IR sensor is HIGH
        intruders = 1
        print ("Intruder detected",intruders)
        #GPIO.output(3, 1)  #Turn ON LED
        servo1.ChangeDutyCycle(12)
        time.sleep(1.5)
        servo1.ChangeDutyCycle(0)
        time.sleep(1.5)


