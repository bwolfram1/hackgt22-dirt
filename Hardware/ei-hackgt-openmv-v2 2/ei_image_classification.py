# Edge Impulse - OpenMV Image Classification Example

import sensor, image, time, os, tf, uos, gc, network
from mqtt import MQTTClient

sensor.reset()                         # Reset and initialize the sensor.
sensor.set_pixformat(sensor.RGB565)    # Set pixel format to RGB565 (or GRAYSCALE)
sensor.set_framesize(sensor.QVGA)      # Set frame size to QVGA (320x240)
sensor.set_windowing((240, 240))       # Set 240x240 window.
sensor.skip_frames(time=2000)          # Let the camera adjust.

net = None
labels = None

SSID='BrandonsWifi' # Network SSID
KEY='pchs1987'  # Network key

coords = [[33.768391, -84.389796, "overpass"], [33.759056, -84.379760, "overpass"], [33.756156, -84.388767, "building"], [33.777780, -84.387398, "building"], [33.795102, -84.370808
, "bridge"], [33.764721, -84.359114, "bridge"]]

# Init wlan module and connect to network
print("Trying to connect... (may take a while)...")

wlan = network.WINC()
wlan.connect(SSID, key=KEY, security=wlan.WPA_PSK)

# We should have a valid IP now via DHCP
print(wlan.ifconfig())

client = MQTTClient("openmv", "test.mosquitto.org", port=1883)
client.connect()

try:
    # load the model, alloc the model file on the heap if we have at least 64K free after loading
    net = tf.load("trained.tflite", load_to_fb=uos.stat('trained.tflite')[6] > (gc.mem_free() - (64*1024)))
except Exception as e:
    print(e)
    raise Exception('Failed to load "trained.tflite", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')')

try:
    labels = [line.rstrip('\n') for line in open("labels.txt")]
except Exception as e:
    raise Exception('Failed to load "labels.txt", did you copy the .tflite and labels.txt file onto the mass-storage device? (' + str(e) + ')')

clock = time.clock()
while(True):
    clock.tick()

    img = sensor.snapshot()

    # default settings just do one detection... change them to search the image...
    for obj in net.classify(img, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5):
        print("**********\nPredictions at [x=%d,y=%d,w=%d,h=%d]" % obj.rect())
        img.draw_rectangle(obj.rect())
        # This combines the labels and confidence values into a list of tuples
        predictions_list = list(zip(labels, obj.output()))
    classes = net.classify(img, min_scale=1.0, scale_mul=0.8, x_overlap=0.5, y_overlap=0.5)[0][4]

    actualclass = labels[classes.index((max(classes)))]
    if actualclass == labels[1]:
        client.publish("openmv/corn", actualclass)
        print("sent")
    print(actualclass)
    print(clock.fps(), "fps")

    time.sleep(3)

client.close()
