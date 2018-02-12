// This #include statement was automatically added by the Particle IDE.
#include <Adafruit_DHT.h>

//define the pin and dht type for the dht sensor
#define DHT_PIN 0
#define DHT_TYPE DHT11

//define the ints for the other sensors
#define PHOTORESISTOR_PIN A0
#define SOILMOISTUREPIN A2

//define the port and ip address of the server
#define SERVER_PORT 8080
#define SERVER_IP {192, 168, 1, 8}


//declare the variables that will hold the values for the sensors
float temperature;
float humidity;
float prValue;      //photo resistor value
int moistureValue;  //soil moisture value

//create the dht sensor object
DHT dht(DHT_PIN, DHT_TYPE);

//create the tcp client object that the photon will use to 
TCPClient client;

//create the byte array
byte serverIP[] = SERVER_IP;

//this byte array will hold the mac address of the photon
byte photonMacAddress[6];
String macAddress;



//the setup function runs on the initial start up of the firmware
void setup() {
    //start the dht sensor
    dht.begin();
    
    //set up the pin for the photoresistor
    pinMode(PHOTORESISTOR_PIN, INPUT);
    //set up the pin for the soil moisture sensor
    pinMode(SOILMOISTUREPIN, INPUT);
    
    
    
    //set up the network item on the photon to grab the mac address
    WiFi.macAddress(photonMacAddress);
    
    //convert the byte array to a string
    for (int i = 5; i > 0; i--) {
        macAddress += photonMacAddress[i]>>4; //>>4
        macAddress += photonMacAddress[i]&0x0f; //&0x0f
        
        if(i != 1) {
            macAddress += ":";
        }
    }
    Particle.publish("mac address", macAddress);
    //delay(10000);
}

//the main loop. the photon reruns this loop over and over again until
//the device is turned off or the code is updated
void loop() {
    
    //--------------------------------------------------
    //grab the temerature from the DHT sensor
    temperature = dht.getTempFarenheit();
    
    //grab the humidity from the DHT sensor
    humidity = dht.getHumidity();
    
    //grab the photo resistor measurement
    prValue = analogRead(PHOTORESISTOR_PIN);
    //find the light value
    int light = (prValue / 4096 * 100);
    
    //grab the soil mosture value
    moistureValue = analogRead(SOILMOISTUREPIN);
    
    
    //grab the current time of gathering all the sensor data
    //and create a string out of the data
    String tStamp = String(Time.month()) + "/";
    tStamp += String(Time.day()) + "/";
    tStamp += String(Time.year()) + "--";
    tStamp += String(Time.hour()) + ":";
    tStamp += String(Time.minute()) + ":";
    tStamp += String(Time.second());
    //--------------------------------------------------
    
    //--------------------------------------------------
    //connect to the server
    if(client.connect(serverIP, SERVER_PORT)) {
        
        //first send over the mac address of the photon
       client.write("mac address~" + macAddress);
        
        
        //if the connection is good, then pubhish the information
        //to the console and to the server
        Spark.publish("temperature: ", String(temperature) + "°F");
        client.write("temperature~" + String(temperature));
        delay(100);
        
        //send the humidity level to the server
        Spark.publish("humidity:", String(humidity));
        client.write("humidity~" + String(humidity));
        delay(100);
        
        //send the light value
        Spark.publish("Light value:", String(light));
        client.write("light~" + String(light));
        delay(100);
        
        //send the moisure value
        Spark.publish("moisture value:", String(moistureValue));
        client.write("moisture~" + String(moistureValue));
        delay(100);
        
        //send the time stamp
        Spark.publish("Time stamp:", tStamp);
        client.write("Time~" + tStamp);
        delay (100);
        
        //flush out what ever is in the socket and
        //end the connection to the server for now
        //delay the connection to the server again
        //for additional 19.83 minutes (the .167 minutes
        //will be delayed no matter if the connection
        //was successful or not)
        client.flush();
        client.stop();
        delay(1170000);
    }
    //if the connection fails, then print out an error message
    else {
        Spark.publish("connection failed", "could not connect to server IP: " + String(serverIP[0]) + String(serverIP[1]) + String(serverIP[2]) + String(serverIP[3]) +"    PORT: " + String(SERVER_PORT));
    }
    //--------------------------------------------------
    
    
    //delay the whole loop 20 minutes so that that the particle is not constantly
    //connecting and reconnecting to the server bogging it down with connection request
    delay(6000);
}