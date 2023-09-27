const int switchPin = 15;
const int ledPin = 14;
int switchState = 0;
#define LED_BUILTIN 2

void setup() {
  // pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(115200);
  pinMode(switchPin, OUTPUT);
  pinMode(ledPin, OUTPUT);

}

void loop() {
  switchState = digitalRead(switchPin);
  if(switchState == HIGH){
    digitalWrite(ledPin, HIGH);
  }else{
    digitalWrite(ledPin, LOW);
  }

  // digitalWrite(LED_BUILTIN, HIGH);
  // delay(1000);
  // digitalWrite(LED_BUILTIN, LOW);
  // delay(1000);
}
