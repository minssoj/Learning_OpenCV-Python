# =================================================
# minso.jeong@daum.net
# 18. 이미지 Contour 응용 1
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

img_path = '../Images/05.logo.jpg'

# A. 이미지 모멘트
def moment():
	img = cv.imread(img_path)
	gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	ret, thr = cv.threshold(gray_img, 127, 255, 0)
	_, contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	contour = contours[0]
	mmt = cv.moments(contour)
	for key, val in mmt.items():
		print('%s:\t%.5f' %(key, val))
	cx = int(mmt['m10']/mmt['m00'])
	cy = int(mmt['m01']/mmt['m00'])
	print(cx, cy)
#moment()

def contour():
	img = cv.imread(img_path)
	gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	ret, thr = cv.threshold(gray_img, 127, 255, 0)
	_, contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	contour = contours[5]

	area = cv.contourArea(contour)
	perimeter = cv.arcLength(contour, True)
	cv.drawContours(img, [contour], 0, (0, 0, 255), 1)

	print('Contour 면적: ', area)
	print('Contour 길이: ', perimeter)

	cv.imshow('Contour', img)
	cv.waitKey(0)
	cv.destroyAllWindows()

#contour()

# B. Contour 근사법
def contour_apx():
	img = cv.imread('../Images/19.contour.png')
	img1 = cv.imread('../Images/19.contour.png')
	img2 = cv.imread('../Images/19.contour.png')
	gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	ret, thr = cv.threshold(gray_img, 127, 255, 0)
	_, contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	contour = contours[0]
	cv.drawContours(img, [contour], 0, (255, 0, 0), 1)
	epsilon1 = 0.01* cv.arcLength(contour, True)
	epsilon2 = 0.1 * cv.arcLength(contour, True)
	approx1 = cv.approxPolyDP(contour, epsilon1, True)
	approx2 = cv.approxPolyDP(contour, epsilon2, True)
	cv.drawContours(img1, [approx1], 0, (0, 255, 0), 3)
	cv.drawContours(img2, [approx2], 0, (0, 255, 0), 3)
	plt.subplot(1,3,1), plt.imshow(img)
	plt.title('contour'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,3,2), plt.imshow(img1)
	plt.title('Approx1'), plt.xticks([]), plt.yticks([])
	plt.subplot(1,3,3), plt.imshow(img2)
	plt.title('Approx2'), plt.xticks([]), plt.yticks([])
	plt.show()
contour_apx()


