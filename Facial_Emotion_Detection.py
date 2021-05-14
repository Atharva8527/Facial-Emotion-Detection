

import cv2
from deepface import DeepFace

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(1)
#check if video cam is open
if not cap.isOpened():
    cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise IDError('Cannot open webcam')

while True:
    ret, frame = cap.read() ##read one face as an image
    result = DeepFace.analyze(frame, actions = ['emotion'])
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    faces = faceCascade.detectMultiScale(gray,1.1,4)

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
    font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.putText(frame,
                result['dominant_emotion'],
                (100, 100),
                font, 2,
                (0, 0, 255),
                2,
                cv2.LINE_4)
    cv2.imshow('Original video', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    ##cv2.close()

    
cap.release()
cv2.destroyAllWindows()
print(result['dominant_emotion'])
