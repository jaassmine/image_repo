import cv2
import numpy as np

image1 = cv2.imread("C:\\Users\\YASHU\\Desktop\\image_repo\\book.jpg")
retval, threshold = cv2.threshold(image1, 12, 255,cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
retval2, threshold2= cv2.threshold(grayscaled, 12 ,255 , cv2.THRESH_BINARY)
guas = cv2.adaptiveThreshold(grayscaled, 255 , cv2.ADAPTIVE_THRESH_GAUSSIAN_C , cv2.THRESH_BINARY , 115,1)

cv2.imshow('original', image1)
cv2.imshow('threshold' , threshold)
cv2.imshow('threshold2', threshold2)
cv2.imshow('guas' ,guas)
cv2.waitKey(0)
cv2.destroyAllWindows()


