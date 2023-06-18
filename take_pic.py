import cv2
import time

def snap():
    # Open the default camera
    camera = cv2.VideoCapture(1)

    # Capture a frame
    ret, frame = camera.read()

    if ret:
        cv2.imwrite("captured_image.jpg", frame)
    camera.release()

