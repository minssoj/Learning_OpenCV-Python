# =================================================
# minso.jeong@daum.net
# 21. 이미지 Contour 응용 4
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# A. Convexity Defects
def contour():
	img = cv.imread('../Images/23.star.jpg')
	gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	ret, thr = cv.threshold(gray_img, 127, 255, 0)
	_, contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	contour = contours[0]
	hull = cv.convexHull(contour)
	cv.drawContours(img, [hull], 0, (0, 0, 255), 2)
	hull = cv.convexHull(contour, returnPoints=False)
	defects = cv.convexityDefects(contour, hull)
	
	for i in range(defects.shape[0]):
		sp, ep, fp, dist = defects[i, 0]
		start = tuple(contour[sp][0])
		end = tuple(contour[ep][0])
		farthest = tuple(contour[fp][0])
		cv.circle(img, farthest, 5, (0, 255, 0), -1)
	cv.imshow('defects', img)
	cv.waitKey(0)
	cv.destroyAllWindows()	
#contour()

# B. 어느 한 점에서 도형까지 최단거리 구하기
def min_distance():
	img = cv.imread('../Images/23.star.jpg')
	gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	ret, thr = cv.threshold(gray_img, 127, 255, 0)
	_, contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
	contour = contours[0]
	cv.drawContours(img, [contour], 0, (0, 255, 0), 2)

	outside = (55, 70)
	inside = (280, 300)

	# False이면 return값 - 외부 -1 , contour 위 0, 내부 1 
	dist1= cv.pointPolygonTest(contour, outside, True)
	dist2= cv.pointPolygonTest(contour, inside, True)

	print('contour에서 (%d, %d)까지의 거리 : %.3f' %(outside[0], outside[1], dist1))
	print('contour에서 (%d, %d)까지의 거리 : %.3f' %(inside[0], inside[1], dist2))

	cv.circle(img, outside, 3, (0, 255, 0), -1)
	cv.circle(img, inside, 3, (255, 0, 255), -1)

	cv.imshow('defects', img)
	cv.waitKey(0)
	cv.destroyAllWindows()	

# min_distance()

# C. 모양 비교하기
CONTOURS_MATCH_l1 = 1
CONTOURS_MATCH_l2 = 2
CONTOURS_MATCH_l3 = 3

def shape_compare():
	imgfile_list = ['../Images/23.star.jpg', '../Images/24.star.jpg', '../Images/25.star.jpg', '../Images/27.star.jpg', '../Images/26.diamond.jpg']
	wins = map(lambda x: 'img' + str(x), range(5))
	wins = list(wins)
	imgs = []
	contour_list = []

	i = 0
	for imgfile in imgfile_list:
		img = cv.imread(imgfile, cv.IMREAD_GRAYSCALE)
		imgs.append(img)
		ret, thr = cv.threshold(img, 127, 255, 0)
		_, contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
		contour_list.append(contours[0])
		i += 1
	for i in range(4):
		cv.imshow(wins[i+1], imgs[i+1])
		ret = cv.matchShapes(contour_list[0], contour_list[i+1], CONTOURS_MATCH_l1, 0.0)
		print(ret)
	cv.waitKey(0)
	cv.destroyAllWindows()

shape_compare()
