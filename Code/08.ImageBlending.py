# =================================================
# minso.jeong@daum.net
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv

# 이미지 더하기
def addImage(imgfile1, imgfile2):
	img1 = cv.imread(imgfile1)
	img2 = cv.imread(imgfile2)
	cv.imshow('img1', img1)
	cv.imshow('img2', img2)
	add_img1 = img1 + img2
	add_img2 = cv.add(img1, img2)
	cv.imshow('+', add_img1)
	cv.imshow('add', add_img2)
	cv.waitKey(0)
	cv.destroyAllWindows()

# Image Blending
def onMouse(x):
	pass
def imgBlending(imgfile1, imgfile2):
	img1 = cv.imread(imgfile1)
	img2 = cv.imread(imgfile2)
	cv.namedWindow('imgPane')
	cv.createTrackbar('Blending', 'imgPane', 0 , 100, onMouse)
	mix = cv.getTrackbarPos('Blending', 'imgPane')
	while True:
		img = cv.addWeighted(img1, float(100-mix)/100, img2, float(mix)/100, 0)
		cv.imshow('imgPane', img)
		k = cv.waitKey(1) & 0xFF
		if k == 27:
			break;
		mix = cv.getTrackbarPos('Blending', 'imgPane')
	cv.destroyAllWindows()

# 이미지 비트연산
def bitOperation(hpos, vpos):
	img1 = cv.imread('../Images/04.Ji.jpg')
	img2 = cv.imread('../Images/05.logo.jpg')
	# 01. 로고 삽일할 영역 지정
	rows, cols, channels = img2.shape
	roi = img1[vpos:rows+vpos, hpos:cols+hpos]
	# 02. 로고를 위한 마스크 및 역마스크 생성
	img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
	print(img2gray[10,10])
	ret, mask = cv.threshold(img2gray, 100, 255, cv.THRESH_BINARY)
	mask_inv = cv.bitwise_not(mask)
	# 03. ROI에서 로고에 해당하는 부분만 검정색으로 만들기
	img1_bg = cv.bitwise_and(roi, roi, mask=mask_inv)
	# 04. 로고 이미지에서 로고 부분만 추출하기
	img2_fg = cv.bitwise_and(img2, img2, mask=mask)
	# 05. 로고 이미지 배경을 cv2.add로 투명으로 만들고 ROI에 로고 이미지 십입
	dst = cv.add(img1_bg, img2_fg)
	img1[vpos:rows+vpos, hpos:cols+hpos] = dst
	cv.imshow('result', img1)
	cv.waitKey(0)
	cv.destroyAllWindows()

# addImage('../Images/03.hallstatt.jpg', '../Images/04.Ji.jpg')
#imgBlending('../Images/03.hallstatt.jpg', '../Images/04.Ji.jpg')
bitOperation(10, 10)