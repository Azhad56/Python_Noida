import cv2
import time
cap = cv2.VideoCapture('abc.mp4')


while True:

    retval, image = cap.read()

    if retval:

        x, y, w, h = 100, 200, 300, 400

        cut = image[y:y+h, x:x+w]

        cut[:, :, :2] = 0

        cv2.imshow("whole", image)

    key = cv2.waitKey(10)

    if key == ord("q"):
        break
    if key == ord("c"):
        cv2.imwrite("classroom.png", image)


cap.release()
cv2.destroyAllWindows()