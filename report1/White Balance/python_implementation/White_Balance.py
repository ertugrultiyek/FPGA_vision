import cv2
import numpy as np

name = "fruit.jpg"

img = cv2.imread(name)
height, width = img.shape[:2]
balanced = np.zeros(shape=[height, width, 3], dtype=np.uint8)

maxB = 0
avgB = 0
maxG = 0
avgG = 0
maxR = 0
avgR = 0

pxs = width*height

for y in range(height):
    for x in range(width):
        avgB += img[y, x, 0]/pxs
        avgG += img[y, x, 1]/pxs
        avgR += img[y, x, 2]/pxs

        if maxB < img[y, x, 0]:
            maxB = img[y, x, 0]
        if maxG < img[y, x, 1]:
            maxG = img[y, x, 1]
        if maxR < img[y, x, 2]:
            maxR = img[y, x, 2]

# corrB = 255 / (maxB + 1)
# corrG = 255 / (maxG + 1)
# corrR = 255 / (maxR + 1)

corrB = avgG / avgB
corrR = avgG / avgR

for y in range(height):
    for x in range(width):
        if img[y, x, 0] * corrB < 255:
            balanced[y, x, 0] = img[y, x, 0] * corrB

        balanced[y, x, 1] = img[y, x, 1]
        
        if img[y, x, 2] * corrR < 255:
            balanced[y, x, 2] = img[y, x, 2] * corrR

cv2.imwrite("C:/Users/MAHSES/Downloads/FPGA_vision-main/FPGA_vision-main/report1/White Balance/python_implementation/" + name + "_balanced.tif", balanced)

cv2.imshow("original", img)
cv2.imshow("balanced", balanced)
cv2.waitKey(0)
