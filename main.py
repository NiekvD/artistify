import cv2

img = cv2.imread('testimg.jpg')  
rawMask = cv2.imread('mask.jpg')

rawMask = cv2.resize(rawMask, (img.shape[1], img.shape[0]))
grayImage = cv2.cvtColor(rawMask, cv2.COLOR_BGR2GRAY)  
(thresh, mask) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
mask = cv2.bitwise_not(mask)
res = cv2.bitwise_and(img,img,mask = mask)

cv2.imshow('mask', mask)
cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()