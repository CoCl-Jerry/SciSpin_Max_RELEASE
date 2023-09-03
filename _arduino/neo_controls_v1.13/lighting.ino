void stripUpdate() {
  for (uint16_t i = 0; i < strip.numPixels(); i++) {
    if (i >= commands[2] && i < commands[3]) {
      strip.setPixelColor(i, commands[4], commands[5], commands[6], commands[7]);
    }
  }
  strip.setBrightness(int(commands[8] * 2.55));
}

void brightnessUpdate() {
  strip.setBrightness(int(commands[2] * 2.55));
}

void stripClear() {
  strip.clear();
  strip.show();
}

void stripShow() {
  strip.show();
}

void infraOn() {
  digitalWrite(IR_PIN, HIGH);
}

void infraOff() {
  digitalWrite(IR_PIN, LOW);
}
