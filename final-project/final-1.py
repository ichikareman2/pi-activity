import RPi.GPIO as GPIO
import time
import os
from camera import Camera

def main():
    LOG_FOLDER_PATH = "/home/pi/Camera"
    LOG_FILE_PATH = LOG_FOLDER_PATH + "/" + "capture_log"
    CHECK_LOOP_SECONDS = 0.1
    CHECK_THRESHOLD_SECOND = 3
    PIR_PIN = 4
    camera = Camera()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    detect_image_captured = False
    consecutive_high_count = 0

    def update_log(file_name):
        if not os.path.exists(LOG_FOLDER_PATH):
            os.mkdir(LOG_FOLDER_PATH)
        with open(LOG_FILE_PATH, "a") as f:
            f.write(file_name + "\n")

    def on_pir_detect():
        file_name = camera.capture()
        nonlocal detect_image_captured
        detect_image_captured = True
        update_log(file_name)

    try:
        print("system ready")
        while True:
            if GPIO.input(PIR_PIN):
                consecutive_high_count += CHECK_LOOP_SECONDS
            else:
                consecutive_high_count = 0
                detect_image_captured = False
            if consecutive_high_count >= CHECK_THRESHOLD_SECOND and not detect_image_captured:
                on_pir_detect()
            time.sleep(CHECK_LOOP_SECONDS)
    except KeyboardInterrupt:
        print("keyboard interrupt")
        pass
    finally:
        GPIO.cleanup()
        camera.dispose()
        print("GPIO cleaned up")

main()