import cv2

# Load the pre-trained Haar Cascade for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start the webcam
cap = cv2.VideoCapture(0)  # 0 = default camera

print("Press 's' to save an image with detected faces, or 'q' to quit.")

while True:
    ret, frame = cap.read()  # Read frame from webcam
    if not ret:
        print("Failed to capture video")
        break

    # Convert to grayscale (Haar cascades work better on grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show the webcam feed
    cv2.imshow('Face Detection', frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        # Save the image when 's' is pressed
        cv2.imwrite('detected_faces.png', frame)
        print("Image saved as 'detected_faces.png'")
    elif key == ord('q'):
        # Quit when 'q' is pressed
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
