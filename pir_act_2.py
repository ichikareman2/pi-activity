import RPi.GPIO as GPIO
import time

PIR_PIN = 4
LED_PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIR_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)
last_state = GPIO.LOW

try:
    while True:
        new_state = GPIO.input(PIR_PIN)
        if last_state != new_state:
            last_state = new_state
            if last_state == GPIO.HIGH:
                GPIO.output(LED_PIN, GPIO.HIGH)
            else:
                GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(0.1)
except:
    pass
finally:
    GPIO.cleanup()
