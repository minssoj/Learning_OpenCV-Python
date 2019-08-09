# =================================================
# minso.jeong@daum.net
# 25. CLAHE
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

def clahe():
	img = cv.imread('../Images/31.light.jpg', cv.IMREAD_GRAYSCALE)
	clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
	img2 = clahe.apply(img)
	res = np.hstack((img, img2))
	cv.imshow('clahe', res)
	cv.waitKey(0)
	cv.destroyAllWindows()
clahe()