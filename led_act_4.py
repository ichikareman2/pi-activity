import RPi.GPIO as GPIO
import time

LED_PIN_LIST = [17, 27, 22]
BTN_PIN = 26

GPIO.setmode(GPIO.BCM)
for led_pin in LED_PIN_LIST:
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.output(led_pin, GPIO.LOW)
GPIO.setup(BTN_PIN, GPIO.IN)

btn_status = GPIO.LOW
active_led_index = None

def next_led_pin_index(led_pin_list, last_led_pin_index):
    if last_led_pin_index == None:
        return 0
    else:
        return (last_led_pin_index + 1) % len(led_pin_list)

while True:
    new_btn_status = GPIO.input(BTN_PIN)
    if new_btn_status != btn_status:
        btn_status = new_btn_status
        if btn_status == GPIO.HIGH:
            if active_led_index != None:
                GPIO.output(LED_PIN_LIST[active_led_index], GPIO.LOW)
            active_led_index = next_led_pin_index(LED_PIN_LIST, active_led_index)
            if active_led_index != None:
                GPIO.output(LED_PIN_LIST[active_led_index], GPIO.HIGH)
    time.sleep(0.05)
    
    
GPIO.cleanup()
