from time import sleep

import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

bits = len(dac)
levels = 2**bits
maxVoltage = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def Binary_number(number):
    return [int(elem) for elem in bin(number)[2:].zfill(8)]


def adc():
    for value in range(256):
        a = Binary_number(value)
        GPIO.output(dac, a)
        sleep(0.005)
        compVal = GPIO.input(comp)
        if compVal == 1:
            return value
            break


try:
    while True:
        value = adc()
        if type(value) == int:
            voltage = value / levels * maxVoltage
            print("Digital = ", value, "Voltage = ", voltage)
        else:
            print("Error")
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")