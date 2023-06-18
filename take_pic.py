import cv2

def snap():
    camera = cv2.VideoCapture(0)

    ret, frame = camera.read()

    if ret:
        cv2.imwrite("captured_image.jpg", frame)
    camera.release()