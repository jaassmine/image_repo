import numpy as np
import cv2

image_1= cv2.imread("C:\\Users\\YASHU\\Desktop\\image_repo\\flowers.jpeg",0)
image_2 = cv2.imread("C:\\Users\\YASHU\\Desktop\\image_repo\\images.jpg",0)

add_image=cv2.add(image_1 , image_2)    #adding two images
dim=image_2.shape[2]
print(dim)
#rows,cols,channels  = image_2.shape
#roi - image_1[0:rows,0:cols]
#image_2grey=cv2.cvtColor(image_2,cv2.COLOR_BGR2GRAY)
#ret,mask= cv2.threshold(image_2grey,220,225,cv2.THRESH_BINARY_INV)

#cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
