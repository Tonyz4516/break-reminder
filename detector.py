import cv2
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect_face():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    # cv2.imwrite("Desktop/x.jpg", frame)
    cap.release()
    
    # convert the image to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # if face detected, the faces array has length > 0
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    return len(faces) > 0