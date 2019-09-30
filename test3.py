import numpy as np
import cv2
myimg = np.zeros((512,512,3),np.uint8)


myimg=cv2.line(myimg,(0,512),(512,0),(255,0,255),2)
myimg=cv2.rectangle(myimg,(25,52),(200,200),(255,0,255),3)
myimg=cv2.circle(myimg,(350,350),75,(255,0,255),3)
myimg=cv2.putText(myimg,"Ankit Ved")
cv2.imshow('myimg',myimg)
cv2.waitKey(0)
cv2.destroyAllWindows()