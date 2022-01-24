import cv2
import numpy as np
import histogram

img = cv2.imread("forest.tif")


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

decompressed = np.zeros(shape=[height,width,3], dtype=np.uint8)

for y in range(height):
	for x in range(width):
		if((y%2 == 0)):
			if(x%2 == 0):
				decompressed[y,x,0] = np.uint8((int(bayer[y,x-1]) + int(bayer[y,x+1]))/2)
				decompressed[y,x,1] = bayer[y,x]
				decompressed[y,x,2] = np.uint8((int(bayer[y-1,x]) + int(bayer[y+1,x]))/2)
			else:
				decompressed[y,x,0] = bayer[y,x]
				decompressed[y,x,1] = np.uint8((int(bayer[y-1,x]) + int(bayer[y+1,x]) + int(bayer[y,x-1]) + int(bayer[y,x+1]))/4)
				decompressed[y,x,2] = np.uint8((int(bayer[y-1,x-1]) + int(bayer[y+1,x-1]) + int(bayer[y-1,x+1]) + int(bayer[y+1,x+1]))/4)
		else:
			if(x%2 == 0):
				decompressed[y,x,0] = np.uint8((int(bayer[y-1,x-1]) + int(bayer[y+1,x-1]) + int(bayer[y-1,x+1]) + int(bayer[y+1,x+1]))/4)
				decompressed[y,x,1] = np.uint8((int(bayer[y-1,x]) + int(bayer[y+1,x]) + int(bayer[y,x-1]) + int(bayer[y,x+1]))/4)
				decompressed[y,x,2] = bayer[y,x]
			else:
				decompressed[y,x,0] = np.uint8((int(bayer[y-1,x]) + int(bayer[y+1,x]))/2)
				decompressed[y,x,1] = bayer[y,x]
				decompressed[y,x,2] = np.uint8((int(bayer[y,x-1]) + int(bayer[y,x+1]))/2)

cv2.imwrite('C:/Users/MAHSES/Downloads/FPGA_vision-main/FPGA_vision-main/report1/Bayer Format/python implementation/bayerFormat.tif', bayer)
cv2.imwrite('C:/Users/MAHSES/Downloads/FPGA_vision-main/FPGA_vision-main/report1/Bayer Format/python implementation/decompressed.tif', decompressed)
