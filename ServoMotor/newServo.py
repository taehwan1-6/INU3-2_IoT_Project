import RPi.GPIO as GPIO  
import time

GPIO.setmode(GPIO.BCM) 

SERVO_PIN1 = 18
SERVO_PIN2 = 26

GPIO.setup(SERVO_PIN1, GPIO.OUT)
GPIO.setup(SERVO_PIN2, GPIO.OUT)

p1 = GPIO.PWM(SERVO_PIN1, 50)
p2 = GPIO.PWM(SERVO_PIN2, 50)   

p1.start(12.5) 
p2.start(0)            

# p.ChangeDutyCycle(3) 
# sleep(1)

# p.ChangeDutyCycle(12)
# sleep(1) 

# p.ChangeDutyCycle(7.5)
# sleep(1)

# try:
#     while True:
#         if distance <= 10: #초음파 센서와 거리
#             print("angle : 1")
#             servo.ChangeDutyCycle(2.5)
#             time.sleep(1)
#         else:
#             print("angle : 5")
#             servo.ChangeDutyCycle(7.5)
#             time.sleep(1)
        
        
# except KeyboardInterrupt:
#     p1.stop()
#     p2.stop()
#     GPIO.cleanup()

try:
    while(1):

        val1 = float(input("servo1 input(3~7.5~12) = "))
        

        if val1 == -1: break

        val2 = float(input("servo2 input(3~7.5~12) = "))

        p1.ChangeDutyCycle(val1)
        p2.ChangeDutyCycle(val2)
        time.sleep(1)

  
except KeyboardInterrupt:
    p1.stop()
    p2.stop()

    GPIO.cleanup()