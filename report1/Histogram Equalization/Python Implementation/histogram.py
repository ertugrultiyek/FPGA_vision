import cv2 as cv
import numpy as np

img = cv.imread("university.png")

height, width = img.shape[:2]

equalized = np.zeros(shape=[height,width], dtype=np.uint8)

hist = list([] for i in range(512))

for y in range(height):
	for x in range(width):
		hist[img[y,x,0]].append({
			"x" : x,
			"y" : y
		});

for k in range(len(hist)):
	val = 0
	for cnt in range(k):
		val += len(hist[cnt])/(width*height)
	val *= (len(hist)-1)
	val += k
	val /= 2
	for px in hist[k]:
		equalized[px["y"],px["x"]] = val

cv.imshow("equalized", equalized)
cv.imshow("original", img)
cv.waitKey(0)
