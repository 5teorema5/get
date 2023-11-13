import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)

try:
    x = int(input("введите число от 0 до 100: "))
    p = GPIO.PWM(24, 1000)
    p.start(x)
    input("Enter чтобы завершить: ")
    p.stop()
finally:
    GPIO.output(24, 0)
    GPIO.cleanup()  

