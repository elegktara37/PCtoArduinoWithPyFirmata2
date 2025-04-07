#include <Wire.h> 
#include <LiquidCrystal_I2C.h>
#include <Firmata.h>

LiquidCrystal_I2C lcd(0x27,16,2);  // LCD I2C address

int lastLine = 1;

void getData(char *stringData){
  if (lastLine){
    lastLine = 0;
    lcd.clear();
    lcd.setCursor(0,0);
  } else {
    lastLine = 1;
    lcd.setCursor(0,1);
  }
  lcd.print(stringData);
}

void setup() {
  lcd.init();  // Initialize LCD
  lcd.backlight();  // Make sure backlight is on (optional but useful)
  
  Firmata.setFirmwareVersion(FIRMATA_MAJOR_VERSION, FIRMATA_MINOR_VERSION);
  Firmata.attach(STRING_DATA, getData);
  Firmata.begin();
}

void loop() {
  while (Firmata.available()) {
    Firmata.processInput();
  }
}
