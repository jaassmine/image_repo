import cv2
import numpy as np


cap = cv2.imread("butterfly.png")
hsv= cv2.cvtColor(cap,cv2.COLOR_BGR2HSV)

lower_color= np.array([100,180,0])
upper_color=np.array([185,255,255])

mask = cv2.inRange(hsv, lower_color , upper_color)
res= cv2.bitwise_and(cap , cap,mask=mask)

cv2.imshow('cap' , cap)
cv2.imshow('mask',mask)
cv2.imshow('res',res)

cv2.waitKey(0)
cv2.destroyAllWindows()
    
