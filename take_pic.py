from pycamera import camera

def snap():
    cam = camera.Camera(0)
    picture = cam.snap() 
    picture.save("captured_image.jpg")