import RPi.GPIO as GPIO
import time

BTN_PIN = 26
LED_PIN = 17

GPIO.setmode(GPIO.BCM)

GPIO.setup(BTN_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    if GPIO.input(BTN_PIN) == GPIO.HIGH:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.01)


GPIO.cleanup()