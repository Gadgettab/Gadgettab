#include <UTFT.h>
#include <URTouch.h>

UTFT myGLCD(TFT01_22SP, 8, 9, 12, 11, 10);
URTouch  myTouch( 6, 5, 4, 3, 2);

bool flag = 1;
int x = 0;
int y = 0;

void setup() {
  myTouch.InitTouch(PORTRAIT);
  myTouch.setPrecision(PREC_HI);
  myGLCD.InitLCD(0);
  // очищаем экран
  myGLCD.clrScr();

  myGLCD.setColor(0, 0, 0);
  // вывод закрашенного прямоугольника
  myGLCD.fillRect(1, 1, 240, 320);
  myGLCD.setColor(0, 0, 255);

  myGLCD.fillRect(20, 20, 100, 100);
  myGLCD.fillRect(140, 20, 220, 100);

  myGLCD.fillRect(20, 120, 100, 200);
  myGLCD.fillRect(140, 120, 220, 200);

  myGLCD.fillRect(20, 220, 100, 300);
  myGLCD.fillRect(140, 220, 220, 300);
  Serial.begin(9600);
}

void loop() {
  bool i = myTouch.dataAvailable();
  if (i) {
    myTouch.read();                 // Запускаем процесс определения координат точки касания.
    //Serial.print("X=");
    x = myTouch.getX();
    //Serial.print(x);   // Получаем и выводим в монитор последовательного порта координату касания по оси X
    //Serial.print(", Y=");
    y = myTouch.getY();
    //Serial.print(y);   // Получаем и выводим в монитор последовательного порта координату касания по оси Y
    //Serial.println(".");

    if (flag) {
      flag = 0;
      if (x > 20 & x<100 & y>20 & y < 100) {
        Serial.println("1-st button presed");
        delay(100);
      }
      else if (x > 140 & x<220 & y>20 & y < 100) {
        Serial.println("2-nd button presed");
        delay(100);
      }
      else if (x > 20 & x<100 & y>120 & y < 200) {
        Serial.println("3-d button presed");
        delay(100);
      }
      else if (x > 140 & x<220 & y>120 & y < 200) {
        Serial.println("4-th button presed");
        delay(100);
      }
      else if (x > 20 & x<100 & y>220 & y < 300) {
        Serial.println("5-th button presed");
        delay(100);
      }
      else if (x > 140 & x<220 & y>220 & y < 300) {
        Serial.println("6-th button presed");
        delay(100);
      }
    }
  }
  else {
    flag = 1;
  }
}
