import cv2
import  numpy as np

#1.Reading a image
img=cv2.imread("Images/frt.jpg")
print(type(img)) #stored in numpy array
print("Resolution and Channel for color image",img.shape) #gives resolution and channel for the image



# 2.printing image
cv2.imshow("Fruits",img)
cv2.waitKey(0) #induced delay to 0


#3.Converting RGB image into GreyScale
img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Greyscale image",img_grey)
cv2.waitKey(0)
print("Resolution and channels for greyscale image",img_grey.shape)