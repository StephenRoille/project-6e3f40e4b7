"""Drawing Functions in OpenCV.

tutorial: https://docs.opencv.org/master/dc/da5/tutorial_py_drawing_functions.html
"""
import numpy as np
import cv2 as cv


img = np.zeros((512,512,3), np.uint8)
cv.line(img, (0,0), (511,511), (255,0,0), 5)
cv.circle(img,(447,63), 63, (0,0,255), -1)
pts = np.array([[10,5], [20,30], [70,20], [50,200]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)
while True:
    cv.imshow("name", img)
    if cv.waitKey(0) == ord("q"):
        break

