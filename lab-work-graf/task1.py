import matplotlib.pyplot as plt
import matplotlib.pyplot as ticker
import numpy as np


def n_largest_indices(arr, n):
    return int(np.argpartition(arr, -n)[-n:])


with open("settings-copy.txt", 'r') as file:
    tmp = [float(i) for i in file.read().split('\n')]
data_array = np.loadtxt("task.txt")
for i in range(len(data_array)):
    data_array[i] = float(data_array[i])*tmp[1]

with open("time-copy.txt", 'r') as file:
    x = [i for i in file.read().split('\n')]

fig, ax = plt.subplots(figsize=(16, 10), dpi=200)
ax.plot(x[:-1], data_array, label="V(t)",
        marker=".", linestyle="-",
        color='k', linewidth=1, markevery=20)




ax.minorticks_on()
ax.grid(which = 'minor', color = 'grey', linestyle=':')

plt.title("Рис 1 Процесс заряда и разряда конденсатора в RC-цепочке", size=10)
plt.xlabel("Время, с", size=9)
plt.ylabel("Напряжение, В", size=9)
plt.legend()
plt.xticks([0, 50, 100, 150, 200, 250, 300, 350, 400])
p = n_largest_indices(data_array, 1)
plt.text(300, 2.21, "Время зарядки равно {t} с".format(t=x[p]), fontsize=9, color='r')
plt.xlim(-10, 450)
plt.ylim(0, 3)
plt.grid(color = "k")
plt.show()