import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

from time import sleep


led_R = 2
led_L = 3

GPIO.setup(led_R, GPIO.OUT)
GPIO.setup(led_L, GPIO.OUT)


while True:

	GPIO.output(led_R, GPIO.HIGH)
	GPIO.output(led_L, GPIO.HIGH)
	sleep(3)

	GPIO.output(led_R, GPIO.LOW)
	GPIO.output(led_L, GPIO.LOW)
	sleep(1)

