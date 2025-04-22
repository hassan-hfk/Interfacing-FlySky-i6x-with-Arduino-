char val;
#define PPM_PIN 3                 // Output pin for PPM signal (D3 on Nano)
#define NUM_CHANNELS 6
#define FRAME_LENGTH 20000       // Total frame time in microseconds
#define PULSE_WIDTH 400          // Sync pulse width (low pulse)
#define CHANNEL_GAP 300          // Fixed pulse before each channel

int channel[NUM_CHANNELS] = {1486, 1486, 1000, 1486, 1800, 2000};

void setup() {
  pinMode(PPM_PIN, OUTPUT);
  digitalWrite(PPM_PIN, HIGH);  // PPM idle state is HIGH
  Serial.begin(9600);
  Serial.println("FlySky Trainer Mode - PPM Generator Ready");
}

void loop() {
  // Handle serial input and update channel values
  if (Serial.available() < 1 ) {
    channel[1] = 1472;
    channel[0] = 1486;
    channel[3] = 1486;
  }
  while (Serial.available() > 0) {
    val = tolower(Serial.read());

    switch (val) {
      case 'w':
        if (channel[1] < 2000 ) {channel[1]++;};
        break;    // Forward Pitch
      case 's':
        if (channel[1] > 1000 ) {channel[1]--;};
        break;    // Backward Pitch
      case 'd':
        if (channel[0] < 2000 ) {channel[0]++;};
        break;// Right Roll
      case 'a':
        if (channel[0] > 1000 ) {channel[0]--;};
        break;// Left Roll
      case 'e':
        if (channel[2] < 2000 ) {channel[2]++;};
        break; // Throttle Up
      case 'q':
        if (channel[2] > 1000 ) {channel[2]--;};
        break;// Throttle Down
      case 'm':
        if (channel[3] < 2000 ) {channel[3]++;};
        break;// Yaw Right
      case 'n':
        if (channel[3] > 1000 ) {channel[3]--;};
        break; // Yaw Left
    }
  }

  // Debug print of all channel values

  Serial.print(channel[0]);
  Serial.println();

  // Generate PPM frame
  unsigned long frame_start = micros();
  unsigned long elapsed_time = 0;

  for (int i = 0; i < NUM_CHANNELS; i++) {
    digitalWrite(PPM_PIN, LOW);
    delayMicroseconds(PULSE_WIDTH);

    digitalWrite(PPM_PIN, HIGH);
    delayMicroseconds(channel[i] - PULSE_WIDTH);
    elapsed_time += channel[i];
  }

  // Sync gap
  unsigned long sync_gap = FRAME_LENGTH - elapsed_time;
  digitalWrite(PPM_PIN, LOW);
  delayMicroseconds(PULSE_WIDTH);
  digitalWrite(PPM_PIN, HIGH);
  delayMicroseconds(sync_gap - PULSE_WIDTH);  // Rest of sync gap
}
