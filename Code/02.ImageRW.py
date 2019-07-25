import numpy as np
import cv2
import matplotlib.pyplot as plt

def showImage():
	imgF = '../Images/01.kakao.png'
	img = cv2.imread(imgF, cv2.IMREAD_COLOR)

	cv2.namedWindow('kakao', cv2.WINDOW_NORMAL)	# Control window size
	# cv2.namedWindow('kakao', cv2.AUTOSIZE)
	cv2.imshow('kakao', img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def showImage_Mat():
	imgF = '../Images/01.kakao.png'
	img = cv2.imread(imgF, cv2.IMREAD_GRAYSCALE)
	plt.imshow(img, cmap='gray', interpolation='bicubic')
	plt.xticks([])
	plt.yticks([])
	plt.title('kakao')
	plt.show()

def writeImage():
	imgF = '../Images/01.kakao.png'
	img = cv2.imread(imgF, cv2.IMREAD_COLOR)
	cv2.imshow('kakao', img)

	k = cv2.waitKey(0) & 0xFF

	if k == 27:	# Enter the ESC key
		cv2.destroyAllWindows()
	elif k == ord('c'):
		cv2.imwrite('../Images/01.kakao.jpg', img)
		print("saved!")
		cv2.destroyAllWindows()


# Read Image
#showImage()
showImage_Mat()
# Write Image
#writeImage()