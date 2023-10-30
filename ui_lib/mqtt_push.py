import datetime

import paho.mqtt.client as mqtt
import json
# Define the MQTT broker's address and port
broker_address = "172.16.1.106"
port = 1883
# Define the topic under which you want to publish data
topic = "EMS/Data/AHUG"
op=datetime.datetime.now()
data = {"AHUGproperty": [{"property": "Mode", "value": "AUTO"}, {"property": "Air Speed", "value": 45.0},
                         {"property": "Desired Temperature", "value": 60},{"property": "VFD Status", "value": "OFF"},
                         {"property": "Relay Status", "value": "ON"},{"property": "Flow Direction", "value": "REVERSE"},
                         {"property": "System Error", "value": "Providing Test Data"},
                         {"property": "System Startup Time", "value": "2023-06-27 16:16:01"},
                         {"property": "Machine Status", "value": "OFF"},{"property": "Actual Room Temperature", "value": 25.736263736263737},
                         {"property": "AHU Room Temperature", "value": 25.4},{"property": "RPM", "value": 1177},
                         {"property": "Drive DC Voltage", "value": 595}, {"property": "Current", "value": 3.14},
                         {"property": "Power KW", "value": 1.1},
                         {"property": "Drive Temperature", "value": 33},
                         {"property": "VFD Faults", "value": "can't get data from VFD"},
                         {"property": "VFD Mode", "value": "Off"},
                         {"property": "Total Run Time Today", "value": "0:00:03"},
                         {"property": "Total Machine Run Time", "value": "4:09:09"}], "NumberofProperties": 20,
        "deviceid": 123456, "devicetype": "AHUG",
        "networkid": 55891, "responsecmd": "UpdatedData", "updatedat": str(op)}
class AHUGpro:
    def __init__(self):
           pass

# Convert the dictionary to a JSON string
    def data1(self,data):
        client = mqtt.Client()
        # Connect to the broker
        client.connect(broker_address, port)
        # Define the topic under which you want to publish data
        topic = "EMS/Data/AHUG"
        json_data = json.dumps(data)
        print(data["AHUGproperty"][0]['value'])
        #json_data = json.dumps(mes)
        # Publish the JSON data
        client.publish(topic, json_data)
        # Disconnect from the broker
        client.disconnect()
