from time import sleep, time

import matplotlib.pyplot as plt
import RPi.GPIO as GPIO

ArrayValue = []
ArrayTime = []
time_start = time()
flag = False

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
    value_res = 0
    temp_value = 0
    for i in range(7, -1, -1):
        pow2 = 2 ** i
        temp_value = value_res + pow2
        signal = Binary_number(temp_value)
        GPIO.output(dac, signal)
        sleep(0.003)
        compVal = GPIO.input(comp)
        if compVal == 0:
            value_res += pow2
    return value_res


try:
    while True:
        value = adc()
        voltage = value / levels * maxVoltage
        ArrayValue.append(voltage)
        ArrayTime.append(time() - time_start)
        print("Digital = ", value, "Voltage = ", voltage)
        if (voltage >= 2.66) and (time() - time_start > 6):
            GPIO.output(troyka, 0)
            plt.plot(time() - time_start, voltage, "ro")
            break
    while True:
        value = adc()
        voltage = value / levels * maxVoltage
        ArrayValue.append(voltage)
        ArrayTime.append(time() - time_start)
        print("Digital = ", value, "Voltage = ", voltage)
        if voltage < 2.475 and (time() - time_start > 11):
            break
    time_finish = time()
    plt.plot(ArrayTime, ArrayValue)
    plt.show()
    with open("task.txt", 'w') as f:
        f.write("Общая продолжительность эксперимента: " + str('{:.3f}'.format(time_finish-time_start)) + " секунд" + '\n')
        f.write("Время" + '\t' + "напряжение" + '\n')
        for i in range(len(ArrayValue)):
            f.write(str('{:.3f}'.format(ArrayTime[i])) + '\t' + str('{:.3f}'.format(ArrayValue[i])) + '\n')
    with open("settings.txt", 'w') as f:
        f.write("Среднюяя частота дискретизации проведённых измерений: " + str('{:.3f}'.format(len(ArrayValue) / (time_finish-time_start))) + " Гц" + '\n')
        f.write("Шаг квантования АЦП: " + str('{:.3f}'.format(3.3 / 256)) + " Вольт" + '\n')
     
finally:
    GPIO.output(dac, 0)
    GPIO.output(troyka, 0)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")