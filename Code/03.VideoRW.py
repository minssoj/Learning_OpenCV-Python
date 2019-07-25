import numpy as np
import cv2

def showVideo():
	try: # Error 발생 시 except 진행
		print("Execute Camera!")
		#cap = cv2.VideoCapture(0)
		cap = cv2.VideoCapture('../Images/02.cloudy_water.mp4')
	except:
		print("Failed Executing Camera")
		return

	#cap.set(3, 480)	# width
	#cap.set(4, 320)	# height

	fps = 20.0
	width = int(cap.get(3))
	height = int(cap.get(4))
	fcc = cv2.VideoWriter_fourcc('D','I','V','X')	# DIVX Codec
	out = cv2.VideoWriter('../Images/02.cloudy_water.avi',fcc, fps, (width, height))
	print("Start recording!")

	while True:
		ret, frame = cap.read()

		if not ret:
			print("Error!")
			break

		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		cv2.imshow('video', gray)
		out.write(frame)
		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			break
	cap.release()
	out.release()
	cv2.destroyAllWindows()

showVideo()

