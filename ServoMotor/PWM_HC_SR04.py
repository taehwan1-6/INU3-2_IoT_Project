import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO_TRIGGER = 23
GPIO_ECHO = 24
print("Ultrasonic Measurement")

GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)

GPIO.output(GPIO_TRIGGER,False)
time.sleep(2)

try:
    while True:
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        while GPIO.input(GPIO_ECHO) == 0:
            start = time.time()

        while GPIO.input(GPIO_ECHO) == 1:
            stop = time.time()

        elapsed = stop - start
        distance = (elapsed * 34300) / 2

        print("Distance %.1f cm" % distance)
        time.sleep(0.4)
        
except KeyboardInterrupt:
    print("Measurement stopped by User")
    GPIO.cleanup()

# def measure():
    
#     start = time.time()

    

    

#     return distance

# def measure_average():
#     distance1 = measure()
#     time.sleep(0.1)
#     distance2 = measure()
#     time.sleep(0.1)
#     distance3 = measure()
#     distance = distance1 + distance2 + distance3
#     distance = distance / 3
#     return distance




# servo = 18


# GPIO.setup(servo,GPIO.OUT)


# p = GPIO.PWM(servo, 50)
# p.start(2.5)

