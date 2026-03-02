int buzzer_pin = 12;
int trig_pin = 9;
int echo_pin = 8;

float threshold_cm = 50.0;

long duration;
float distance;


void setup() {
  Serial.begin(9600);
  pinMode(trig_pin, OUTPUT);
  pinMode(echo_pin, INPUT);
  pinMode(buzzer_pin, OUTPUT);

}

void loop() {
  digitalWrite(trig_pin, LOW);
  delayMicroseconds(2);
  digitalWrite(trig_pin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig_pin, LOW);

  duration = pulseIn(echo_pin, HIGH);
  distance = (duration * 0.0343) / 2.0;

  Serial.print("Distance: ");
  Serial.print(distance);
  Serial.println("");

  if (distance > threshold_cm){
    tone(buzzer_pin, 1000);
  }
  else{
    noTone(buzzer_pin);
  }
  delay(200);
}
