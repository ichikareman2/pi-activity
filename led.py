import RPi.GPIO as GPIO
import time

LED_PIN = 17
# set gpio mode so that pin 17 is really pin 17
GPIO.setmode(GPIO.BCM)
# setup pin 17 for output
GPIO.setup(LED_PIN, GPIO.OUT)
# output to pin 17 at high/on
GPIO.output(LED_PIN, GPIO.HIGH)
# sleep for 1 second
time.sleep(1)
# output to pin 17 at low/off
GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()