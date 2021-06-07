#Modules Required
import cv2
import os

#Creating/Checking a Database Dir
if os.path.exists('database'):
    pass
else:
    os.mkdir('database')

#Reseting Counter and Users
dir = os.listdir('database')
if len(dir) == 0:
    users = open('resources/user.txt','w')
    ids = open('resources/count.txt','w')
    users.write('None')
    ids.write('0')
    users.close()
    ids.close()

    if os.path.exists('resources/trained_model.yml'):
        os.remove('resources/trained_model.yml')
    else:
        pass

else:
    pass

#Video Dimensions
camera = cv2.VideoCapture(0)
camera.set(3, 1280)
camera.set(4, 1024)

#Cascade for Frontal Face Detection
#Credits: https://github.com/opencv/opencv
detector = cv2.CascadeClassifier('resources/haarcascade_frontalface_default.xml')

#Read Pre-Existing Users
users = open('resources/user.txt','r')
names = users.read().splitlines()
users.close()

#Name Input
flag = 1
while(flag == 1):
    face_name = input('Enter the name of the person:')
    if face_name in names:
        print('\nSorry, the name already exists, please enter another name.\n')
        flag = 1
    else:
        users = open('resources/user.txt','a')
        users.write("\n" + face_name)
        users.close()
        flag = 0

#ID Counter Increment
ids = open('resources/count.txt','r')
read = ids.read()
count = int(read)
face_id = count + 1
ids.close()

ids = open('resources/count.txt','w')
write = str(face_id)
ids.write(write)
ids.close()

#Instructions
print("Please make sure that you are in a well lit environment.\nThis will capture several photos of you, so make sure to give different angles.\n\nCapturing will start automatically within 10 seconds.")

#Camera Capturing Initiated
count = 0
flag = 0
print("\nFace Caputuring Initiated. Please look into the camera.\nThis might take a while.")
while(flag == 0):
    ret, img = camera.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face = detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in face:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1
        
        cv2.imwrite("database/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('image', img)

    #Escape key Protocol
    key = cv2.waitKey(10) & 0xff
    if key == 27:
        flag = 1
    elif count >= 400:
        flag = 1

#Training the Dataset
import training

#Exiting
camera.release()
cv2.destroyAllWindows()
