import cv2
img=cv2.imread("input.jpg")
r,c=img.shape[:2]
M=cv2.getRotationMatrix2D((c//2,r//2),45,1)
out=cv2.warpAffine(img,M,(c,r))
cv2.imshow("Rotated",out)
cv2.waitKey(0); cv2.destroyAllWindows()