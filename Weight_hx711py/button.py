import RPi.GPIO as GPIO
import time
import requests,json
from example import *

def button_callback(channel):
    start_weight = hx.get_weight(5)
    print("처음무게: %dg" % start_weight)

    hx.power_down()
    hx.power_up()
    time.sleep(0.1)

    URL = 'http://52.79.170.214:8080/disinfectant'
    data = {"serialNumber":"juhwan0815","startWeight": start_weight-100}
    res = requests.post(URL, data=json.dumps(data), headers={'Content-type': 'application/json'})
    print(res.status_code)
    print(res.text)
    res.close()

button_pin = 15

GPIO.setmode(GPIO.BCM)
GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)