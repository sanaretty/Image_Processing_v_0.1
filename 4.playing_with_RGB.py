import cv2
import  numpy as np

#1.Reading a image
img=cv2.imread("Images/frt.jpg")
# print(type(img)) #stored in numpy array
# print("Resolution and Channel for color image",img.shape)

# img[:,:,0]=0 Blue channel is 0
# img[:,:,1]=0 Green channel is 0
# img[:,:,2]=0 Red channel is 0

imgblue=img[:,:,0]
imggreen=img[:,:,1]
imgred=img[:,:,2]

images=np.hstack((imgblue,imggreen,imgred))
#hstack is  used for analyzing images side by side

cv2.imshow("image",images)
cv2.waitKey(0)