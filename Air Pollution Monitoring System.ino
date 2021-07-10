#include <LiquidCrystal.h>
const int rs=12, en=11, d4=5, d5=4, d6=3, d7=2;
LiquidCrystal lcd(rs,en,d4,d5,d6,d7);

int buz = 8;
int led = 9;

const int aqsensor = A0;
int threshold = 250;
void setup() 
{

  pinMode (buz,OUTPUT);
  pinMode (led,OUTPUT);
  pinMode (aqsensor,INPUT);

  Serial.begin (9600);   
      
}

void loop() {

  int ppm = analogRead(aqsensor);

  Serial.print("Air Quality:");
  Serial.print(ppm);
  Serial.print(" ppm");

  if (ppm > threshold) 
    {
      Serial.println("  AQ Level HIGH");     
      tone(led,1000,200);
      digitalWrite(buz,HIGH);
    }
  else
    {
      digitalWrite(led,LOW);
      digitalWrite(buz,LOW);
      Serial.println("  AQ Level Good");
    }  
  delay (500);
}
