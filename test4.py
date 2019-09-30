import cv2
import numpy as np
def draw_rect(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.rectangle(img,(x,y),(x+100,y+100),(200,200,0),2)

img= np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_rect)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(0) & 0xFF == 27:
        break
cv2.destroyAllWindows()