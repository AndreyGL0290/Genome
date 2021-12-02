from random import choice, random

from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

'''
Задать гены последовательностью 2 кода
'''

'''
CONFIG
size = 128 * 128
creatures = 10
'''
# Example gen - 00010203 04050607 08090A0B 0C0D0E0F
creatures = 50
creatures_list = {}
gens = [hex(i) for i in range(16*16)]
def create_gen():
    counter = 0
    gen = ''
    while counter <= 4:
        gen += f'{choice(gens)} '
        counter += 1
    return gen

def make_creature(i):
    x, y = round(128 * random()), round(128 * random())
    creatures_list[i] = {'x': x, 'y': y, 'gen': create_gen()}
    return plt.scatter(x, y, marker='o', s=5)


def make_population():
    for i in range(creatures):
        make_creature(i)

survived_cretures = {}
def choose_creatures():
    '''Here we say what factor will be killing our little creatures'''
    for k, v in creatures_list.items():
        if v['x'] <= 64:
            survived_cretures[k] = v
    return survived_cretures

x1 = []
y1 = []
def creatures_movement(i):
    global x1, y1
    plusX = 0
    plusY = 0
    if i <= 100:
        for k, v in creatures_list.items():
            # Change elifs
            genes = creatures_list[k]['gen'].split()
            if hex(0) in genes:
                plusX = 1
                plusY = 0
            elif hex(46) in genes:
                plusX = -1
                plusY = 0
            elif hex(30) in genes:
                plusX = 0
                plusY = 1
            elif hex(28) in genes:
                plusX = 0
                plusY = -1
            # size - plusX or plusY
            if 2 <= creatures_list[k]['x'] <= 126:
               creatures_list[k]['x'] += plusX
            if 2 <= creatures_list[k]['y'] <= 126:
                creatures_list[k]['y'] += plusY
            plt.clf()
            x1.insert(int(k), creatures_list[k]['x'])
            del x1[creatures::]
            y1.insert(int(k), creatures_list[k]['y'])
            del y1[creatures::]
        for i in range(creatures):
            plt.scatter(x1[i], y1[i], marker='o', s=5)
        plt.plot([0, 0, 128, 128, 0], [0, 128, 128, 0, 0], color='black')
    else:
        reproduction(choose_creatures())

def reproduction(arr):
    '''Here we cross parentes gens and making their childes'''
    for k, v in arr.items():
        pass
    return

make_population()
ani = FuncAnimation(plt.gcf(), creatures_movement, interval=100, frames=102, repeat=False)


plt.grid()

plt.show()
