## Sensor script

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

PIR_PIN = 7
GPIO.setup(PIR_PIN, GPIO.IN)

counter = 0

try:
    print("PIR MODULE TEST, CTRL + C TO CANCEL")
    time.sleep(2)
    print("READY")


    while True:
        if GPIO.input(PIR_PIN):
            print("MOTION DETECTED", counter)
            counter += 1
        time.sleep(1)
 
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
