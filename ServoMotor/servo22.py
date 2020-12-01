from __future__ import print_function
import time
import RPi.GPIO as GPIO

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
servo_pin = 18
print("Ultrasonic Measurement")

GPIO.setup(servo_pin,GPIO.OUT)
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)

GPIO.output(GPIO_TRIGGER,False)
time.sleep(2) # 원래 2

servo = GPIO.PWM(servo_pin, 50)
servo.start(2.5) # 원래 2.5

try:
    while True:
        distance = measure_average()
        print("Distance : %.1f" % distance)
        time.sleep(1) #

        if distance <= 10: #초음파 센서와 거리
            print("angle : 1")
            servo.ChangeDutyCycle(2.5)
        else:
            print("angle : 5")
            servo.ChangeDutyCycle(7.5)

except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()