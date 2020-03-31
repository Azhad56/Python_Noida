import cv2
import numpy as np
import time
import time
import os
cap = cv2.VideoCapture('face.mp4')
classifier = cv2.CascadeClassifier('/home/azhad56/Desktop/Python_training/lecture31/haarcascade_frontalface_default.xml')
X = []
name = input("Enter Your name : ")
sample = int(input("enter number of sample : "))
while True:
    retval,image = cap.read()
    if retval:
        faces = classifier.detectMultiScale(image)
        sorted_faces = sorted(faces,key = lambda face:face[2]*face[3],reverse=True)
        if len(sorted_faces) >=1:
            x,y,w,h = faces[0]
            face1 = image[y:y+h,x:x+w]
            t_face1 = cv2.resize(face1,(100,100))
            gray = cv2.cvtColor(t_face1,cv2.COLOR_BGR2GRAY)
            cv2.imshow("Swapped",image)
    key = cv2.waitKey(4)
    if key==ord('q'):
        break
    if key==ord('c'):
        X.append(gray.flatten())
        sample -= 1
        print("Faces Remaining",sample)
        if sample==0:
            break
cap.release()
cv2.destroyAllWindows()
X_mod = np.array(X)
y_mod = np.full((len(X),1),name)
data = np.hstack([y_mod,X_mod])
if os.path.exists("faces.npy"):
    old = np.load("faces.npy")
    data = np.vstack([old,data])
np.save("faces.npy",data)
