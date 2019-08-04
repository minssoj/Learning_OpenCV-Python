# =================================================
# minso.jeong@daum.net
# 19. 이미지 Contour 응용 2
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# A. Convex Hull
def convex():
	img = cv.imread('../Images/20.convexhull.png')
	img1 = img.copy()
	gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	ret, thr = cv.threshold(gray_img, 127, 255, 0)
	_, contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	contour = contours[1]
	cv.drawContours(img, [contour], 0, (0, 255, 0), 3)
	check = cv.isContourConvex(contour)
	if not check:
		hull = cv.convexHull(contour)
		cv.drawContours(img1, [hull], 0, (0, 255, 0), 3)
		cv.imshow('convexhull', img1)
	cv.imshow('contour', img)
	cv.waitKey(0)
	cv.destroyAllWindows()
#convex()

# B. Bounding Rectangle & Minimum Area Rectangle
def convex_rec():
	img = cv.imread('../Images/21.star.png')
	gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	ret, thr = cv.threshold(gray_img, 127, 255, 0)
	_, contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	contour = contours[5]
	x, y, w, h = cv.boundingRect(contour)
	cv.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255),3)

	rect = cv.minAreaRect(contour)
	box = cv.boxPoints(rect)
	box = np.int0(box)

	cv.drawContours(img, [box], 0, (0, 255, 0), 3)
	cv.imshow('rectangle', img)
	cv.waitKey(0)
	cv.destroyAllWindows()
convex_rec()

# Minimum Enclosing Circle & Fitting Ellipse & Fitting Line
def convex_ellipse():
	img = cv.imread('../Images/21.star.png')
	gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	rows, cols = img.shape[:2]
	ret, thr = cv.threshold(gray_img, 127, 255, 0)
	_, contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	contour = contours[5]
	(x, y), r = cv.minEnclosingCircle(contour)
	center = (int(x), int(y))
	r = int(r)
	cv.circle(img, center, r, (255, 0, 0), 3)

	ellipse = cv.fitEllipse(contour)
	cv.ellipse(img, ellipse, (0, 255, 0), 3)

	[vx, vy, x, y] = cv.fitLine(contour, cv.DIST_L2, 0, 0.01, 0.01)
	ly = int((-x*vy/vx)+y)
	ry = int(((cols-x)*vy/vx)+y)
	cv.line(img, (cols-1, ry), (0, ly), (0, 0, 255), 2)

	cv.imshow('fitting', img)
	cv.waitKey(0)
	cv.destroyAllWindows()

#convex_ellipse()
