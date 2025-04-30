import RPi.GPIO as GPIO
from time import sleep

LED = 8
switch = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(LED, GPIO.OUT)

try:
	while True:
		if GPIO.input(switch) == GPIO.HIGH:
			print("LED ON")
			GPIO.output(LED, GPIO.HIGH)
			sleep(1)
		else:
			print("LED OFF")
			GPIO.output(LED, GPIO.LOW)
			sleep(1)

finally:
	GPIO.cleanup()
