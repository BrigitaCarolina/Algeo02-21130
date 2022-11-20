import cv2
import os
from matplotlib import pyplot as plt
from time import time

def fromwebcam():
    ret = False
    i = 0
    while not ret :
        photo = cv2.VideoCapture(i)
        photo.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
        photo.set(cv2.CAP_PROP_FRAME_HEIGHT, 256)
        ret, frame = photo.read()
        i += 1
    
    plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    cv2.imwrite(os.path.join('../ALGEO02-21130/test/input','input.jpg'), frame)
    photo.release()

    # CROP
    precrop = cv2.imread('input.jpg')


def videowebcam():
    ret = False
    i = 0
    while not ret :
        photo = cv2.VideoCapture(i)
        ret, frame = photo.read()
        i += 1

    prevtime = time()

    while photo.isOpened():
        photo.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
        photo.set(cv2.CAP_PROP_FRAME_HEIGHT, 256)
        ret, frame = photo.read()
        cv2.imshow('Webcam', frame)

        currenttime = time()

        if currenttime - prevtime >= 10.0 :
            #proses imagenya ada yg sama atau engga

            #simpen benter
            cv2.imwrite(os.path.join('../ALGEO02-21130/test/input','input.jpg'), frame)
            prevtime = currenttime

            #if x :
                #kasih notif telah ditemukan orang yang mirip
                #balik ke laman gui
                #break
            #else :
                #kasih notif buat benerin posisi biar bisa ke capt dengan benar

        if cv2.waitKey(1) & 0xFF == ord(' '):
            break
    
    photo.relese()
    cv2.destroyAllWindows()

videowebcam()
    