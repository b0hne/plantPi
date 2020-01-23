#include <Arduino.h>
#include <stdio.h>

const int mostureSensor2 = 7;
const int mostureSensor1 = 6;
const int mostureSensor0 = 5;


void setup() {
  Serial.begin(9600);
  Serial.begin(9600); 
}

void loop() {
  int sensorValue0 = analogRead(mostureSensor0);
  int sensorValue1 = analogRead(mostureSensor1);
  int sensorValue2 = analogRead(mostureSensor2);
  float percentage0 = (1024.0f-sensorValue0)/10.24;
  float percentage1 = (1024.0f-sensorValue1)/10.24;
  float percentage2 = (1024.0f-sensorValue2)/10.24;
 
  Serial.println(String(percentage0, 6) + " : Paprika rechts");
  Serial.println(String(percentage1, 6) + " : Chilli rechts");
  Serial.println(String(percentage2, 6) + " : Paprika links");
  delay(180000);
}