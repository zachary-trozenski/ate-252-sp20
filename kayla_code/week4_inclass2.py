import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)


counter = 0
try:
    print('PIR Module test, CTRL + C to exit')
    time.sleep(2)
    print('Ready')

    while True:

        if GPIO.input(PIR_PIN):
            counter += 1
            print('Motion detected',counter)
        time.sleep(1)

except KeyboardInterrupt:
    print('Quit')
    GPIO.cleanup()

        
