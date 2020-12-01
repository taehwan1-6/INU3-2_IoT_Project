from __future__ import print_function
import time
import RPi.GPIO as GPIO
import requests, json
from example import *
from button import *



def measure():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()

    while GPIO.input(GPIO_ECHO) == 0:
        start = time.time()

    while GPIO.input(GPIO_ECHO) == 1:
        stop = time.time()

    elapsed = stop-start
    distance = (elapsed * 34300) / 2
    

    return distance

def measure_average():
    distance1 = measure()
    time.sleep(0.1)
    distance2 = measure()
    time.sleep(0.1)
    distance3 = measure()
    distance = distance1 + distance2 + distance3
    distance = distance / 3
    return distance

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_TRIGGER = 23
GPIO_ECHO = 24
servo_pin1 = 18
servo_pin2 = 26
print("Ultrasonic Measurement")

GPIO.setup(servo_pin1,GPIO.OUT)
GPIO.setup(servo_pin2,GPIO.OUT)

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)

GPIO.output(GPIO_TRIGGER,False)
time.sleep(2) # 원래 2

p1 = GPIO.PWM(servo_pin1, 50)
p2 = GPIO.PWM(servo_pin2, 50)
p1.start(0) # 원래 2.5
p2.start(12.5) # 원래 2.5

GPIO.add_event_detect(button_pin, GPIO.RISING, callback=button_callback)

try:
    while True:
        distance = measure_average()
        print("Distance : %.1f" % distance)
        time.sleep(1) #

        if distance <= 10: #초음파 센서와 거리
            print("angle : 1")
            p1.ChangeDutyCycle(12.5)
            p2.ChangeDutyCycle(3)
            time.sleep(1)

            current_weight = hx.get_weight(5)
            print("현재무게 :%dg" % current_weight)

            hx.power_down()
            hx.power_up()
            time.sleep(0.1)

            # URL = 'http://52.79.170.214:8080/useHistory'
            # data = {"serialNumber":"juhwan0815","currentCapacity": current_weight-100}
            # res = requests.post(URL, data=json.dumps(data), headers={'Content-type': 'application/json'})
            # print(res.status_code)
            # print(res.text)
            # res.close()
        else:
            print("angle : 5")
            p1.ChangeDutyCycle(3)
            p2.ChangeDutyCycle(12.5)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()