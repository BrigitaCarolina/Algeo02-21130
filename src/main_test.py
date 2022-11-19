import cv2
import numpy as np
import os
from os import listdir
import extractor
import eigenface


datasetPath = os.getcwd() + "\\test\\dataset"
inputPath = os.getcwd() + "\\test\\input"
outputPath = os.getcwd() + "\\test\\output"
# print(datasetPath)

# Extract all dataset to image_train
images_arr = extractor.extractImages(datasetPath)
# print(images_arr)

# Extract input image
test_face = extractor.extractImages(inputPath)

# Checking the size of a single image
# print(test_face.shape)

# Diplay image 1
# cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
# cv2.imshow('image', test_face)
# cv2.waitKey()


eigenfaces,execution_time = eigenface.Eigenfaces(images_arr,test_face)

# for i in range(len(eigenface)):
#     string = "image"+str(i)+".jpg"
#     cv2.imwrite(string,np.int_(eigenface[i]))


cv2.imwrite(os.path.join(outputPath , 'output.jpg'),np.int_(eigenfaces))
print(execution_time)
# cv2.imwrite("/test/output/image.jpg",np.int_(eigenfaces))
