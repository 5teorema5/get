import lightFunctions as j
import matplotlib.pyplot as plt
import numpy as np

photos = ["pruningphotos/white_rt.jpg", "pruningphotos/white_nk.jpg", "pruningphotos/red_nk.jpg", "pruningphotos/yellow_nk.jpg", "pruningphotos/green_nk.jpg","pruningphotos/blue_nk.jpg"]

rgb, I0 = j.read_image(photos[0], 'graph_white_rt.png', 'ртутная лампа', 'белый лист')
rgb1, I1 = j.read_image(photos[1], 'graph_white_nk.png', 'лампа накаливания', 'белый лист')
rgb2, I2 = j.read_image(photos[2], 'graph_red_nk.png', 'лампа накаливания', 'красный лист')
rgb3, I3 = j.read_image(photos[3], 'graph_yellow_nk.png', 'лампа накаливания', 'жёлтый лист')
rgb4, I4 = j.read_image(photos[4], 'graph_green_nk.png', 'лампа накаливания', 'зелёный лист')
rgb5, I5 = j.read_image(photos[5], 'graph_blue_nk.png', 'лампа накаливания', 'синий лист')

red = [r[0] for r in rgb]
red_max = max(red)
print(red_max)
index_red_max = red.index(red_max)
alfa = 650 / index_red_max
print(alfa)

x = np.linspace(0, 315, 315)
x = [i * alfa for i in x]

plt.cla()
plt.clf()
ax = plt.axes()
ax.set_facecolor(color='#E5E4E2')

plt.plot(x, I1, color='white', label='white')
plt.plot(x, I2, color='red', label='red')
plt.plot(x, I3, color='yellow', label='yellow')
plt.plot(x, I4, color='green', label='green')
plt.plot(x, I5, color='blue', label='blue')

plt.legend()
plt.title('Отражённая интенсивность излучения лампы накаливания')
plt.ylabel('Яркость')
plt.xlabel('Длина волны, нм')

ax.grid(which='major', linewidth=1)
ax.grid(which='minor', linewidth=0.7, linestyle='--')
ax.minorticks_on()

plt.savefig('intensity.png')
plt.cla()
plt.clf()

A1 = [I1[i] / I1[i] for i in range(0, len(I1), 5)]
A2 = [I2[i] / I1[i] for i in range(0, len(I1), 5)]
A3 = [I3[i] / I1[i] for i in range(0, len(I1), 5)]
A4 = [I4[i] / I1[i] for i in range(0, len(I1), 5)]
A5 = [I5[i] / I1[i] for i in range(0, len(I1), 5)]

ax = plt.axes()
ax.set_facecolor(color='#E5E4E2')

plt.plot(x[::5], A1, color='white', label='white')
plt.plot(x[::5], A2, color='red', label='red')
plt.plot(x[::5], A3, color='yellow', label='yellow')
plt.plot(x[::5], A4, color='green', label='green')
plt.plot(x[::5], A5, color='blue', label='blue')

plt.legend()
plt.title('Зависимость альбедо поверхностей от длины волны падающего света')
plt.ylabel('Альбедо')
plt.xlabel('Длина волны, нм')

ax.grid(which='major', linewidth=1)
ax.grid(which='minor', linewidth=0.7, linestyle='--')
ax.minorticks_on()

plt.savefig('dependence.png')