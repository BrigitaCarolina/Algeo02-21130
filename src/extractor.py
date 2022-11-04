import cv2
import numpy as np
import os
from os import listdir

print(os.getcwd())

def extractImages(folderPath):
    # extract
    images_train =[]
    for file in listdir(folderPath):
        filePath = os.path.join(folderPath,file)
        img = cv2.imread(filePath, cv2.IMREAD_GRAYSCALE)
        img = cv2.resize(img,(256,256),interpolation = cv2.INTER_AREA)
        images_train.append(img)

    # # image to numpy array
    # images_arr = []
    # for x in range(len(images_train)):
    #     images_arr.append(np.array(images_train[x]))
    return images_train

    