import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

def binary_number(number):
    return [int(elem) for elem in bin(number)[2:].zfill(8)]

try:
    T = int(input("введите период: "))
    n_T = int(input("введите число периодов: "))
    i = 0
    for j in range(n_T):
        while i < 255:
            GPIO.output(dac, binary_number(int(i)))
            print(3.3/256*int(i), " вольт")
            i += 1
            sleep(T/512)
        while i > 0:
            GPIO.output(dac, binary_number(int(i)))
            print(3.3/256*int(i), " вольт")
            i -= 1
            sleep(T/512)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()    
