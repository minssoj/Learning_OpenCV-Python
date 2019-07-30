# =================================================
# minso.jeong@daum.net
# 09. 색공간 바꾸기 및 색 추적
# Reference : samsjang@naver.com
# =================================================

import numpy as np
import cv2 as cv

# A. 색공간 변경하기
def hsv():
	B = np.uint8([[[255,0,0]]])
	G = np.uint8([[[0,255,0]]])
	R = np.uint8([[[0,0,255]]])
	B_hsv = cv.cvtColor(B, cv.COLOR_BGR2HSV)
	G_hsv = cv.cvtColor(G, cv.COLOR_BGR2HSV)
	R_hsv = cv.cvtColor(R, cv.COLOR_BGR2HSV)
	print('HSV for BLUE: ', B_hsv)
	print('HSV for GREEN: ', G_hsv)
	print('HSV for RED: ', R_hsv)
#hsv()

# B. 색 추적하기
def tracking():
	try:
		print("Camera Working!")
		#cap = cv.VideoCapture(0)
		cap = cv.VideoCapture('../Images/06.Banner.mp4')
	except:
		print('failed Working Camer!')
		return
	while True:
		ret, frame = cap.read()
		# 01. BGR -> HSV
		hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
		# 02. HSV -> BGR로 가정할 범위
		low_B = np.array([110, 100, 100])
		up_B = np.array([130, 255, 255])
		low_G = np.array([50, 100, 100])
		up_G = np.array([70, 255, 255])
		low_R = np.array([-10, 100, 100])
		up_R = np.array([10, 255, 255])
		# 03. 추출을 위한 임계값
		mask_B = cv.inRange(hsv, low_B, up_B)
		mask_G = cv.inRange(hsv, low_G, up_G)
		mask_R = cv.inRange(hsv, low_R, up_R)
		# 04. mask와 원본 이미지를 비트 연산함
		res1 = cv.bitwise_and(frame, frame, mask=mask_B)
		res2 = cv.bitwise_and(frame, frame, mask=mask_G)
		res3 = cv.bitwise_and(frame, frame, mask=mask_R)
		cv.imshow('original', frame)
		cv.imshow('Blue', res1)
		cv.imshow('Greem', res2)
		cv.imshow('Red', res3)
		k = cv.waitKey(1) & 0xFF
		if k == 27:
			break
	cv.destroyAllWindows()
tracking()