# =================================================
# minso.jeong@daum.net
# Reference : samsjang@naver.com
# =================================================

import numpy as np
import cv2 as cv

def onChange(x):
	pass

def trackbar():
	img = np.zeros((200, 512, 3), np.uint8)
	cv.namedWindow('trackbar')

	cv.createTrackbar('B', 'trackbar', 0, 255, onChange)
	cv.createTrackbar('G', 'trackbar', 0, 255, onChange)
	cv.createTrackbar('R', 'trackbar', 0, 255, onChange)
	cv.createTrackbar('0: OFF 1: ON','trackbar', 0, 1, onChange)

	while True:
		cv.imshow('trackbar', img)
		k = cv.waitKey(1) & 0xFF

		if k == 27:
			break

		B = cv.getTrackbarPos('B', 'trackbar')
		G = cv.getTrackbarPos('G', 'trackbar')
		R = cv.getTrackbarPos('R', 'trackbar')
		S = cv.getTrackbarPos('0: OFF 1: ON', 'trackbar')

		if S == 0:	# mode : OFF
			img[:] = 0
		else:
			img[:] = [B,G,R]

	cv.destroyAllWindows()

trackbar()
