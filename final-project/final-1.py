import RPi.GPIO as GPIO
import time
from camera import Camera

CHECK_LOOP_SECONDS = 0.1
CHECK_THRESHOLD_SECOND = 3
PIR_PIN = 4
camera = Camera()
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

detect_image_captured = False
consecutive_high_count = 0

def on_pir_detect():
    camera.capture()
    detect_image_captured = True
    print('detected movement')

try:
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
    print("GPIO cleaned up")