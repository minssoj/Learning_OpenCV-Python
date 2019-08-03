# =================================================
# minso.jeong@daum.net
# 11. 이미지 변환 - 리사이징, 이동, 회전, 원근효과
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# A. Image Resizing
def transform_resize():
	img = cv.imread('../Images/11.Ji.jpg')
	h, w = img.shape[:2]
	img2 = cv.resize(img, None, fx=0.5, fy=1, interpolation=cv.INTER_AREA)
	img3 = cv.resize(img, None, fx=1, fy=0.5, interpolation=cv.INTER_AREA)
	img4 = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_AREA)
	cv.imshow('original', img)
	cv.imshow('fx=0.5', img2)
	cv.imshow('fy=0.5', img3)
	cv.imshow('fx=0.5, fy=0.5', img4)
	cv.waitKey(0)
	cv.destroyAllWindows()

#transform_resize()

# B. Image Shift
def transform_shift():
	img = cv.imread('../Images/11.Ji.jpg')
	h, w = img.shape[:2]
	M1 = np.float32([[1, 0, 100], [0, 1, 50]])
	M2 = cv.getRotationMatrix2D((w/2, h/2), 45, 1)
	M3 = cv.getRotationMatrix2D((w/2, h/2), 90, 1)
	img2 = cv.warpAffine(img, M1, (w, h))
	img3 = cv.warpAffine(img, M2, (w, h))
	img4 = cv.warpAffine(img, M3, (w, h))
	cv.imshow('original', img)
	cv.imshow('shift image', img2)
	cv.imshow('45-rotate image', img3)
	cv.imshow('90-rotate image', img4)
	cv.waitKey(0)
	cv.destroyAllWindows()

#transform_shift()

# C. Image Forced
def transform_forced():
	img = cv.imread('../Images/12.sudoku.png')
	h, w = img.shape[:2]
	pts1_a = np.float32([[50, 50], [200, 50], [20, 200]])
	pts2_a = np.float32([[10, 100], [200, 50], [100, 250]])
	M1 = cv.getAffineTransform(pts1_a, pts2_a)
	img2 = cv.warpAffine(img, M1, (w, h))
	pts1_p = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])
	pts2_p = np.float32([[56, 65], [368, 52], [28, 387], [389, 390]])
	M2 = cv.getPerspectiveTransform(pts1_p, pts2_p)
	img3 = cv.warpPerspective(img, M2, (w, h))
	cv.imshow('original', img)
	cv.imshow('Affine transform', img2)
	cv.imshow('Perspective transform', img3)
	cv.waitKey(0)
	cv.destroyAllWindows()

transform_forced()



