void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT); // LED Azul (Red Bull RB18)
  pinMode(3, OUTPUT); // LED Rojo (Porsche 911 GT3 RS)
  pinMode(4, OUTPUT); // LED Verde (BMW M4 DTM)
}

void loop() {
  if (Serial.available()) {
    char data = Serial.read();

    // Apagar todos primero
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);

    // Encender solo el que corresponde
    if (data == 'R') digitalWrite(2, HIGH);     // Red Bull
    else if (data == 'P') digitalWrite(3, HIGH); // Porsche
    else if (data == 'B') digitalWrite(4, HIGH); // BMW
    // 'N' ya los deja apagados
  }
}
