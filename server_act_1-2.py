from flask import Flask
import RPi.GPIO as GPIO

LED_PINS = [17, 27, 22]
LED_STATES = [0, 1]
BTN_PIN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(BTN_PIN, GPIO.IN)
for pin in LED_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

app = Flask(__name__)
# btn = Button(26, pull_up=False)

# routes
@app.route("/")
def index():
    return "Hello"

@app.route("/push-button")
def check_button():
#    if btn.is_pressed:
    if GPIO.input(BTN_PIN) == GPIO.HIGH:
        return "button is pressed"
    return "button is NOT pressed";

@app.route("/led/<int:led_pin>/state/<int:led_state>")
def trigger_led(led_pin, led_state):
    if (led_pin in LED_PINS and led_state in LED_STATES):
#        led = LED(led_pin)
        if led_state == 1:
            GPIO.output(led_pin, GPIO.HIGH)
        else:
            GPIO.output(led_pin, GPIO.LOW)
        return "led triggered"
    return "led or state not valid"

try:
    app.run(host="0.0.0.0")
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
