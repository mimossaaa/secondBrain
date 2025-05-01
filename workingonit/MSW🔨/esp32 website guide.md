To host a simple webpage on an ESP32, we can use the ESP32's built-in Wi-Fi functionality along with an HTTP server library. Below is a step-by-step guide and sample code to get you started.

### Requirements:
- **ESP32 Development Board**
- **Arduino IDE** (with ESP32 board support installed)
- **Wi-Fi network credentials**

### Step 1: Install ESP32 in Arduino IDE
1. Open Arduino IDE and go to `File > Preferences`.
2. In the "Additional Boards Manager URLs" field, add the following URL:
   ```
   https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
   ```
3. Go to `Tools > Board > Boards Manager`, search for "esp32," and install the **ESP32** package.
4. Select your ESP32 board from `Tools > Board`.

### Step 2: Libraries Needed
Make sure the following libraries are installed (if not already included with the ESP32 package):
- **WiFi.h**
- **WebServer.h** (for handling HTTP requests)

### Step 3: Connect to Wi-Fi and Host a Webpage
Below is the code to host a simple webpage on the ESP32.

#### Code Explanation:
- The ESP32 connects to your Wi-Fi network.
- A basic HTTP server is created using the `WebServer` library.
- When the ESP32's IP is accessed in a browser, a webpage is displayed.

```cpp
#include <WiFi.h>
#include <WebServer.h>

// Replace these with your network credentials
const char* ssid = "your-SSID";
const char* password = "your-PASSWORD";

// Create a WebServer object on port 80
WebServer server(80);

// HTML content for the webpage
String htmlPage = "<!DOCTYPE html>\
<html>\
<head>\
  <title>ESP32 Webpage</title>\
  <meta charset='UTF-8'>\
  <meta name='viewport' content='width=device-width, initial-scale=1.0'>\
  <style>\
    body { font-family: Arial, sans-serif; text-align: center; padding: 20px; }\
    h1 { color: #005f9e; }\
    p { font-size: 20px; }\
  </style>\
</head>\
<body>\
  <h1>Welcome to ESP32 Webpage!</h1>\
  <p>This is a simple web server running on an ESP32.</p>\
</body>\
</html>";

// Function to handle the root path ("/")
void handleRoot() {
  server.send(200, "text/html", htmlPage);
}

void setup() {
  // Start Serial Monitor
  Serial.begin(115200);

  // Connect to Wi-Fi
  Serial.println("Connecting to Wi-Fi...");
  WiFi.begin(ssid, password);

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting...");
  }

  // Wi-Fi connected
  Serial.println("Connected to Wi-Fi!");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());  // Get the ESP32's IP address

  // Set up routes
  server.on("/", handleRoot);  // Route to handle root "/"

  // Start the server
  server.begin();
  Serial.println("HTTP server started.");
}

void loop() {
  // Handle client requests
  server.handleClient();
}
```

### Step 4: Upload the Code
1. Connect your ESP32 to your computer.
2. In Arduino IDE, select the correct **COM port** for the ESP32 (`Tools > Port`).
3. Click **Upload** to flash the code onto your ESP32.
4. Open the **Serial Monitor** to view the ESP32’s IP address after it connects to Wi-Fi.

### Step 5: Access the Webpage
1. Once the ESP32 is connected to Wi-Fi, the Serial Monitor will display the IP address (e.g., `192.168.1.100`).
2. Open a web browser and type the IP address into the address bar.
3. The webpage hosted by the ESP32 will be displayed.

### Step 6: Customizing the Webpage
- You can modify the `htmlPage` variable in the code to add more HTML, CSS, or JavaScript content to customize the webpage.

### Optional Features:
- **Handling Multiple Routes**: You can add more routes to handle different URLs. For example:
    ```cpp
    server.on("/anotherpage", handleAnotherPage);
    ```
- **Sending Sensor Data**: You can use the ESP32 to send live sensor data to the webpage.

Let me know if you'd like to expand on any features or integrate sensors!