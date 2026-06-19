import cv2, numpy as np
img=cv2.imread("input.jpg")
cv2.line(img,(20,20),(300,20),(255,0,0),3)
pts=np.array([[100,100],[200,50],[300,150]],np.int32)
cv2.polylines(img,[pts],True,(0,255,0),2)
cv2.putText(img,"OpenCV",(50,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
cv2.imshow("Output",img)
cv2.waitKey(0); cv2.destroyAllWindows()