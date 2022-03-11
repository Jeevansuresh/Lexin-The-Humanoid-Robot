/* Lexin */


/*Blynk is an open source application and webserver */

int a = 14;
int b = 12;
int c = 13;
int d = 15;


void Forward() {
  digitalWrite(a,HIGH);
  digitalWrite(b,LOW);
  digitalWrite(c,HIGH);
  digitalWrite(d,LOW);
}



void Backward() {
  digitalWrite(a,LOW);
  digitalWrite(b,HIGH);
  digitalWrite(c,LOW);
  digitalWrite(d,HIGH);
}



void Right(){
  digitalWrite(a,HIGH);
  digitalWrite(b,LOW);
  digitalWrite(c,LOW);
  digitalWrite(d,LOW);
}



void Left(){
  digitalWrite(a,LOW);
  digitalWrite(b,HIGH);
  digitalWrite(c,LOW);
  digitalWrite(d,LOW);
}



void Rotate(){
  digitalWrite(a,HIGH);
  digitalWrite(b,LOW);
  digitalWrite(c,LOW);
  digitalWrite(d,HIGH);
}



void Stop() {
  digitalWrite(a,LOW);
  digitalWrite(b,LOW);
  digitalWrite(c,LOW);
  digitalWrite(d,LOW);
}











#define BLYNK_PRINT Serial

#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <BlynkSimpleEsp8266.h>
char auth[] = "YourAuthToken"; #assigned by blynk app 
char ssid[] = "XXXXXXXXX"; /*internet ssid */
char pass[] = "XXXXXXXXX"; /* Internet pass */

ESP8266WebServer server(80);



void handleRoot() {
  server.send(200, "text/plain", "hello from Lexin!");
}


void handleNotFound() {
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += (server.method() == HTTP_GET) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";
  for (uint8_t i = 0; i < server.args(); i++) {
    message += " " + server.argName(i) + ": " + server.arg(i) + "\n";
  }
  server.send(404, "text/plain","Poda Bottu");
}

void setup(void) 
{
  pinMode(a,INPUT);
  pinMode(b,INPUT);
  pinMode(c,INPUT);
  pinMode(d,INPUT);
  Serial.begin(115200);
  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid,pass);
  Serial.println("");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");

    
 
  Serial.println("");
  
  Serial.print("Connected to ");
  
  Serial.println(ssid);
  
  Serial.print("IP address: ");
  
  Serial.println(WiFi.localIP());

  if (MDNS.begin("esp8266")) {
    
    Serial.println("MDNS responder started");
  }


  Blynk.begin(auth, ssid, pass);
}




  server.on("/", handleRoot);

  
  server.on("/f", []() {
    server.send(200, "text/plain", "Forward");
  digitalWrite(a,HIGH);
  digitalWrite(b,LOW);
  digitalWrite(c,HIGH);
  digitalWrite(d,LOW);
  });



  server.on("/b", [] () {
    server.send(200, "text/plain", "Backward");
  digitalWrite(a,LOW);
  digitalWrite(b,HIGH);
  digitalWrite(c,LOW);
  digitalWrite(d,HIGH);
  });

  
  server.on("/l", [] () {
    server.send(200, "text/plain" , "Left");
  digitalWrite(a,LOW);
  digitalWrite(b,HIGH);
  digitalWrite(c,LOW);
  digitalWrite(d,LOW);
  });


 
  server.on("/r", [] () {
    server.send(200, "text/plain" , "Right");
  digitalWrite(a,HIGH);
  digitalWrite(b,LOW);
  digitalWrite(c,LOW);
  digitalWrite(d,LOW);
    
  });


server.on("/stp", [] () {
    server.send(200, "text/plain" , "Stop");
  digitalWrite(a,LOW);
  digitalWrite(b,LOW);
  digitalWrite(c,LOW);
  digitalWrite(d,LOW);
  });
  
  server.on("/rt", [] () {
    server.send(200, "text/plain", "rotate");
  digitalWrite(a,HIGH);
  digitalWrite(b,LOW);
  digitalWrite(c,LOW);
  digitalWrite(d,HIGH);
  });

  
  server.onNotFound(handleNotFound);
  server.begin();
  Serial.println("HTTP server started");
}
void loop(void)
{
  server.handleClient();
  MDNS.update();
  Blynk.run();
}