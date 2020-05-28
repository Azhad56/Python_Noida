import cv2
import numpy as np
import os
from sklearn.neighbors import KNeighborsClassifier
cap = cv2.VideoCapture('Azhad_Ahmad.mp4')
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
        if len(sorted_faces) >=2:
            x1,y1,w1,h1 = faces[0]
            x2, y2, w2, h2 = faces[1]
            cv2.rectangle(image,(x1,y1),(x1+w1,y1+h1),(255,0,18),10)
            cv2.rectangle(image, (x2, y2), (x2 + w2, y2 + h2), (255, 0, 18), 10)
            face1 = image[y1:y1+h1,x1:x1+w1]
            face2 = image[y2:y2 + h2, x2:x2 + w2]
            t_face1 = cv2.resize(face1,(100,100))
            t_face2 = cv2.resize(face2, (100, 100))
            gray1 = cv2.cvtColor(t_face1,cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(t_face2, cv2.COLOR_BGR2GRAY)
            text1 = str(model.predict([gray1.flatten()])[0])
            text2 = str(model.predict([gray2.flatten()])[0])
            cv2.putText(image,text1,(x1,y1),cv2.FONT_HERSHEY_COMPLEX,2,(255,0,0),3)
            cv2.putText(image, text2, (x2, y2), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 0), 3)
            cv2.imshow("Swapped",image)
    key = cv2.waitKey(4)
    if key==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
