from picamera2 import Picamera2
from libcamera import Transform
import time
import os

class Camera():
    FILE_FORMAT = "jpeg"
    path = "/home/pi/Camera"
    size = (1280, 720)
    transform = Transform(vflip=True)
    picam = None
    file_name = "image_log"
    last_file_name_number = None

    def __init__(self):
        # self.path = path
        # self.file_name = file_name
        # # check and create file
        if not os.path.exists(self.path):
            os.mkdir(self.path)
            print("created folder: " + self.path)
        print("starting up camera")
        self.picam = Picamera2()
        config = self.picam.create_still_configuration(main={"size": (self.size)}, transform=self.transform)
        self.picam.configure(config)
        self.picam.start()
        time.sleep(2)
        print("camera started up")


    def capture():
        # new_file_name = self.getNextAvailableNumber(path=self.path,
        #                                             name=self.file_name,
        #                                             format=self.format,
        #                                             initial_number=self.last_file_name_number)
        new_file_name = self.path + "/" + time.time() + "." + self.format
        self.picam.capture_file(new_file_name)
        print("captured image into: " + new_file_name)

    def dispose():
        self.picam.stop()
        print("picamera stopped and disposed")

    # def getNextAvailableNumber(path, name, format, initial_number):
    #     current_number = initial_number
    #     if initial_number == None:
    #         current_number = 1
    #     while True:
    #         full_file_name = path + name + current_number + "." + format
    #         if os.path.exists(full_file_name):
    #             current_number += 1
    #         else:
    #             return full_file_name
