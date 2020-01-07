import numpy as np
import cv2

img = cv2.imread('C:\\Users\\YASHU\\Desktop\\image_repo\\flowers.jpeg',cv2.IMREAD_COLOR)  #reading an images

font=cv2.FONT_HERSHEY_SIMPLEX  #for font
cv2.putText(img,'Hey there !!', (0,150),font,1,(0,0,0),2,cv2.LINE_AA)
#  putText is function for writing text on image

cv2.imshow('image' ,img) # display an image
cv2.waitKey(0)  
cv2.destroyAllWindows()
