import sys
import cv2
import numpy as np
import subprocess
import time
from fer import FER  # Import FER for facial emotion detection

# Initialize the FER emotion detector
emotion_detector = FER()

#Camera for capturing video
cam = cv2.VideoCapture(0)

#We might be able to get rid of this..
frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (frame_width, frame_height))

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
start_time = time.time()
duration = 5

#While the duration is not up yet, capture frames and detect faces
while time.time() - start_time < duration:
    try:
        ret, frame = cam.read()
        if not ret:
            break
        
        flipped_frame = cv2.flip(frame, 1)
        elapsed_time = time.time() - start_time
            
        gray = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                face_img = flipped_frame[y:y + h, x:x + w]
                emotion, _ = emotion_detector.top_emotion(face_img)
                
                cv2.rectangle(flipped_frame, (x, y), (x + w, y + h), (100, 84, 48), 5)
                cv2.putText(flipped_frame, f"Emotion: {emotion}", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2, cv2.LINE_AA)

        out.write(flipped_frame)
        cv2.imshow('Camera', flipped_frame)
        
        # Display remaining time
        remaining_time = max(0, duration - elapsed_time)
        cv2.putText(flipped_frame, f"Time left: {remaining_time:.1f}s", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    except Exception as e:
        print(f"Error: {e}")

# After the loop ends, capture the last frame as the final emotion
if len(faces) > 0:
    x, y, w, h = faces[0]  # Assuming we're interested in the first detected face
    face_img = flipped_frame[y:y + h, x:x + w]
    cv2.imwrite("face_img_recent.png", face_img)
    final_emotion, _ = emotion_detector.top_emotion(face_img)
    print(f"Final captured emotion: {final_emotion}")


cam.release()
out.release()
cv2.destroyAllWindows()