##operation on image

import numpy as np
import cv2

img = cv2.imread('C:\\Users\\YASHU\\Desktop\\image_repo\\flowers.jpeg',cv2.IMREAD_COLOR)  #reading an images

px=img[55,55]

img[100:150, 100:150] = [0,0,0] # convert the colour of the part specifies by the points into the specified color
cv2.imshow('image',img)


# cut and paste
img_part = img[40:100, 100:150]
img[0:60,0:50]=img_part
cv2.imshow('imge',img)


cv2.waitKey()
cv2.destroyAllWindows()
