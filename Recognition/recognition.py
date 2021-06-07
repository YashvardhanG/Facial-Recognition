#Modules Required
import cv2

#Database Declaration
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('resources/trained_model.yml')
cascade = "resources/haarcascade_frontalface_default.xml"
detector = cv2.CascadeClassifier(cascade);

#Font Declaration
font = cv2.FONT_HERSHEY_DUPLEX

#Retrieving Users
id = 0
pad = open('resources/user.txt','r')
names = pad.read().splitlines()
pad.close()

#Video Dimensions
camera = cv2.VideoCapture(0)
camera.set(3, 1280)
camera.set(4, 1024)

#Minimum Window Dimensions
min_width = 0.1*camera.get(3)
min_height = 0.1*camera.get(4)

#Initiating Recognition
while True:
    ret, img = camera.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = detector.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(min_width), int(min_height)),
    )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        #Confidence is less than 100 ==> "0", Perfect Match
        if (confidence < 100):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        
        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',img) 

    #Escape key Protocol
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break

#Exiting
camera.release()
cv2.destroyAllWindows()
