# =================================================
# minso.jeong@daum.net
# Reference : samsjang@naver.com
# =================================================

import numpy as np
import cv2 as cv

img = cv.imread('../Images/03.hallstatt.jpg')
setting = 6

if setting == 1:
	# 이미지 픽셀 값 얻기
	px = img[340,200]
	print(px)

elif setting == 2:
	# 이미지 픽셀 값 얻기
	B = img.item(340,200,0)
	G = img.item(340,200,1)
	R = img.item(340,200,2)
	BGR = [B, G, R]
	print(BGR)

elif setting == 3:
	# 이미지 속성 얻기
	print(img.shape)
	print(img.size)
	print(img.dtype)

elif setting == 4:
	# 이미지 ROI 설정
	cv.imshow('original', img)
	subimg = img[300:400, 350:750]
	cv.imshow('cutting',subimg)
	# Merge subimg & original img
	img[300:400, 0:400] = subimg
	print(img.shape)
	print(subimg.shape)
	cv.imshow('merge', img)
	cv.waitKey(0)
	cv.destroyAllWindows()

elif setting == 5:
	# 이미지 채널 분할
	B, G, R = cv.split(img)
	print(img[100, 100])
	print(B[100, 100],G[100, 100],R[100, 100])
	cv.imshow('Blue Ch', B)
	cv.imshow('Green Ch', G)
	cv.imshow('Red Ch', R)
	cv.waitKey(0)
	cv.destroyAllWindows()


elif setting == 6:
	# 이미지 합치기
	B, G, R = cv.split(img)
	merged_img = cv.merge((B, G, R))
	cv.imshow('Merge', merged_img)
	cv.waitKey(0)
	cv.destroyAllWindows()

