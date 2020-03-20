import cv2
import time
cap = cv2.VideoCapture("face_replacement.mp4")
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
count = 0
while True:
    ret_val,image = cap.read()
    if ret_val:
        faces = classifier.detectMultiScale(image)
        faces = sorted(faces,key=lambda face:face[2]*face[3],reverse=True)
        if len(faces) >= 2:
            x1,y1,w1,h1 = faces[0]
            x2,y2,w2,h2 = faces[1]
            face1 = image[y1:y1+h1,w1:w1+h1]
            face2 = image[y2:y2+h2,w2:w2+h2]
            t_face1 = cv2.resize(face2,(w1,h1))
            t_face2 = cv2.resize(face1,(w2,h2))
            face1[:] = t_face1
            face2[:] = t_face2
            cv2.imshow("Swapped",image)
        key = cv2.waitKey(1)
        if key == ord("q"):
            break
        if key == ord("c"):
            cv2.imwrite("pic{}.png ".format(count), image)
            count += 1
cap.release()
cv2.destroyAllWindows()
