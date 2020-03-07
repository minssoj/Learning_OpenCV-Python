# =================================================
# minso.jeong@daum.net
# 32. 허프변환을 이용하 직선찾기
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
#import matplotlib.pyplot as plt

def hough_line(threshold):
	img = cv.imread('../Images/37.sudoku.png')
	img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	edges = cv.Canny(img_gray, 50, 150, apertureSize = 3)

	# 1: binary image, 2: 거리, 3: 각도, 4: 직선이라고 판별할 threshold
	# threshold 값에 따라 정확도 달라짐
	lines = cv.HoughLines(edges, 1, np.pi/180, threshold)

	for line in lines:
		r, theta = line[0]
		a = np.cos(theta)
		b = np.sin(theta)
		x0 = a*r
		y0 = b*r
		x1 = int(x0+1000*(-b))
		y1 = int(y0+1000*(+a))
		x2 = int(x0-1000*(-b))
		y2 = int(y0-1000*(+a))

		cv.line(img, (x1, y1), (x2, y2), (0,0,255),1)


	cv.imshow('result', img)
	cv.waitKey(0)
	cv.destroyAllWindows()

def hough(threshold, minLineLength, maxLineGap):
	img = cv.imread('../Images/37.sudoku.png')
	img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	edges = cv.Canny(img_gray, 50, 150, apertureSize = 3)

	# minLineLength : 해당 값 이하로 주어진 선길이는 직선으로 생각하지 않음
	# maxLineGap : 찾은 직선이 해당 값 이상 떨어져 있으면 다른 직선으로 생각
	lines = cv.HoughLinesP(edges, 1, np.pi/180, threshold, minLineLength, maxLineGap)

	for line in lines:
		x1, y1, x2, y2 = line[0]
		cv.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

	cv.imshow('result', img)
	cv.waitKey(0)
	cv.destroyAllWindows()

#hough_line(140)
hough(140, 100, 10)
