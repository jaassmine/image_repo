import numpy as np
import cv2

img = cv2.imread('C:\\Users\\YASHU\\Desktop\\image_repo\\flowers.jpeg',cv2.IMREAD_COLOR)  #reading an images

cv2.line(img,(10,10),(100,100),(0,0,0),10) # for drawing line

cv2.rectangle(img,(15,25),(200,150),(0,0,0),5)  #for drawing rectangle

cv2.circle(img,(100,63),55,(0,0,255),1) #for drawing circle

#for drawing polygons points needs to be define
pts=np.array([[10,5],[20,30],[70,20],[50,10]])
pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),3)  #for drawing polygons

cv2.imshow('image' ,img) # display an image
cv2.waitKey(0)  
cv2.destroyAllWindows()
