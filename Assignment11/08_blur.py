import cv2
img=cv2.imread("input.jpg")
cv2.imshow("Gaussian",cv2.GaussianBlur(img,(5,5),0))
cv2.imshow("Median",cv2.medianBlur(img,5))
cv2.waitKey(0); cv2.destroyAllWindows()