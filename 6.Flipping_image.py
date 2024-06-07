import  cv2
import  numpy as np


img=cv2.imread("Images/frt.jpg")

new_img=cv2.flip(img,1)
#Flipping is used for data augumentation

#0 flips image vertically
#1 flips image horizontally
#-1 flips combined that is in vertical as well as horizontal

cv2.imshow("Flipped image",new_img)

cv2.waitKey(0)