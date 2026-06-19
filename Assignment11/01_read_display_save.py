import cv2
img=cv2.imread("input.jpg")
cv2.imshow("Image",img)
cv2.imwrite("saved.jpg",img)
cv2.waitKey(0); cv2.destroyAllWindows()