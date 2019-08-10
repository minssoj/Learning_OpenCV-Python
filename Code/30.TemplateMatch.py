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
	w, h = template.shape[:,:,-1]

	methods = []