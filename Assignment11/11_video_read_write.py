import cv2
cap=cv2.VideoCapture("input_video.mp4")
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter("output.avi",fourcc,20,(640,480))
while True:
    ret,frame=cap.read()
    if not ret: break
    frame=cv2.resize(frame,(640,480))
    out.write(frame)
    cv2.imshow("Video",frame)
    if cv2.waitKey(1)==ord('q'): break
cap.release(); out.release(); cv2.destroyAllWindows()