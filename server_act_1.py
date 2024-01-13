from flask import Flask
from gpiozero import Button, LED
from signal import pause
app = Flask(__name__)
btn = Button(26, pull_up=False)
LED_PINS = [17, 27, 22]
LED_STATES = [0, 1]
# routes
@app.route("/")
def index():
    return "Hello"

@app.route("/push-button")
def check_button():
    if btn.is_pressed:
        return "button is pressed"
    return "button is NOT pressed";

@app.route("/led/<int:led_pin>/state/<int:led_state>")
def trigger_led(led_pin, led_state):
    if (led_pin in LED_PINS and led_state in LED_STATES):
        led = LED(led_pin)
        if led_state == 1:
            led.on()
        else:
            led.off()
        pause()
        return "led triggered"
    return "led or state not valid"
app.run(host="0.0.0.0")
