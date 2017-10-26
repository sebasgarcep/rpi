import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
try:
    while True:
        input_state = GPIO.input(18)
        if input_state == False:
            print('Button pressed')
            time.sleep(0.2)
finally:
    GPIO.cleanup()
