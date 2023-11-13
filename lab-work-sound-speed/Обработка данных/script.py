import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

def speedOfSound_experiment(data_0, data_1):
    # Функция, определяющая скорость звука в ходе эксперимента

    SamplingRate = 500000 # Частота дискретизации
    L = 1.158 # Длина трубы

    max_ob0 = max(data_0)
    max_ind0 = data_0.index(max_ob0)

    max_ob1 = max(data_1)
    max_ind1 = data_1.index(max_ob1)
    print(max_ind0 , max_ind1)
    t = abs((max_ind1 - max_ind0))/SamplingRate

    return (L / t)

def speedOfSound_theory(temp, fi):
    # Функция определения скорости звука в теории
    # Возвращает два массива, в одном из которых концентрация углекислого газа
    # в другом - скорость при данной концентрации
    Mi = [0.01801, 0.02897, 0.04401]  # Молярная масса H2O, N2+O2+Ar, CO2
    Cpi = [1.863, 1.0036, 0.838]
    Cvi = [1.403, 0.7166, 0.649]
    R = 8.314

    array_a = []
    array_x = []

    x = 0 # Концентрация CO2
    for i in range(0, 100):
        x += 0.001
        M = ( fi * (Mi[0]-Mi[1]) + x * (Mi[2]-Mi[1]) + Mi[1] )
        Y = ( fi * (Mi[0] * Cpi[0] - Mi[1] * Cpi[1]) + x * (Mi[2] * Cpi[2] - Mi[1] * Cpi[1]) + Mi[1] * Cpi[1] ) / 
        ( fi * (Mi[0] * Cvi[0] - Mi[1] * Cvi[1]) + x * (Mi[2] * Cvi[2] - Mi[1] * Cvi[1]) + Mi[1] * Cvi[1] )
        a = ( Y * R * temp / M ) ** 0.5
        array_a.append(a)
        array_x.append(x*100)
    return array_a, array_x

def grafics(x, y, a):
    x = np.array(x)
    y = np.array(y)

    fig, ax = plt.subplots()

    ax.plot(x, y, label="Аналитическая зависимость",
            marker="", linestyle="-",
            color='r', linewidth=1)

    array_a_get = []

    ax.plot(1.7, a, label="Значение в воздухе: ___ [м/с], ___ [%]",
            marker="*", linestyle="",
            color='green', linewidth=1)

    ax.grid(which = "major", linewidth = 1)
    ax.grid(which = "minor", linewidth = 0.2)
    ax.minorticks_on()
    plt.text(0, 358, 'Влажность составляет ___ %\nТемпература составляет ___ по Цельсии', 
             bbox={"facecolor": "white",
                   "edgecolor": "black"}, size=7)

    plt.xlabel("Концентрация CO2 [%]", size=10)
    plt.ylabel("Скорость звука [м/с]", size=10)
    plt.legend()
    plt.show()
    # Сохраним график
    fig.savefig('SoundSpeedair.png', dpi=600)

# Запросим измеренные прибором данные
temp = float(input('Введите температуру смеси газов в трубке в Цельсиях: '))
temp += 273 # в Кельвинах
fi = float(input('Введите влажность в трубке в процентах: '))
fi /= 100

# Считаем данные, измеренные с помощью АЦП
with open ("data_0.txt", 'r') as file:
    data_0_air = []
    for f in file:
        data_0_air.append(f.split()[0])

with open ("data_1.txt", 'r') as file:
    data_1_air = []
    for f in file:
        data_1_air.append(f.split()[0])

a_air = speedOfSound_experiment(data_0_air, data_1_air)
print('Скорость звука в равна ', a_air, 'м/с')

array_a, array_x = [], []
array_a, array_x = speedOfSound_theory(temp, fi)

grafics(array_x, array_a, a_air)
