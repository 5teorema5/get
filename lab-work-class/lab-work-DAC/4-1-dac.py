import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]

GPIO.setup(dac, GPIO.OUT)

def binary_number(number):
    return [int(elem) for elem in bin(number)[2:].zfill(8)]

try:
    while True:
        n = input("введите число от 0 до 255: ")
        if n == "q":
            break
        elif n.isdigit() is False:
            print("вы введи не число или неправильное число!")
        elif int(n) > 255:
            print("вы ввели большое число!")
        else:
            GPIO.output(dac, binary_number(int(n)))
            print(3.3/256*int(n), " вольт")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()