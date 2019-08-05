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

