# recognition.py
import cv2
import time
from fer import FER  # Import FER for facial emotion detection

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

def capture_emotion(cam, emotion_detector):
    # Start timer
    start_time = time.time()
    final_emotion = None

    while time.time() - start_time < 5:  # Run for 5 seconds
        ret, frame = cam.read()
        if not ret:
            break

        flipped_frame = cv2.flip(frame, 1)
        gray = cv2.cvtColor(flipped_frame, cv2.COLOR_BGR2GRAY)

        # Detect faces
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        if len(faces) > 0:
            for (x, y, w, h) in faces:
                face_img = flipped_frame[y:y + h, x:x + w]
                emotion, _ = emotion_detector.top_emotion(face_img)
                final_emotion = emotion  # Update final_emotion with each iteration

                # Draw rectangle around the face and display detected emotion
                cv2.rectangle(flipped_frame, (x, y), (x + w, y + h), (100, 84, 48), 5)
                cv2.putText(flipped_frame, f"Emotion: {emotion}", (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2, cv2.LINE_AA)

        # Display the frame
        cv2.imshow('Camera', flipped_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break  # Stop if 'q' is pressed

    # Close the camera window
    cv2.destroyAllWindows()
    return final_emotion
