import cv2
import os
from matplotlib import pyplot as plt
from time import time

def fromwebcam():
    ret = False
    i = 0
    while not ret :
        photo = cv2.VideoCapture(i)
        ret, frame = photo.read()
        i += 1
    
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    cv2.imwrite(os.path.join('../ALGEO02-21130/test/input','input.jpg'), frame)
    photo.release()

def videowebcam():
    ret = False
    i = 0
    while not ret :
        photo = cv2.VideoCapture(i)
        ret, frame = photo.read()
        i += 1

    while photo.isOpened():
        ret, frame = photo.read()
        cv2.imshow('Webcam', frame)

        if cv2.waitKey(1) & 0xFF == ord(' '):
            break
    
    photo.relese()
    cv2.destroyAllWindows()

    # cropping
    precrop = cv2.imread('Web')

fromwebcam()
    