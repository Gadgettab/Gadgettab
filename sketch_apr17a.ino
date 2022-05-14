#include <Servo.h>

#define pot_1 A0
#define pot_2 A1
#define pot_3 A2
#define pot_4 A3

#define but_pin 10

Servo servo_1;
Servo servo_2;
Servo servo_3;
Servo servo_4;

int servo_1_pin = 6;
int servo_2_pin = 7;
int servo_3_pin = 8;
int servo_4_pin = 9;

int angle_1;
int angle_2;
int angle_3;
int angle_4;

int buf_angle_1;
int buf_angle_2;
int buf_angle_3;
int buf_angle_4;

void setup() {
  pinMode(pot_1, INPUT);
  pinMode(pot_2, INPUT);
  pinMode(pot_3, INPUT);
  pinMode(pot_4, INPUT);

  servo_1.attach(servo_1_pin);
  servo_2.attach(servo_2_pin);
  servo_3.attach(servo_3_pin);
  servo_4.attach(servo_4_pin);

  Serial.begin(9600);
}

void loop() {

  angle_1 = map(analogRead(pot_1), 0, 1023, 0, 180);
  angle_2 = map(analogRead(pot_2), 0, 1023, 160, 80 );
  angle_3 = map(analogRead(pot_3), 0, 1023, 34, 110);
  angle_4 = map(analogRead(pot_4), 0, 1023, 0, 180);
  
  servo_1.write(angle_1);
  servo_2.write(angle_2);
  servo_3.write(angle_3);
  servo_4.write(angle_4);

  Serial.print(angle_1);
  Serial.print("/t");
  Serial.print(angle_2);
  Serial.print("/t");
  Serial.print(angle_3);
  Serial.print("/t");
  Serial.print(angle_4);
  erial.print("/t");
  Serial.print(analogRead(A4));
  Serial.println();
  delay(15);

  if (analogRead(A4) <= 300){
    digitalWrite(11, HIGH);
    digitalWrite(12, LOW);
   
  }
  else if(analogRead(A4) >= 900){
    digitalWrite(11, LOW);
    digitalWrite(12, HIGH);
  }
  else{
    digitalWrite(11, LOW);
    digitalWrite(12, LOW);
}
}
