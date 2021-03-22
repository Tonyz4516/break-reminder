import cv2
from imutils.video import VideoStream

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
vs = VideoStream(src=0).start()

def detect_face():
    frame = vs.read()
    # cv2.imwrite("Desktop/x.jpg", frame)
    
    # convert the image to gray scale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # if face detected, the faces array has length > 0
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    return len(faces) > 0
