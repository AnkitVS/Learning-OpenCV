import cv2
import numpy as np

def blankcalable(a):
    pass;

img= np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

cv2.createTrackbar("Red","image",0,255,blankcalable)
cv2.createTrackbar("Blue","image",0,255,blankcalable)
cv2.createTrackbar("Green","image",0,255,blankcalable)

r=0
b=0
g=0

img2 = cv2.imread("test.jpg")
b2,r2,g2 = cv2.split(img2)
b2_orig,g2_orig,r2_orig = cv2.split(img2)
cv2.namedWindow("Output")

while(True):
    cv2.imshow("image",img)
    cv2.imshow("Output",img2)

    img[:]=[b,g,r]
    b2=b2-b
    g2=g2-g
    r2=r2-r

    img2=cv2.merge((b2,r2,g2))

    cv2.putText(img,"Press r to reset",(10,50), cv2.QT_FONT_NORMAL,1,(200,200,200),1)
    k=cv2.waitKey(3) & 0xFF

    r=cv2.getTrackbarPos("Red","image")
    b=cv2.getTrackbarPos("Blue","image")
    g=cv2.getTrackbarPos("Green","image")

    if k==ord('r'):
        cv2.getTrackbarPos("Red", "image", 0)
        cv2.getTrackbarPos("Blue", "image", 0)
        cv2.getTrackbarPos("Green", "image", 0)
        b2=b2_orig
        g2 = g2_orig
        r2 = r2_orig

    elif k==ord('q'):
        break
    elif k==27:
        break

cv2.destroyAllWindows()
