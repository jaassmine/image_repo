import numpy as np
import cv2

image_1= cv2.imread("C:\\Users\\YASHU\\Desktop\\image_repo\\flowers.jpeg")
image_2 = cv2.imread("C:\\Users\\YASHU\\Desktop\\image_repo\\bee.jpeg")

add_image=image_1+image_2

cv2.imshow()
cv2.waitKey()
cv2.destroyAllWindows()
