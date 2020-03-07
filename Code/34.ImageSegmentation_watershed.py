# =================================================
# minso.jeong@daum.net
# 34. watershed 알고리즘을 이용한 이미지 분할
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
from scipy.ndimage import label

def watershed():
	img = cv.imread('../Images/39.coin.jpg')
	gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	# Binary Image로 변환
	ret, thr = cv.threshold(gray_img, 0, 255, cv.THRESH_BINARY_INV + cv.THRESH_OTSU)

	kernel = np.ones((3,3), np.uint8)

	# 이미지 Noise 제거를 위한 Opening (Chapter. 13 참고) 
	opening = cv.morphologyEx(thr, cv.MORPH_OPEN, kernel, iterations=2)

	# 동전과 배경의 경계 추출
	border = cv.dilate(opening, kernel, iterations=3)
	border = border - cv.erode(border, None)

	# 
	dt = cv.distanceTransform(opening, cv.DIST_L2, 5)
	dt = ((dt-dt.min()) / (dt.max()-dt.min())*255).astype(np.uint8)
	ret, dt = cv.threshold(dt, 180, 255, cv.THRESH_BINARY)

	marker, ncc = label(dt)
	marker = marker * (255/ncc)

	marker[border == 255] = 255
	marker = marker.astype(np.int32)
	cv.watershed(img, marker)

	marker[marker == -1] = 0
	marker = marker.astype(np.int8)
	marker = 255 - marker

	marker[marker != 255] = 0
	marker = cv.dilate(marker, None)
	img[marker == 255] = (0, 0, 255)

	cv.imshow('Result', img)
	cv.waitKey(0)
	cv.destroyAllWindows()

watershed()

