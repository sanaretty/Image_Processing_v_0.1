import cv2
import  numpy as np


img=cv2.imread("Images/frt.jpg")

new_img=cv2.resize(img,(350,400))

cv2.imshow("New_image",new_img)
cv2.waitKey(0)

#Creating a half image from original image
new_img2=cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))

cv2.imshow("New_image",new_img2)
print("Resolution and pixels of new image",new_img2.shape)
cv2.waitKey(0)
