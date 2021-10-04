import RPi.GPIO as GPIO
import time

SERVO_PIN1 = 20

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(SERVO_PIN1,GPIO.OUT)

servo1 = GPIO.PWM(SERVO_PIN1,50)

servo1.start(0)


try:
    while True:
        servo1.ChangeDutyCycle(7.5)
        time.sleep(1)
        servo1.ChangeDutyCycle(12.5)
        time.sleep(1)
        servo1.ChangeDutyCycle(2.5)
        time.sleep(1)
        
except KeyboardInterrupt:
    servo1.stop()
    GPIO.cleanup()