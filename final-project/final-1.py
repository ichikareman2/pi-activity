import RPi.GPIO as GPIO
import time
import os
from camera import Camera
from email_sender import EmailSender

def main():
    RECEIVING_EMAIL = "kevinwillardquing@proton.me"
    CAMERA_FOLDER_PATH = "/home/pi/Camera"
    LOG_FOLDER_PATH = "/home/pi/Camera"
    LOG_FILE_PATH = LOG_FOLDER_PATH + "/" + "capture_log.txt"
    CHECK_LOOP_SECONDS = 0.1
    CHECK_THRESHOLD_SECONDS = 3.0
    CAPTURE_WAIT_SECONDS = 60.0
    PIR_PIN = 4
    camera = Camera(CAMERA_FOLDER_PATH)
    email_sender = EmailSender()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    last_image_capture_time = None
    move_start_time = None

    def update_log(file_name):
        if not os.path.exists(LOG_FOLDER_PATH):
            os.mkdir(LOG_FOLDER_PATH)
        with open(LOG_FILE_PATH, "a") as f:
            f.write(file_name + "\n")

    def on_pir_detect():
        nonlocal last_image_capture_time
        current_time = time.time()
        if last_image_capture_time == None or current_time - last_image_capture_time > CAPTURE_WAIT_SECONDS:
            last_image_capture_time = current_time
            file_name = camera.capture()
            update_log(file_name)
            email_sender.send_email(RECEIVING_EMAIL,
                                    "Movement detected",
                                    "Movement log file: " + file_name,
                                    attachments=file_name)

    try:
        print("system ready")
        while True:
            movement_detected = GPIO.input(PIR_PIN) == GPIO.HIGH
            if movement_detected and move_start_time == None:
                move_start_time = time.time()
            elif not movement_detected and move_start_time != None:
                move_start_time = None
            if move_start_time != None and (time.time() - move_start_time) >= CHECK_THRESHOLD_SECONDS:
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