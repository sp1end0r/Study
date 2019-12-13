#include <SoftwareSerial.h>
#include <string.h>
#define ssid "U+Net4AA0"
#define password "5000025115"

SoftwareSerial espSerial(2, 3);
int cmdSize = 0;
long previousMillis = 0;
int GasPin = A0;                        
boolean flag;

void setup(void)
{
  Serial.begin(9600);
  espSerial.begin(9600);
  connectWifi();
}

 
void loop(void)
{
  int result = gas_sensor();
  long currentMillis = millis();
  if(currentMillis - previousMillis >= 7000)
  {
    previousMillis = currentMillis;
    requestBusInfo(result, flag);
  }



  if(espSerial.available())

  {
    Serial.write(espSerial.read());

  }
  
   delay(30000000000);
}



void connectWifi()

{

  espSerial.println("AT+CWMODE=1");

  while(espSerial.available()){
    Serial.write(espSerial.read());
  }

  delay(500);

  espSerial.println("AT+CIPMUX=0");

  while(espSerial.available()){

    Serial.write(espSerial.read());

  }

  delay(500);
  espSerial.print("AT+CWJAP=\"");
  espSerial.print(ssid);
  espSerial.print("\",\"");
  espSerial.print(password);

  espSerial.println("\"");

  while(espSerial.available()){

    Serial.write(espSerial.read());

  }

}



void requestBusInfo(int data, bool flag){
  String cmd = "GET /insert_data.php?sensor='gas'&data="+String(data)+"&flag="+String(flag)+" HTTP/1.1";

  //cmdSize = strlen("GET /insert_data.php?data=123&flag=1 HTTP/1.1")

  //            + strlen("Host:116.36.56.97\r\n\r\n") + 2;
  cmdSize = cmd.length()+ strlen("Host:116.36.56.97\r\n\r\n") + 2;

  espSerial.println("AT+CIPSTART=\"TCP\",\"116.36.59.97\",80");

  delay(500);

  espSerial.print("AT+CIPSEND=");

  delay(100);

  espSerial.println(cmdSize);

  delay(100);

  espSerial.println(cmd);

  espSerial.println("Host:116.36.56.97\r\n\r\n");

} 

int gas_sensor()
{
  int res = analogRead(GasPin);
  if (res >200) 
  {
    flag = true;
  }
  else 
  {
    flag = false;
  }
  return res;
}