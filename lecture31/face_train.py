import cv2
import time

import numpy as np

import os

cap = cv2.VideoCapture('face.mp4')

classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

X = []

name = input("Enter your name : ")
count = int(input("Enter number of samples : "))

while True:

    retval, image = cap.read()

    if retval:

        faces = classifier.detectMultiScale(image)
        faces = sorted(faces, key=lambda face: face[2]*face[3], reverse=True)

        if len(faces) >= 1:

            x1, y1, w1, h1 = faces[0]

            face1 = image[y1:y1+h1, x1:x1+w1]

            t_face1 = cv2.resize(face1, (100, 100))

            gray = cv2.cvtColor(t_face1, cv2.COLOR_BGR2GRAY)

            cv2.imshow("swapped", gray)

    key = cv2.waitKey(10)

    if key == ord("c"):
        X.append(gray.flatten())
        print("Faces remaining", count)
        count -= 1
        if count == 0:
            break


cap.release()
cv2.destroyAllWindows()

X_mod = np.array(X).shape
y_mod = np.full((len(X), 1), name)

data = np.hstack([y_mod, X_mod])

if os.path.exists("faces.npy"):
    old = np.load("faces.npy")
    data = np.vstack([old, data])

np.save("faces.npy", data)