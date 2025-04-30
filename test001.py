import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED = 11
LED2 = 13

GPIO.setup(LED, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(LED, GPIO.HIGH)

GPIO.setup(LED2, GPIO.OUT, initial=GPIO.LOW)
GPIO.output(LED2, GPIO.HIGH)

try:
	while 1:
		switch = int(input())
		if switch == 1:
			GPIO.output(LED, GPIO.HIGH)
			GPIO.output(LED2, GPIO.HIGH)
		elif switch == 0:
			GPIO.output(LED, GPIO.LOW)
			GPIO.output(LED2, GPIO.LOW)
except KeyboardInterrupt:
	pass

finally:
	GPIO.cleanup()
