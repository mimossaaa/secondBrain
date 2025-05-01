

**Hardware Setup:**

1. **Connect the Gravity Sensor to the Arduino:**
    
    - Connect the sensor's TX pin to the Arduino's RX pin.
    - Connect the sensor's VCC pin to the Arduino's 5V pin.
    - Connect the sensor's GND pin to the Arduino's GND pin.
2. **Connect the LED to the Arduino:**
    
    - Connect the LED's anode (long leg) to a digital pin on the Arduino (e.g., pin 13).
    - Connect the LED's cathode (short leg) to the Arduino's GND pin.
3. **Connect the Servo Motor to the Arduino:**
    
    - Connect the servo motor's power supply (usually 4-6V) to the Arduino's 5V pin.
    - Connect the servo motor's ground to the Arduino's GND pin.
    - Connect the servo motor's signal pin to a digital pin on the Arduino (e.g., pin 9).

**Code:**

C++

```
#include <SoftwareSerial.h>
SoftwareSerial mySerial(10, 11); // RX, TX

int ledPin = 13;
int servoPin = 9;

Servo myServo;

void setup() {
  mySerial.begin(9600);
  pinMode(ledPin, OUTPUT);
  myServo.attach(servoPin);
}

void loop() {
  if (mySerial.available()) {
    String command = mySerial.readStringUntil('\n');
    command.trim();

    if (command == "led on") {
      digitalWrite(ledPin, HIGH);
    } else if (command == "led off") {
      digitalWrite(ledPin, LOW);
    } else if (command == "servo 0") {
      myServo.write(0); // 0 degrees
    } else if (command == "servo 90") {
      myServo.write(90); // 90 degrees
    } else if (command == "servo 180") {
      myServo.write(180); // 180 degrees
    }
  }
}
```

**Explanation:**

- The `SoftwareSerial` library is used to communicate with the Gravity Sensor.
- The `ledPin` and `servoPin` variables store the pin numbers for the LED and servo motor.
- The `myServo` object is created to control the servo motor.
- In the `loop` function, the code checks if there's any data available from the Gravity Sensor.
- If a command is received, it's compared to predefined strings.
- Based on the command, the LED is turned on or off, or the servo motor is positioned to the specified angle.

**Using the Gravity Sensor:**

- After uploading the code to the Arduino, open the Gravity Sensor's app and select the "Offline Voice Command" mode.
- Speak the desired command (e.g., "led on", "servo 90") into the microphone.
- The Arduino will receive the command and execute the corresponding action.

Remember to replace the placeholder strings in the code with the actual commands you want to use. You can also add more commands and actions to suit your specific needs.


---


## Connections Table

| Component      | Pin on Component | Pin on Arduino         |
| -------------- | ---------------- | ---------------------- |
| Gravity Sensor | TX               | RX                     |
| Gravity Sensor | VCC              | 5V                     |
| Gravity Sensor | GND              | GND                    |
| LED            | Anode            | Digital Pin (e.g., 13) |
| LED            | Cathode          | GND                    |
| Servo Motor    | Power            | 5V                     |
| Servo Motor    | Ground           | GND                    |
| Servo Motor    | Signal           | Digital Pin (e.g., 9)  |