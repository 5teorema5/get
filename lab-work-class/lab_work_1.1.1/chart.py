import matplotlib.pyplot as plt

y1 = [50.2,56.9,66.7,83.1,98.5,116.7,156.9]
x1 = [47,54,63,78,92,110,146]

plt.plot(x1, y1, label='l = 20см',
         marker = 'o', linestyle = '',
         color = 'red', linewidth=1)

plt.plot([0, 150], [0, 161],
         marker = '', linestyle = '-',
         color = 'red', linewidth=1)

y2 = [71.4,76.8,82.5,96.8,117.2,149.8,190.2]
x2 = [45,48,52,61,73,94,119]

plt.plot(x2, y2, label='l = 30см',
         marker = 'o', linestyle = '',
         color = 'green', linewidth=1)

plt.plot([0, 150], [0, 239],
         marker = '', linestyle = '-',
         color = 'green', linewidth=1)

y3 = [115.4,128.9,148.8,182.7,243.9,319.9,396.0]
x3 = [43,48,56,68,91,119,146]

plt.plot(x3, y3, label='l = 50см',
         marker = 'o', linestyle = '',
         color = 'blue', linewidth=1)

plt.plot([0, 150], [0, 403],
         marker = '', linestyle = '-',
         color = 'blue', linewidth=1)

plt.plot(0, 0)

plt.grid ( True )

plt.xlabel("I, дел - измеряемая сила тока в делениях", fontsize=8, color='k')
plt.ylabel("U, мВ - измеряемое напряжение", fontsize=8, color='k')
plt.title("Рис 1. Результаты измерений напряжений $U_{В}$ в зависимости от \nсилы тока $I_{А}$ для проволок разной длины l", fontsize=10, color='k')

plt.legend()

plt.show()