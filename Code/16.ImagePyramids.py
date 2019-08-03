# =================================================
# minso.jeong@daum.net
# 16. 이미지 피라미드
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# A. Gaussian Pyramids
# cv.pyrDown(img)
# cv.pyrUp(img)
def pyramid_down():
	img = cv.imread('../Images/11.Ji.Jpg', cv.IMREAD_GRAYSCALE)
	tmp = img.copy()

	titles = ['original', 'level1', 'level2', 'level3']
	g_down = []
	g_down.append(tmp)

	for i in range(3):
		tmp1 = cv.pyrDown(tmp)
		g_down.append(tmp1)
		tmp = tmp1

	for i in range(4):
		cv.imshow(titles[i], g_down[i])
	cv.waitKey(0)
	cv.destroyAllWindows()

def pyramid_up():
	img = cv.imread('../Images/11.Ji.Jpg', cv.IMREAD_GRAYSCALE)
	tmp = img.copy()

	titles = ['original', 'level1', 'level2']
	g_down = []
	g_up = []
	g_down.append(tmp)

	for i in range(3):
		tmp1 = cv.pyrDown(tmp)
		g_down.append(tmp1)
		tmp = tmp1
	cv.imshow('level3', tmp)

	for i in range(3):
		tmp = g_down[i+1]
		tmp1 = cv.pyrUp(tmp)
		g_up.append(tmp1)

	for i in range(3):
		cv.imshow(titles[i], g_up[i])
	cv.waitKey(0)
	cv.destroyAllWindows()
#pyramid_down()
#pyramid_up()

# B. Laplacian Pyramids (Results of Gaussian Pyramids)
def pyramid_laplacian():
	img = cv.imread('../Images/11.Ji.Jpg', cv.IMREAD_GRAYSCALE)
	tmp = img.copy()

	titles = ['original', 'level1', 'level2', 'level3']
	g_down = []
	g_up = []
	img_shape = []

	g_down.append(tmp)
	img_shape.append(tmp.shape)

	for i in range(3):
		tmp1 = cv.pyrDown(tmp)
		g_down.append(tmp1)
		img_shape.append(tmp1.shape)
		tmp = tmp1
	for i in range(3):
		tmp = g_down[i+1]
		tmp1 = cv.pyrUp(tmp)
		tmp = cv.resize(tmp1, dsize=(img_shape[i][1], img_shape[i][0]), interpolation=cv.INTER_CUBIC)
		g_up.append(tmp)

	for i in range(3):
		tmp = cv.subtract(g_down[i], g_up[i])
		cv.imshow(titles[i], tmp)

	cv.waitKey(0)
	cv.destroyAllWindows()

pyramid_laplacian()
