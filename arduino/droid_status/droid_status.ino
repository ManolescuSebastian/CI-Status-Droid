/**
* Android status signal
* Description: This application should control two servo motors
*/

#include <Servo.h>

Servo leftHandServo;
Servo rightHandServo;

int SERVO_PIN_LEFT = 10;
int SERVO_PIN_RIGHT = 11;

void setup() {
  Serial.begin(9600);
  Serial.print("Setup started");

  leftHandServo.attach(SERVO_PIN_LEFT);
  leftHandServo.write(110);
  rightHandServo.attach(SERVO_PIN_RIGHT);
  rightHandServo.write(20);

  delay(1000);

  leftHandServo.detach();
  rightHandServo.detach();

  Serial.print("Setup ended");
}

void loop() {

  while (Serial.available() > 0)
  {
    char recieved = Serial.read();

    if (recieved == '1') {
      leftSideActiveOnly();
    }

    if (recieved == '2') {
      rightSideActiveOnly();
    }

  }
}

/**
   When left side is active, right side is inactive
*/
void leftSideActiveOnly() {
  rightHandServo.attach(SERVO_PIN_RIGHT);
  rightHandServo.write(20);
  delay(1000);
  rightHandServo.detach();

  leftHandServo.attach(SERVO_PIN_LEFT);
  delay(200);

  for (int pos = 120; pos >= 20; pos --) {
    leftHandServo.write(pos);
    delay(10);
  }
  
  delay(200);
  leftHandServo.detach();
}

/**
   When right side is active, leftht side is inactive
*/
void rightSideActiveOnly() {
  leftHandServo.attach(SERVO_PIN_LEFT);
  leftHandServo.write(110);
  delay(1000);
  leftHandServo.detach();

  rightHandServo.attach(SERVO_PIN_RIGHT);
  delay(200);

  for (int pos = 20; pos <= 110; pos ++) {
    rightHandServo.write(pos);
    delay(20);
  }
  delay(200);
  rightHandServo.detach();
}


void moveLeftHand() {

  for (int pos = 120; pos >= 20; pos --) {
    leftHandServo.write(pos);
    delay(10);
  }

  leftHandServo.detach();
  delay(3000);
  leftHandServo.attach(SERVO_PIN_LEFT);
  delay(200);

  for (int pos = 20; pos <= 120; pos ++) {
    leftHandServo.write(pos);
    delay(20);
  }

  leftHandServo.detach();
  delay(3000);
  leftHandServo.attach(SERVO_PIN_LEFT);
  delay(200);
}

void moveRightHand() {
  for (int pos = 20; pos <= 110; pos ++) {
    rightHandServo.write(pos);
    delay(20);
  }

  rightHandServo.detach();
  delay(3000);
  rightHandServo.attach(SERVO_PIN_RIGHT);
  delay(200);

  for (int pos = 110; pos >= 20; pos --) {
    rightHandServo.write(pos);
    delay(10);
  }

  rightHandServo.detach();
  delay(3000);
  rightHandServo.attach(SERVO_PIN_RIGHT);
  delay(200);
}
