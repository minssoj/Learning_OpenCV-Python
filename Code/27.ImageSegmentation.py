# =================================================
# minso.jeong@daum.net
# 27. 이미지 히스토그램 배경투사
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# =====================* arrangement *============================
# 1. M : 찾고자 하는 객체의 컬러 히스토그램, I : 원본 이미지의 컬러 히스토그램
# 2. R = M/I, B(x, y) = R[h(x, y), s(x, y)], B(x, y) = min(B(x, y), 1)
# 3. B = D*B (D : 원형 커널)
# 4. 픽셀값이 가장 밝은 부분이 우리가 원하는 객체, thresholding 처리
# 5. 원본 이미지와의 비트연산
# ================================================================

ix, iy = -1, -1
mode = False
img1, img2 = None, None

# 원본 이미지에서 마우스로 사각형 영역을 지정하면 해당 영역과 비슷한 부분을 추출하여 화면에 디스플레이
def onMouse(event, x, y, flag, param):
	global ix, iy, mode, img1, img2
	if event == cv.EVENT_LBUTTONDOWN:
		mode = True
		ix, iy = x, y
	elif event == cv.EVENT_MOUSEMOVE:
		if mode:
			img1 = img2.copy()
			cv.rectangle(img1, (ix, iy), (x, y), (0, 0, 255), 2)
			cv.imshow('original', img1)
	elif event == cv.EVENT_LBUTTONUP:
		mode = False
		if ix >= x or iy >= y:
			return
		cv.rectangle(img1, (ix, iy), (x, y), (0, 0, 255), 2)
		roi = img1[iy:y, ix:x]
		backProjection(img2, roi)
	return

# 마우스로 지정한 대상과 원본 이미지를 가지고 히스토그램 배경 투사 알고리즘을 구현한 부분
def backProjection(img, roi):
	hsv = cv.cvtColor(roi, cv.COLOR_BGR2HSV)
	hsvt = cv.cvtColor(img, cv.COLOR_BGR2HSV)

	# Process 1
	roihist = cv.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
	# cv2.normalize(original_array, result_array, min value, max_value, 방식)
	cv.normalize(roihist, roihist, 0, 255, cv.NORM_MINMAX)
	# Process 2
	dst = cv.calcBackProject([hsvt], [0, 1], roihist, [0, 180, 0, 256], 1)
	disc = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
	# Process 3
	cv.filter2D(dst, -1, disc, dst)
	# Process 4
	ret, thr = cv.threshold(dst, 50, 255, 0)
	thr = cv.merge((thr, thr, thr))
	res = cv.bitwise_and(img, thr)

	cv.imshow('backproj', res)
# 원본 이미지와 이미지 히스토그램 배경 투사가 적용된 결과 이미지는 각각 img1. img2에 담기
# img1과 img2는 전역변수 선언, 마우스 이벤트 처리를 위해 콜백 함수 지정
# ESC 누르면 종료
def main():
	global img1, img2

	img1 = cv.imread('../Images/34.Ji.jpg')
	img2 = img1.copy()

	cv.namedWindow('original'), cv.namedWindow('backproj')
	cv.setMouseCallback('original', onMouse, param=None)

	cv.imshow('backproj', img2)

	while True:
		cv.imshow('original', img1)
		k = cv.waitKey(1) & 0xFF
		if k == 27:
			break
	cv.destroyAllWindows()

main()
