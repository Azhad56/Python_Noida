import cv2
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier
cap = cv2.VideoCapture('obama.mp4')
classifier = cv2.CascadeClassifier('/home/azhad56/Desktop/Python_training/lecture31/haarcascade_frontalface_default.xml')
data = np.load("faces.npy")
X = data[:,1:].astype(np.uint8)
y = data[:,0]
model = KNeighborsClassifier()
model.fit(X,y)
while True:
    retval,image = cap.read()
    if retval:
        faces = classifier.detectMultiScale(image)
        sorted_faces = sorted(faces,key = lambda face:face[2]*face[3],reverse=True)
        if len(sorted_faces) >=1:
            x,y,w,h = faces[0]
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,18),10)
            face1 = image[y:y+h,x:x+w]
            t_face1 = cv2.resize(face1,(100,100))
            gray = cv2.cvtColor(t_face1,cv2.COLOR_BGR2GRAY)
            text = str(model.predict([gray.flatten()])[0])
            cv2.putText(image,text,(x,y),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),3)
            cv2.imshow("Swapped",image)
    key = cv2.waitKey(4)
    if key==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
