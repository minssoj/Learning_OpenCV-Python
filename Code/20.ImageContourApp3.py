# =================================================
# minso.jeong@daum.net
# 20. 이미지 Contour 응용 3
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# =====================* arrangement *============================
# 01. Aspect Ratic (종횡비)
# x, y, w, h = cv2.boundingRect(cnt), aspect_ratio = float(w)/h
# 02. Extent (Contour 넓이와 Contour 외접 직사각형의 넓이비)
# area = cv2.contoourArea(cnt), x, y, w, h = cv2.boundingRect(cnt)
# rect_area = w*h, extent = float(area)/rect_area
# 03. Solidity (Contour 넓이와 이 Contour의 Convex Hull 넓이의 비)
# area = cv2.contourArea(cnt), hull = cv2.convexHull(cnt)
# hull_area = cv2.contourArea(hull), solidity = float(area)/hull_area
# 04. Equivalent Diameter (Contour의 넓이와 동일한 넓이를 가진 원의 지름)
# area = cv2.contourArea(cont), equivalent_diameter = np.sqrt(4*area/np.pi)
# 05. Orientation (Contour의 최적 타원의 기울어진 각도)
# (x, y), (MajorAxis, MinorAxis), angle = cv2.fitEllipse(cnt)
# 06. Mask & Pixel Points (객체를 구성하는 모든 점들)
# mask = np.zeros(imgray.shape, np.uint8) 
# cv2.drawContours(mask, [cnt], 0, 255, -1), pixels = cv2.findNonZero(mask)
# 07. Mean Color / Mean Intensity (평균 색상)
# mean_value = cv2.mean(img, mask=mask)
# ================================================================

# A. Image Features
def convex():
	img = cv.imread('../Images/22.korea.jpg')
	gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	ret, thr = cv.threshold(gray_img, 127, 255, 0)
	_, contours, _ = cv.findContours(thr, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

	cnt = contours[30]

	mmt = cv.moments(cnt)
	cx = int(mmt['m10']/mmt['m00'])
	cy = int(mmt['m01']/mmt['m00'])

	x, y, w, h = cv.boundingRect(cnt)
	korea_rect_area = w*h
	korea_area = cv.contourArea(cnt)
	hull = cv.convexHull(cnt)
	hull_area = cv.contourArea(hull)
	ellipse = cv.fitEllipse(cnt)

	aspect_ratio = w/h
	extent = korea_area/korea_rect_area
	solidity = korea_area/hull_area

	print("KOREA aspect_ratio :\t%.3f" %aspect_ratio)
	print("KOREA Extent :\t%.3f" %extent)
	print("KOREA Solidity :\t%.3f" %solidity)
	print("KOREA Orientation : :\t%.3f" %ellipse[2])

	equivalent_diameter = np.sqrt(4*korea_area/np.pi)
	korea_radius = int(equivalent_diameter/2)

	cv.circle(img, (cx, cy), 3, (0, 0, 255), -1)
	cv.circle(img, (cx, cy), korea_radius, (0, 0, 255), 2)
	cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
	cv.ellipse(img, ellipse, (50, 50, 50), 2)

	cv.imshow('KOREA Features', img)
	cv.waitKey(0)
	cv.destroyAllWindows()
#convex()

# B: Extreme Points
# =====================* arrangement *============================
# leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
# rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
# topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
# bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
# ================================================================
