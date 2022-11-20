import cv2
import os
from matplotlib import pyplot as plt
from time import time
import eigenface
import extractor

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
    cv2.imwrite(os.path.join('../ALGEO02-21130/test/dataset','input.jpg'), frame)
    photo.release()


def videowebcam():
    datasetPath = os.getcwd() + "/test/dataset"
    inputPath = os.getcwd() + "/test/input"

    listPath = os.listdir(inputPath)
    for i in range(len(listPath)) :
        os.remove(os.path.join(inputPath,listPath[i]))

    ret = False
    i = 0
    while not ret :
        photo = cv2.VideoCapture(i)
        ret, frame = photo.read()
        i += 1

    prevtime = time()
    timeout = time() + 60*5

    while photo.isOpened():
        photo.set(cv2.CAP_PROP_FRAME_WIDTH, 256)
        photo.set(cv2.CAP_PROP_FRAME_HEIGHT, 256)
        ret, frame = photo.read()
        cv2.imshow('Webcam', frame)

        currenttime = time()

        if currenttime - prevtime >= 10.0 :
            cv2.imwrite(os.path.join('../ALGEO02-21130/test/input','input.jpg'), frame)
            
            images_arr = extractor.extractImages(datasetPath)
            test_face = extractor.extractImages(inputPath)
            eigenfaces,execution_time,isfounded = eigenface.Eigenfaces(images_arr,test_face)
            print(isfounded)

            if isfounded :
                break
            else :
                prevtime = currenttime

        if cv2.waitKey(1) & 0xFF == ord(' ') or currenttime > timeout:
            break
    
    photo.release()
    cv2.destroyAllWindows()

#fromwebcam()
#videowebcam()
    