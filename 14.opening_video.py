import  cv2
import numpy as np
import  time

img=cv2.VideoCapture("output.avi")
while True:

    ret,frame=img.read()

    cv2.imshow("Webcam",frame)
    time.sleep(1/20) #Delaying the video to match original speed of the video
    if cv2.waitKey(1) &  0xFF==ord("x"):
        break


cv2.destroyAllWindows()