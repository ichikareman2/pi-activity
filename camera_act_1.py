from picamera2 import Picamera2, Preview
from libcamera import Transform
import time
import os

folder = "/home/pi/Camera"
if not os.path.exists(folder):
    os.mkdir(folder)
    print("created folder: " + folder)

try:
    picam = Picamera2()
    config = picam.create_still_configuration(main = {"size": (1280, 720)}, transform = Transform(vflip=True))
    picam.configure(config)
    picam.start()
    last_file_name_number = 0
    file_name = "test"
    file_format = "jpeg"
    while True:
        time.sleep(5)
        full_file_name = None
        while full_file_name == None or os.path.exists(full_file_name):
            last_file_name_number += 1
            full_file_name = folder + "/" + file_name + str(last_file_name_number) + "." + file_format
        picam.capture_file(full_file_name)
        print("saved image to " + full_file_name)

except KeyboardInterrupt:
    pass
finally:
    picam.stop()
    print("stopped")
