import cv2
import numpy as np
import histogram

img = cv2.imread("kids.tif")

# cv2.imshow("image", img)

height, width = img.shape[:2]

bayer = np.zeros(shape=[height+2,width+2], dtype=np.uint8)

for y in range(1,height):
	for x in range(1,width):
		if((y%2 == 0)):
			if(x%2 == 0):
				bayer[y,x] = img[y,x,1]
			else:
				bayer[y,x] = img[y,x,0]
		else:
			if(x%2 == 0):
				bayer[y,x] = img[y,x,2]
			else:
				bayer[y,x] = img[y,x,1]

# decompressed = np.zeros(shape=[height,width,3], dtype=np.uint8)

decompressed = cv2.cvtColor(bayer, cv2.COLOR_BayerGB2RGB)

# for y in range(height):
# 	for x in range(width):
# 		if((y%2 == 0)):
# 			if(x%2 == 0):
# 				decompressed[y,x,0] = (bayer[y,x-1] + bayer[y,x+1])/2
# 				decompressed[y,x,1] = bayer[y,x]
# 				decompressed[y,x,2] = (bayer[y-1,x] + bayer[y+1,x])/2
# 			else:
# 				decompressed[y,x,0] = bayer[y,x]
# 				decompressed[y,x,1] = (bayer[y-1,x] + bayer[y+1,x] + bayer[y,x-1] + bayer[y,x+1])/4
# 				decompressed[y,x,2] = (bayer[y-1,x-1] + bayer[y+1,x-1] + bayer[y-1,x+1] + bayer[y+1,x+1])/4
# 		else:
# 			if(x%2 == 0):
# 				decompressed[y,x,0] = (bayer[y-1,x-1] + bayer[y+1,x-1] + bayer[y-1,x+1] + bayer[y+1,x+1])/4
# 				decompressed[y,x,1] = (bayer[y-1,x] + bayer[y+1,x] + bayer[y,x-1] + bayer[y,x+1])/4
# 				decompressed[y,x,2] = bayer[y,x]
# 			else:
# 				decompressed[y,x,0] = (bayer[y-1,x] + bayer[y+1,x])/2
# 				decompressed[y,x,1] = bayer[y,x]
# 				decompressed[y,x,2] = (bayer[y,x-1] + bayer[y,x+1])/2

cv2.imshow("original", img)
cv2.imshow("bayer", bayer)
cv2.imshow("decompressed", decompressed)
cv2.waitKey(0);
