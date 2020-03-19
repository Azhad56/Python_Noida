import cv2
cap = cv2.VideoCapture("face.mp4")
while True:
    retval,image = cap.read()
    if retval:
        x,y,w,h = 400,250,250,250
        cut = image[y:y+h,x:x+w]
        cut[:,:,0] = 0
        cv2.imshow("cut image",image)
    key = cv2.waitKey(20)
    if key==ord("q"):
        break
    if key==ord("c"):
        cv2.imwrite("my_capture.png",image)
cap.release()
cv2.destroyAllWindows()