import cv2
import numpy as np
import os
from os import listdir
import extractor
import eigenface


datasetPath = os.getcwd() + "\\test\\dataset"
inputPath = os.getcwd() + "\\test\\input"
# print(datasetPath)

# Extract all dataset to image_train
images_arr = extractor.extractImages(datasetPath)
print(images_arr)

# Extract input image
test_face = extractor.extractImages(inputPath)[0]

# Checking the size of a single image
# print(test_face.shape)

# Diplay image 1
# cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('image', test_face)
# cv2.waitKey()


eigenface = eigenface.Eigenfaces(images_arr)
for i in range(len(eigenface)):
    string = "image"+str(i)+".jpg"
    cv2.imwrite(string,np.int_(eigenface[i]))

