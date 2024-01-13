import RPi.GPIO as GPIO
import time

state = int(input("0: off; 1: on"))
if state == 0 or state == 1:
    LED_PIN = 17
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED_PIN, GPIO.OUT)
    if state == 0:
        GPIO.output(LED_PIN, GPIO.LOW)
    else:
        GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(2)
    GPIO.cleanup()
exit
