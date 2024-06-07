import cv2
import  numpy as np

img=cv2.imread("Images/frt.jpg")
new_img=img[0:200,0:300] #using slicing concept of list for cropping image
#first value is for height axis
#second value is for wisth axis

cv2.imshow("Crop_image",new_img)
cv2.waitKey(0)