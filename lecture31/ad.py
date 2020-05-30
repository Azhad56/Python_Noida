import cv2
import time

import numpy as np

cap_screen = cv2.VideoCapture("abc.mp4")
cap_cam = cv2.VideoCapture("Ahmad2.mp4")

theta = np.linspace(0, 100*np.pi, 10000)
rad = 100
center_x, center_y = 100, 100

X = (rad * np.cos(theta) + center_x).astype(int)
Y = (rad * np.sin(theta) + center_y).astype(int)

for x, y in zip(X, Y):

    retval_screen, image_screen = cap_screen.read()
    retval_cam, image_cam = cap_cam.read()

    if retval_screen and retval_cam:

        w, h = 100, 50
        print(x, y, w, h)

        corner = cv2.resize(image_cam, (w, h))
        print(corner.shape)

        cut = image_screen[y:y+h, x:x+w]
        cut[:] = corner

        cv2.imshow("whole", image_screen)

    key = cv2.waitKey(10)

    if key == ord("q"):
        break


cap_cam.release()
cap_screen.release()
cv2.destroyAllWindows()