import  cv2
import  numpy as np

def draw(event,x,y,flags,params):
    if event==1:
        cv2.circle(img,center=(x,y),color=(255,0,0),thickness=-1,radius=50)
    elif event==4:
        print("Mouse button is released")


cv2.namedWindow(winname="Window")
cv2.setMouseCallback('Window',draw)

img=cv2.imread("Images/frt.jpg")

while True:

    cv2.imshow("Window",img)
    if cv2.waitKey(1) & 0xFF==ord('x'):
        break

cv2.destroyAllWindows()