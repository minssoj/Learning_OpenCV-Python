# =================================================
# minso.jeong@daum.net
# 31. 템플릿 매칭2
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv

def templateMatching(threshold):
	img1 = cv.imread('../Images/35.whole.png')
	img1_gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
	template = cv.imread('../Images/36.part.png', cv.IMREAD_GRAYSCALE)
	w, h = template.shape[::-1]


	result = cv.matchTemplate(img1_gray, template, cv.TM_CCOEFF_NORMED)
	# 좌표를 튜플로 리턴
	location = np.where(result >= threshold)

	# Zip : location의 순서를 거꾸로 하여 튜플로 묶고 리스트화
	for pt in zip(*location[::-1]):
		# Detection 상자 그리기
		cv.rectangle(img1, pt, (pt[0]+w, pt[1]+h), (0, 0, 255), 2)

	cv.imshow('result', img1)
	cv.waitKey(0)
	cv.destroyAllWindows()


templateMatching(0.8)