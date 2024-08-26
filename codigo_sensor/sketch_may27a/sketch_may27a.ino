#include <Wire.h>
#include "Ultrasonic.h"
 
Ultrasonic ultrasonic(7);
 
void setup() {
  Serial.begin(9600);
  Wire.begin();
}
 
void loop() {
  // Leer la distancia en centímetros del sensor HCSR04
  long RangeInCentimeters = ultrasonic.MeasureInCentimeters();
  // Imprimir los datos en una misma línea
  Serial.println(RangeInCentimeters);
 
  delay(500);
}