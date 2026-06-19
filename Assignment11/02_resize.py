import cv2
img=cv2.imread("input.jpg")
res=cv2.resize(img,(500,500))
cv2.imshow("Resized",res)
cv2.waitKey(0); cv2.destroyAllWindows()