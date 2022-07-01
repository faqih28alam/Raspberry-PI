# Import libraries
import RPi.GPIO as GPIO
import time 
import cv2
import numpy as np
import os

######### SERVO CODE START ############
# Set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# Set pin 11 as an output, and set servo1 as pin 11 as PWM
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # Note 11 is pin, 50 = 50Hz pulse

#start PWM running, but with value of 0 (pulse off)
servo1.start(0)
print ("Waiting for 2 seconds")
time.sleep(2)
######################################

######### KNN CODE ############
def distance(v1, v2):
    # Eucledian
    return np.sqrt(((v1-v2)**2).sum())

def knn(train, test, k=50):
    dist = []

    for i in range(train.shape[0]):
        # Get the vector and label
        ix = train[i, :-1]
        iy = train[i, -1]
        # Compute the distance from test point
        d = distance(test, ix)
        dist.append([d, iy])
    # Sort based on distance and get top k
    dk = sorted(dist, key=lambda x: x[0])[:k]
    # Retrieve only the labels
    labels = np.array(dk)[:, -1]

    # Get frequencies of each label
    output = np.unique(labels, return_counts=True)
    # Find max frequency and corresponding label
    index = np.argmax(output[1])
    return output[0][index]
################################

#Init Camera
cap = cv2.VideoCapture(0)

# Face Detection
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

skip = 0
dataset_path = './dataset_wajah/'

face_data = []
labels = []

class_id = 0 # Labels for the given file
names = {} #Mapping btw id - name
user = 'String'

# Data Preparation
for fx in os.listdir(dataset_path):
    if fx.endswith('.npy'):
        #Create a mapping btw class_id and name
        names[class_id] = fx[:-4]
        print("Loaded "+fx)
        data_item = np.load(dataset_path+fx)
        face_data.append(data_item)

        #Create Labels for the class
        target = class_id*np.ones((data_item.shape[0],))
        class_id += 1
        labels.append(target)

face_dataset = np.concatenate(face_data,axis=0)
face_labels = np.concatenate(labels,axis=0).reshape((-1,1))

print(face_dataset.shape)
print(face_labels.shape)

trainset = np.concatenate((face_dataset,face_labels),axis=1)
print(trainset.shape)

#set servo lock the door
servo1.ChangeDutyCycle(3)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)
time.sleep(0.5)

# Testing 

while True:
    ret,frame = cap.read()
    if ret == False:
        continue

    #faces = face_cascade.detectMultiScale(frame,1.3,5)
    faces = face_cascade.detectMultiScale(frame, 
                                 scaleFactor=1.3, 
                                 minNeighbors=4, 
                                 minSize=(30, 30),
                                 flags=cv2.CASCADE_SCALE_IMAGE)
    #print(faces)
    #if(len(faces)==0):
    #    continue
    
    #mengkosongkan variabel klasifikasi wajah
    user = "0"

    for face in faces:
        x,y,w,h = face

        #Get the face ROI
        offset = 10
        face_section = frame[y-offset:y+h+offset,x-offset:x+w+offset]
        face_section = cv2.resize(face_section,(100,100))

        #Predicted Label (out)
        out = knn(trainset,face_section.flatten())

        #Display on the screen the name and rectangle around it
        pred_name = names[int(out)]
        user = pred_name
        cv2.putText(frame,pred_name,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),2,cv2.LINE_AA)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)

    #cv2.imshow("Faces",frame)
    print(user)
    
    if user == "FAQ1":
        print ("User Detected")    
        servo1.ChangeDutyCycle(12)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)
        time.sleep(2.5)
        
    elif user == "FAQ":
        print ("User Detected")    
        servo1.ChangeDutyCycle(12)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)
        time.sleep(2.5)
    
    elif user == "FAQ2":
        print ("User Detected")    
        servo1.ChangeDutyCycle(12)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)
        time.sleep(2.5)
            
    else:               
        print ("None Detected")
            
        servo1.ChangeDutyCycle(3)
        time.sleep(0.5)
        servo1.ChangeDutyCycle(0)
        time.sleep(0.5)
    
    key = cv2.waitKey(1) & 0xFF
    if key==ord('q'):
        break

#Clean things up at the end
servo1.stop()
GPIO.cleanup()
print ("Goodbye")

cap.release()
cv2.destroyAllWindows()
