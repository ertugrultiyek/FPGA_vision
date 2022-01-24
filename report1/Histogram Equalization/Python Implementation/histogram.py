import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("university.png")

height, width = img.shape[:2]

equalized = np.zeros(shape=[height,width], dtype=np.uint8)

hist = list([] for i in range(256))

for y in range(height):
	for x in range(width):
		hist[np.uint8((int(img[y,x,0]) + int(img[y,x,1]) + int(img[y,x,2])) /3)-1].append({
			"x" : x,
			"y" : y
		});

a= range(256)
n = list()
for i in a:
	if i<1:
		n.append(len(hist[i])/(width*height))
	else:
		n.append(len(hist[i])/(width*height)+n[i-1])


for k in range(len(hist)):
	val = 0
	for cnt in range(k):
		val += len(hist[cnt])/(width*height)
	val *= (len(hist)-1)
	# val += k
	# val /= 2
	for px in hist[k]:
		equalized[px["y"],px["x"]] = val

for y in range(height):
	for x in range(width):
		hist[np.uint8((equalized[y,x])-1)].append({
			"x" : x,
			"y" : y
		});

nn = list()
for i in a:
	if i<1:
		nn.append(len(hist[i])/(width*height))
	else:
		nn.append(len(hist[i])/(width*height)+nn[i-1])


plt.plot(a, nn)
plt.plot(a, n)

		# naming the x axis
plt.xlabel('intensity level')
# naming the y axis
plt.ylabel('# of pixels')

# giving a title to my graph
plt.title('Both Histogram CDF in Same Graph')

plt.show()

cv.imwrite("C:/Users/MAHSES/Downloads/FPGA_vision-main/FPGA_vision-main/report1/Histogram Equalization/Python Implementation/output/equalized.tif", equalized)
cv.imwrite("C:/Users/MAHSES/Downloads/FPGA_vision-main/FPGA_vision-main/report1/Histogram Equalization/Python Implementation/output/original.tif", img)
cv.waitKey(0)
