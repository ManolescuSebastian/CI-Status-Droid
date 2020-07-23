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
armLFPin = 12
armRTPin = 13

GPIO.setup(armLFPin, GPIO.OUT)
GPIO.setup(armRTPin, GPIO.OUT)

pwmArmLF= GPIO.PWM(armLFPin, 50)
pwmArmRT= GPIO.PWM(armRTPin, 50)

pwmArmLF.start(0)
pwmArmRT.start(0)

sleep(0.5)

pwmArmLF.ChangeDutyCycle(7)
pwmArmRT.ChangeDutyCycle(7)
sleep(0.5)

pwmArmLF.start(0)
pwmArmRT.start(0)
sleep(0.5)

#leftArm.stop(0)
#rightArm.stop(0)

def leftArmUp():
	startVal: Float = 2
	for x in range (10):
                pwmArmLF.ChangeDutyCycle(startVal + 0.5)
                sleep(0.5)
                pwmArmLF.start(0)

def leftArmDown():
	for x in range (7, 12):
                pwmArmLF.ChangeDutyCycle(7.5)
                sleep(0.2)
                pwmArmLF.start(0)

def rightArmUp():
	startVal: Float = 2
	for x in range (10):
                pwmArmRT.ChangeDutyCycle(startVal + 0.5)
                sleep(0.5)
                pwmArmRT.start(0)

def rightArmDown():
	for x in range (7, 12):
                pwmArmRT.ChangeDutyCycle(7.5)
                sleep(0.2)
                pwmArmRT.start(0)


while True:
    inputValueLeft = GPIO.input(leftPushButton)
    inputValueRight = GPIO.input(rightPushButton)
    if (inputValueLeft == True):	
        print('Left button pressed')
        GPIO.output(led_R, GPIO.LOW)
        GPIO.output(led_L, GPIO.HIGH)
        sleep(0.2)
        pwmArmRT.ChangeDutyCycle(7.5)
        sleep(0.5)
        #leftArmUp()
        #rightArmDown()

    elif (inputValueRight == True):
        #leftArmRotateOposite()
        print('Right button pressed')
        GPIO.output(led_R, GPIO.HIGH)
        GPIO.output(led_L, GPIO.LOW)
        sleep(0.2)
        pwmArmRT.ChangeDutyCycle(3)
        sleep(0.5)
        #leftArmDown()
        #rightArmUp()




#def leftSideAction(channel):
#    leftArmRotate()	
#    print('Left button pressed')
#    GPIO.output(led_R, GPIO.LOW)
#    GPIO.output(led_L, GPIO.HIGH)
#    sleep(1)

#def rightSideAction(channel):
#   leftArmRotateOposite()
#    print('Right button pressed')
#    GPIO.output(led_R, GPIO.HIGH)
#    GPIO.output(led_L, GPIO.LOW)
#    sleep(1)

#GPIO.add_event_detect(leftPushButton,GPIO.RISING,callback=leftSideAction)
#GPIO.add_event_detect(rightPushButton,GPIO.RISING,callback=rightSideAction)

#message = input("Press enter to quit\n\n") # Run until someone presses enter
#GPIO.cleanup() # Clean up

