import cv2
from matplotlib import pyplot as pyplt
img = cv2.imread('test.jpg', 1)
cv2.imshow('image', img)


pyplt.imshow(img,cmap='gray',interpolation='bicubic')
pyplt.show()

wk = cv2.waitKey(0)
if wk ==27:
    print("quit without saving")
    cv2.destroyAllWindows()
elif wk == ord('s'):
    cv2.imwrite('mypython.jpg', img)
    print("image saved")
    cv2.destroyAllWindows()
else:
    print("unknown keystroke")

cv2.destroyAllWindows()
