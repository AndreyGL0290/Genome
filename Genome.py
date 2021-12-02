from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
from random import random, choice

'''
Задать гены последовательностью 2 кода
'''

'''
CONFIG
size = 128 * 128
creatures = 10
'''

creatures = 50
creatures_list = {}
rules = [bin(0), bin(1), bin(2), bin(3)]

def make_creature(i):
    x, y = round(128 * random()), round(128 * random())
    creatures_list[i] = {'x': x, 'y': y, 'gen': choice(rules)}
    return plt.plot(x, y, marker='o')


def make_population():
    for i in range(creatures):
        make_creature(i)

def creatures_movement(i):
    for k, v in creatures_list.items():
        for kk, vv in v.items():
#             Здесь сделать перемещение (блок сравнения генов и далее движение путем замены координат в "массиве")

make_population()
ani = FuncAnimation(plt.gcf(), creatures_movement, interval=1000)


plt.grid(b=True)
print(creatures_list)
plt.show()
