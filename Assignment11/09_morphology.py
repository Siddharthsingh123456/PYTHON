import cv2, numpy as np
img=cv2.imread("input.jpg",0)
k=np.ones((5,5),np.uint8)
cv2.imshow("Tophat",cv2.morphologyEx(img,cv2.MORPH_TOPHAT,k))
cv2.imshow("Blackhat",cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,k))
cv2.waitKey(0); cv2.destroyAllWindows()