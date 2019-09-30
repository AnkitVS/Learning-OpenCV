import cv2
img = cv2.imread('test.jpg', 1)
cv2.imshow('image', img)
cv2.waitKey(0)
img1 = cv2.imwrite('test2.jpg', img)
img3 = cv2.imread('test2.jpg', 0)
cv2.imshow('New image', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
