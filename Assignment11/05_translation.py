import cv2, numpy as np
img=cv2.imread("input.jpg")
r,c=img.shape[:2]
M=np.float32([[1,0,100],[0,1,50]])
out=cv2.warpAffine(img,M,(c,r))
cv2.imshow("Translated",out)
cv2.waitKey(0); cv2.destroyAllWindows()