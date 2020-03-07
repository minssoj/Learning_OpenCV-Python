# =================================================
# minso.jeong@daum.net
# 33. 허프변환을 이용한 원 찾기
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
#import matplotlib.pyplot as plt

def houghCircle():
	img1 = cv.imread('../images/38.shape.jpg')
	img2 = img1.copy()

	img2 = cv.GaussianBlur(img2, (3,3), 0)			# 필수는 아님 (처리를 해줘야 잘찾음)
	gray_img = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)

	# 4번째 인자 : 찾은 원들의 중심간 최소 거리, 중심간의 거리가 해당 값보다 작으면 나중에 찾은 원은 무시
	circles = cv.HoughCircles(gray_img, cv.HOUGH_GRADIENT, 1, 30, param1=60, param2=50, minRadius=0, maxRadius=0)

	if circles is not None:
		circles = np.uint16(np.around(circles))

		for i in circles[0, :]:
			cv.circle(img1, (i[0], i[1]), i[2], (255, 255, 0), 2)

		cv.imshow('Result', img1)
		cv.waitKey(0)
		cv.destroyAllWindows()
	else:
		print("Not found Circle")


houghCircle()
