#define LED_PIN 11  // Try 2 or 13 if you're unsure

void setup() {
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_PIN, HIGH);  // Turn LED on
  delay(500);                   // Wait half a second
  digitalWrite(LED_PIN, LOW);   // Turn LED off
  delay(500);                   // Wait half a second
}
