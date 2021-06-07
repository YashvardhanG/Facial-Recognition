#Modules Required
import cv2
import numpy as np
from PIL import Image
import os

#Database Declaration
#Credits for Cascade: https://github.com/opencv/opencv
path = 'database'
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")

#Image Extractions
def getImagesAndLabels(path):
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]     
    faceSamples=[]
    ids = []

    for imagePath in imagePaths:
        PIL_img = Image.open(imagePath).convert('L')
        img_numpy = np.array(PIL_img,'uint8')

        id = int(os.path.split(imagePath)[1].split(".")[1])
        faces = detector.detectMultiScale(img_numpy)

        for (x,y,w,h) in faces:
            faceSamples.append(img_numpy[y:y+h,x:x+w])
            ids.append(id)

    return faceSamples,ids

#Training the model
print ("\nTraining Initiated. This might take a while")
faces,ids = getImagesAndLabels(path)
face_recognizer.train(faces, np.array(ids))

#Saving the Model
face_recognizer.write('resources/trained_model.yml')