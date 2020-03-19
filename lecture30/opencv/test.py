import cv2

cap = cv2.VideoCapture("jboss.png")

retval, image = cap.read()

if retval:
    cv2.imshow("My capture", image)

key = cv2.waitKey(5000)
