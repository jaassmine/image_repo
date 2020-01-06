import cv2
import numpy as np

cap = cv2.VideoCapture(0) # '0'  if there is single camera connected
                          #otherwise index of device
fourcc= cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video_file.avi' , fourcc, 20.0,(640,480))
while True:
    ret, frame= cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)
    cv2.imshow('gray', gray)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):  #'q' for quit
        break
cap.release()
out.release()
cv2.destroyAllWindows()
