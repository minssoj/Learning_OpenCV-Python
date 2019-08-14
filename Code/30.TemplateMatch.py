# =================================================
# minso.jeong@daum.net
# 30. 템플릿 매칭
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def templateMatching():
	img1 = cv.imread('../Images/11.Ji.Jpg', cv.IMREAD_GRAYSCALE)
	img2 = img1.copy()

	template = cv.imread('../Images/11.Ji_ROI.jpg', cv.IMREAD_GRAYSCALE)
	w, h = template.shape[::-1]

	methods = ['cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR', 'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
	
	for i in methods:
		img1 = img2.copy()
		method = eval(i)

		try:
			res = cv.matchTemplate(img1, template, method)
			min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
		except:
			print('error', i)
			continue
		if method in [cv.TM_SQDIFF, cv.TM_SQDIFF_NORMED]:
			top_left = min_loc
		else:
			top_left = max_loc
		bottom_right = (top_left[0]+w, top_left[1]+h)
		cv.rectangle(img1, top_left, bottom_right, 255, 2)

		plt.subplot(1,2,1), plt.imshow(res, cmap='gray')
		plt.title('Matching Result'), plt.xticks([]), plt.yticks([])

		plt.subplot(1,2,2), plt.imshow(img1, cmap='gray')
		plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
		plt.suptitle(i)

		plt.show()
templateMatching()