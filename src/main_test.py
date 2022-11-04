import cv2
import numpy as np
import os
from os import listdir
import extractor


datasetPath = os.getcwd() + "\\test\\dataset"
inputPath = os.getcwd() + "\\test\\input"
# print(datasetPath)

# Extract all dataset to image_train
image_arr = extractor.extractImages(datasetPath)
print(image_arr)

# Extract input image
test_face = extractor.extractImages(inputPath)[0]

# Checking the size of a single image
print(test_face.shape)

# Diplay image 1
cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('image', test_face)
cv2.waitKey()




