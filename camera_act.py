from picamera2 import Picamera2, Preview
import time

picam = Picamera2()
config = picam.create_still_configuration()
picam.configure(config)
picam.start()
time.sleep(2)
picam.capture_file("test.jpeg")
