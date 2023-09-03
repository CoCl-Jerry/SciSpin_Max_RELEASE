void motorStatus() {
  if (commands[2]!=0)
    frame_stepper.enableOutputs();
  else
    frame_stepper.disableOutputs();

  if (commands[3]!=0)
    core_stepper.enableOutputs();
  else
    core_stepper.disableOutputs();
}

void setMotor() {
  frame_stepper.setSpeed((float)commands[2] / 1000);
  microstep_frame = commands[3];

  core_stepper.setSpeed((float)commands[4] / 1000);
  microstep_core = commands[5];
  ms_change = true;
}
