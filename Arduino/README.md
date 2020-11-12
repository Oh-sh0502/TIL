```java
const int tempPin = A0;
const int ledPin = A2;
boolean check = false;
void setup() {
  //analogReference(INTERNAL);
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
}
void loop() {
  delay(2000);
  digitalWrite(tempPin, HIGH);
  if(Serial.available() > 0){
    String cmd="";
    cmd = Serial.readString();
    Serial.println(cmd);
    if(cmd.equals("s")){
      check = true;
    }else if(cmd.equals("t")){
      check = false;
    }
  }
  if(check){
    float temp = analogRead(tempPin);
    temp = (temp * 5.0/1024.0)*100;
      Serial.println(temp);
      if(temp >= 30){
        digitalWrite(ledPin, HIGH);
      }else{
        digitalWrite(ledPin, LOW);
      }
   }
}
```

