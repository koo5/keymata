void setup(void) {
    Serial.begin(38400);
    int i;
    for(i=2;i<14;i++)
        pinMode(i, OUTPUT);
}

void loop() 
{
    if (Serial.available())
    {
        byte in = Serial.read();
	byte pin = (in&0b11111110)>>1;
        byte value = in&0b00000001;
	digitalWrite(pin, value);
    }
}

