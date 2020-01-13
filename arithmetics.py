import numpy as np
import cv2

image_1= cv2.imread("C:\\Users\\YASHU\\Desktop\\image_repo\\wings.png")
image_2 = cv2.imread("C:\\Users\\YASHU\\Desktop\\image_repo\\butterfly.png")

add_image=cv2.add(image_1 , image_2)    #adding two images
cv2.imshow('add_image',add_image)



rows,cols ,channels = image_2.shape
roi = image_1[0:rows,0:cols]
image_2grey=cv2.cvtColor(image_2,cv2.COLOR_BGR2GRAY)
ret,mask= cv2.threshold(image_2grey,220,225,cv2.THRESH_BINARY_INV)

mask_inv= cv2.bitwise_not(mask)
img1_bg = cv2.bitwise_and(roi,roi,mask= mask_inv)
img2_fg = cv2.bitwise_and(image_2, image_2, mask= mask)

dst= cv2.add(img1_bg ,img2_fg)
image_1[0:rows,0:cols] = dst
cv2.imshow('res', image_1)

cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
