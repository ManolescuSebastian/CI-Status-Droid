import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

from time import sleep

#====================
# LED setup
#====================

led_R = 2
led_L = 3

GPIO.setup(led_R, GPIO.OUT)
GPIO.setup(led_L, GPIO.OUT)


#====================
# Servo motors setup
#====================

leftArmPin = 23
rightArmPin = 12

GPIO.setup(leftArmPin, GPIO.OUT)
GPIO.setup(rightArmPin, GPIO.OUT)

leftArm= GPIO.PWM(leftArmPin, 50)
rightArm = GPIO.PWM(rightArmPin, 50)


leftArm.start(0)
rightArm.start(0)

sleep(1)

leftArm.ChangeDutyCycle(7)
rightArm.ChangeDutyCycle(7)
sleep(0.5)

leftArm.start(0)
rightArm.start(0)
sleep(1)

leftArm.stop(0)
rightArm.stop(0)

#def leftArmRotate():
#	startVal: Float = 2
#	for x in range (10):
#                leftArm.ChangeDutyCycle(startVal + 0.5)
#                sleep(0.5)
#                leftArm.start(0)

#def leftArmRotateOposite():
#	for x in range (7, 12):
#                leftArm.ChangeDutyCycle(7.5)
#                sleep(0.2)
#                leftArm.start(0)

while True:
#    leftArmRotate()	
    GPIO.output(led_R, GPIO.HIGH)
    GPIO.output(led_L, GPIO.HIGH)
    sleep(3)

#    leftArmRotateOposite()
    GPIO.output(led_R, GPIO.LOW)
    GPIO.output(led_L, GPIO.LOW)
    sleep(1)
