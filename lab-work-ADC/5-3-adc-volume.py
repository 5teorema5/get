from time import sleep

import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13

bits = len(dac)
levels = 2**bits
maxVoltage = 3.3

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)


def Binary_number(number):
    return [int(elem) for elem in bin(number)[2:].zfill(8)]


def adc():
    value_res = 0
    temp_value = 0
    for i in range(7, -1, -1):
        pow2 = 2 ** i
        temp_value = value_res + pow2
        signal = Binary_number(temp_value)
        GPIO.output(dac, signal)
        sleep(0.005)
        compVal = GPIO.input(comp)
        if compVal == 0:
            value_res += pow2
    return value_res


try:
    while True:
        value = adc()
        voltage = value / levels * maxVoltage
        print("Digital = ", value, "Voltage = ", voltage)
        if (value/253 > 1):
            binary = [1, 1, 1, 1, 1, 1, 1, 1]
        elif (value/224 > 1):
            binary = [0, 1, 1, 1, 1, 1, 1, 1]
        elif (value/192 > 1):
            binary = [0, 0, 1, 1, 1, 1, 1, 1]
        elif (value/160 > 1):
            binary = [0, 0, 0, 1, 1, 1, 1, 1]
        elif (value/128 > 1):
            binary = [0, 0, 0, 0, 1, 1, 1, 1]
        elif (value/96 > 1):
            binary = [0, 0, 0, 0, 0, 1, 1, 1]
        elif (value/64 > 1):
            binary = [0, 0, 0, 0, 0, 0, 1, 1]
        elif (value/32 > 1):
            binary = [0, 0, 0, 0, 0, 0, 0, 1]
        else:
            binary = [0, 0, 0, 0, 0, 0, 0, 0]
        GPIO.output(leds, binary)
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")