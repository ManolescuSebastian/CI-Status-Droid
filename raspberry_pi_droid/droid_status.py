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
# Push Button setup
#====================
leftPushButton = 17
rightPushButton = 27

GPIO.setup(leftPushButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(rightPushButton, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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

sleep(0.5)

leftArm.ChangeDutyCycle(7)
rightArm.ChangeDutyCycle(7)
sleep(0.5)

leftArm.start(0)
rightArm.start(0)
sleep(0.5)

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
    inputValueLeft = GPIO.input(leftPushButton)
    inputValueRight = GPIO.input(rightPushButton)
    if (inputValueLeft == True):
        #leftArmRotate()	
        print('Left button pressed')
        GPIO.output(led_R, GPIO.LOW)
        GPIO.output(led_L, GPIO.HIGH)
        print('Left button pressed')
        sleep(0.3)
    
    elif (inputValueRight == True):
        #leftArmRotateOposite()
        print('Right button pressed')
        GPIO.output(led_R, GPIO.HIGH)
        GPIO.output(led_L, GPIO.LOW)
        print('Right button pressed')
        sleep(0.3)



def leftSideAction(channel):
    #leftArmRotate()	
    print('Left button pressed')
    GPIO.output(led_R, GPIO.LOW)
    GPIO.output(led_L, GPIO.HIGH)
    sleep(1)

def rightSideAction(channel):
    #leftArmRotateOposite()
    print('Right button pressed')
    GPIO.output(led_R, GPIO.HIGH)
    GPIO.output(led_L, GPIO.LOW)
    sleep(1)

#GPIO.add_event_detect(leftPushButton,GPIO.RISING,callback=leftSideAction)
#GPIO.add_event_detect(rightPushButton,GPIO.RISING,callback=rightSideAction)

#message = input("Press enter to quit\n\n") # Run until someone presses enter
#GPIO.cleanup() # Clean up

