import numpy as np
import paho.mqtt.client as mqtt #import the client1
import time
from Adafruit_IO import Client, Feed, Data, RequestError
import datetime
import requests
import json

ADAFRUIT_IO_USERNAME = "bwolfram1"
ADAFRUIT_IO_KEY = "aio_EOsJ05WNtHaudEGCtmrArBct2HRC"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

coords = [[33.770472, -84.400666, "overpass"],
        [33.745724, -84.349055, "overpass"],
        [33.756156, -84.388767, "building"], 
        [33.777780, -84.387398, "building"]]

def on_message(client, userdata, message):
    obj = str(message.payload.decode("utf-8"))
    rl = int(np.random.random()*len(coords))
    if obj == "positive":
        if coords[rl][2] == "overpass":
            data = 1
        elif coords[rl][2] == "building":
            data = 2
        elif coords[rl][2] == "bridge":
            data = 3
    #elevation_url = 'https://api.open-elevation.com/api/v1/lookup?locations=' + str(coords[rl][0]) + ',' + str(coords[rl][1])
    #elevation = json.loads(requests.get(elevation_url).content)['results'][0]['elevation']
    elevation = 295
    print(rl)
    metadata = {'lat': coords[rl][0],
            'lon': coords[rl][1],
            'ele': elevation,
            'created_at': None}
    aio.send_data('cracks', data, metadata)
 
mqttBroker ="test.mosquitto.org"

client = mqtt.Client("BrokerServer")
client.connect(mqttBroker) 

client.loop_start()

client.subscribe("openmv/corn")

client.on_message=on_message 

time.sleep(60)
client.loop_stop()