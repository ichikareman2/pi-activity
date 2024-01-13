import RPi.GPIO as GPIO
import time

LED_PIN_1 = 17
LED_PIN_2 = 27
LED_PIN_3 = 22

BTN_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_1, GPIO.OUT)
GPIO.setup(LED_PIN_2, GPIO.OUT)
GPIO.setup(LED_PIN_3, GPIO.OUT)
GPIO.setup(BTN_PIN, GPIO.IN)

active_led_pin = None
btn_status = GPIO.LOW

GPIO.output(LED_PIN_1, GPIO.LOW)
GPIO.output(LED_PIN_2, GPIO.LOW)
GPIO.output(LED_PIN_3, GPIO.LOW)

while True:
    new_btn_status = GPIO.input(BTN_PIN)
    if new_btn_status != btn_status:
        btn_status = new_btn_status
        if btn_status == GPIO.HIGH:
            if active_led_pin != None:
                GPIO.output(active_led_pin, GPIO.LOW)
            if active_led_pin == None or active_led_pin == LED_PIN_3:
                active_led_pin = LED_PIN_1
            elif active_led_pin == LED_PIN_1:
                active_led_pin = LED_PIN_2
            elif active_led_pin == LED_PIN_2:
                active_led_pin = LED_PIN_3
            if active_led_pin != None:
                GPIO.output(active_led_pin, GPIO.HIGH)
    time.sleep(0.05)
    
    
GPIO.cleanup()