import cv2

# Open the default camera
camera = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not camera.isOpened():
    print("Failed to open the camera")
    exit()

# Capture a frame
ret, frame = camera.read()

if ret:
    # Save the captured frame as an image file
    cv2.imwrite("captured_image.jpg", frame)
    print("Image captured successfully")

# Release the camera
camera.release()