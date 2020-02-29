import RPi.GPIO as GPIO
import time

print("distance measurement in progress")



while True:
	GPIO.setmode(GPIO.BCM)
	trigger = 23
	echo = 24


	GPIO.setup(trigger, GPIO.OUT)
	GPIO.setup(echo, GPIO.IN)
	GPIO.output(trigger, False)

	print("Waiting for sensor to reset")
	time.sleep(2)

	GPIO.output(trigger, True)
	time.sleep(0.00001)

	GPIO.output(trigger, False)

	while GPIO.input(echo) == 0:
		pulse_start = time.time()
		
	while GPIO.input(echo) == 1:
		pulse_end = time.time()
		
	pulse_duration = pulse_end - pulse_start

	distance = pulse_duration * 17150

	distance = round(distance, 2)

	print("Distance:", distance, "cm")

	GPIO.cleanup()
