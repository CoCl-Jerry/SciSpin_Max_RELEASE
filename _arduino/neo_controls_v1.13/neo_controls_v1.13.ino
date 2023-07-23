#include <TMC2208Stepper.h>
#include <AccelStepper.h>
#include <Adafruit_NeoPixel.h>
#include <Wire.h>
#include <avr/wdt.h>
#include <elapsedMillis.h>

#define DIR_PIN_FRAME 3
#define STEP_PIN_FRAME 4
#define EN_PIN_FRAME 5

#define DIR_PIN_CORE 10
#define STEP_PIN_CORE 11
#define EN_PIN_CORE 12

#define LED_PIN 6
#define NUM_LEDS 87

#define BUZZER_PIN A8
#define IR_PIN A0
#define FAN_PIN 8

#define SLAVE_ADDRESS 0x08
#define COMMANDSIZE 10

TMC2208Stepper frame_driver = TMC2208Stepper(&Serial1);
AccelStepper frame_stepper = AccelStepper(frame_stepper.DRIVER, STEP_PIN_FRAME, DIR_PIN_FRAME);

TMC2208Stepper core_driver = TMC2208Stepper(&Serial2);
AccelStepper core_stepper = AccelStepper(core_stepper.DRIVER, STEP_PIN_CORE, DIR_PIN_CORE);

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, LED_PIN, NEO_GRBW + NEO_KHZ800);

char data[50];
long commands[COMMANDSIZE];

int current_limit_frame = 400;
int microstep_frame = 2;
boolean dir_frame = true;

int current_limit_core = 400;
int microstep_core = 2;
boolean dir_core = true;

boolean ms_change = false;

elapsedMillis printTime;  // one second info printout timer.

void setup() {
  // Pin configurations
  pinMode(IR_PIN, OUTPUT);
  pinMode(FAN_PIN, OUTPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  // pinMode(EN_PIN_FRAME, OUTPUT);
  // pinMode(EN_PIN_CORE, OUTPUT);

  Serial.begin(9600);

  // Serial communication initialization
  Serial1.begin(115200);
  core_driver.push();

  Serial2.begin(115200);
  frame_driver.push();

  // NeoPixel strip initialization
  strip.setBrightness(100);
  strip.begin();
  strip.show();

  // Frame driver configuration
  frame_driver.pdn_disable(true);
  frame_driver.I_scale_analog(false);
  frame_driver.rms_current(current_limit_frame);
  frame_driver.toff(2);
  frame_driver.mstep_reg_select(true);
  frame_driver.microsteps(16);

  // Core driver configuration
  core_driver.pdn_disable(true);
  core_driver.I_scale_analog(false);
  core_driver.rms_current(current_limit_core);
  core_driver.toff(2);
  core_driver.mstep_reg_select(true);
  core_driver.microsteps(16);

  uint32_t data = 0;
  frame_driver.DRV_STATUS(&data);
  core_driver.DRV_STATUS(&data);

  // Frame stepper initialization
  frame_stepper.setEnablePin(EN_PIN_FRAME);
  frame_stepper.setPinsInverted(false, false, true);
  // frame_stepper.enableOutputs();
  frame_stepper.setMaxSpeed(1000);
  frame_stepper.setSpeed(533.333);

  // Core stepper initialization
  core_stepper.setEnablePin(EN_PIN_CORE);
  core_stepper.setPinsInverted(false, false, true);
  // core_stepper.enableOutputs();
  core_stepper.setMaxSpeed(1000);
  core_stepper.setSpeed(533.333);

  // I2C communication setup
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);

  // Startup tasks
  startup();

  // Fan speed increase loop
  for (int value = 100; value < 255; value++) {
    analogWrite(FAN_PIN, value);
    delay(10);
  }
  digitalWrite(FAN_PIN, HIGH);
  digitalWrite(IR_PIN, LOW);

  // core_stepper.enableOutputs();
  // frame_stepper.enableOutputs();
}

void loop() {

  // if (printTime >= 1000) {
  //   printTime = 0;
  //   float mSpeed = core_stepper.speed();
  //   Serial.print(mSpeed);
  //   Serial.print("  ");
  //   Serial.println(core_stepper.currentPosition());
  // }
  // Microstep change handling
  if (ms_change) {
    frame_driver.microsteps(microstep_frame);
    delay(10);
    core_driver.microsteps(microstep_core);
    ms_change = false;
  }

  // Frame stepper movement
  frame_stepper.runSpeed();
  // Core stepper movement
  core_stepper.runSpeed();
}
