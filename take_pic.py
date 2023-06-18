import cv2

def snap():
    # Open the default camera
    camera = cv2.VideoCapture(0)

    # Capture a frame
    ret, frame = camera.read()

    if ret:
        # Save the captured frame as an image file
        cv2.imwrite("captured_image.jpg", frame)
    # Release the camera
    camera.release()