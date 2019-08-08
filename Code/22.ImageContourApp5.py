# =================================================
# minso.jeong@daum.net
# 22. 이미지 Contour 응용 5
# Reference : samsjang@naver.com
# =================================================
import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

# A. Contour Hierachy
# =====================* arrangement *============================
# [Next, Previous, First Child, Parent]
# Next : 동일레벨의 다음 Contour 인덱스, 동일레벨의 다음 Contour가 없으면 -1
# Previous : 동일레벨의 이전 Contour 인덱스, 동일레벨의 이전 Contour가 없으면 -1
# First Child : 최초의 자식 Contour 인덱스, 자식 Contour가 없으면 -1
# Parent : 부모 Contour 인덱스, 부모 Contour가 없으면 -1
# cv2.RETR_LIST, cv2.RETR_TREE, cv2.RETR_EXTERNAL, cv2.RETR_CCOMP
# ================================================================