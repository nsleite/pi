#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
PIN = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.OUT, initial=GPIO.LOW)

while True:

	try:
		print("LED ON...")
		GPIO.output(PIN, GPIO.HIGH)
		time.sleep(0.5)
		
		print("LED OFF...")
		GPIO.output(PIN, GPIO.LOW)
		time.sleep(0.5)

	except KeyboardInterrupt:
		GPIO.output(PIN, GPIO.LOW)
		GPIO.cleanup()
