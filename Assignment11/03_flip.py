import cv2
img=cv2.imread("input.jpg")
cv2.imshow("Horizontal",cv2.flip(img,1))
cv2.imshow("Vertical",cv2.flip(img,0))
cv2.imshow("Both",cv2.flip(img,-1))
cv2.waitKey(0); cv2.destroyAllWindows()