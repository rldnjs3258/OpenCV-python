import cv2

img_color = cv2.imread('Example.jpg', cv2.IMREAD_COLOR)

cv2.namedWindow('Show Image')
cv2.imshow('Show Image', img_color)
cv2.waitKey(0)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imshow("Show Image", img_gray)
cv2.waitKey(0)

cv2.imwrite('savedimage.jpg', img_gray) #흑백 이미지를 저장한다.

cv2.destroyAllWindows()