/**
  Android status signal
  Description: This application should control two servo motors
*/

#include <Servo.h>

Servo leftHandServo;
Servo rightHandServo;

const int SERVO_PIN_LEFT = 10;
const int SERVO_PIN_RIGHT = 11;

const int LEFT_PUSH = 2;
const int RIGHT_PUSH = 3;

const int led_o = 7;
const int led_t = 8;

int leftButtonState = 0;
int rightButtonState = 0;

boolean disableSteppers = true;
boolean disablePushButtons = false;

void setup() {
  Serial.begin(9600);
  Serial.print("Setup started");

  pinMode(LEFT_PUSH, INPUT);
  pinMode(RIGHT_PUSH, INPUT);

  pinMode(led_o, OUTPUT);
  pinMode(led_t, OUTPUT);

  if (disableSteppers) {
    return;
  }

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

  pushButtonDetect();

  while (Serial.available() > 0)
  {
    char recieved = Serial.read();

    if (recieved == '0') {
      leftSideActiveOnly();
      disablePushButtons = true;
      leftButtonState = 1;
      rightButtonState = 1;
    }

    if (recieved == '1') {
      rightSideActiveOnly();
      disablePushButtons = false;
      leftButtonState = 0;
      rightButtonState = 0;
    }

  }
}

void pushButtonDetect() {
  if (!disablePushButtons) {
    leftButtonState = digitalRead(LEFT_PUSH);
    rightButtonState = digitalRead(RIGHT_PUSH);
  }

  if (leftButtonState == HIGH) {
    digitalWrite(led_o, HIGH);
  } else {
    digitalWrite(led_o, LOW);
  }

  if (rightButtonState == HIGH) {
    digitalWrite(led_t, HIGH);
  } else {
    digitalWrite(led_t, LOW);
  }

}

/**
   When left side is active, right side is inactive
*/
void leftSideActiveOnly() {
  if (disableSteppers) {
    return;
  }

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
  if (disableSteppers) {
    return;
  }
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
