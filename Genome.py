from random import choice, random
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

'''
Задать гены последовательностью 16 кода
'''

'''
CONFIG
size = 128 * 128
creatures = 50
'''
# Example gen - 00010203 04050607 08090A0B 0C0D0E0F
creatures = 50
creatures_list = {}

# Creating 256 possible gens
gens = [hex(i) for i in range(16*16)]

# This class creating cretures with different propertys
class Creature:
    def __init__(self):
        self.X = round(random() * 128)
        self.Y = round(random() * 128)
        self.gen = self.genom()

    @staticmethod
    def genom():
        counter = 1
        gen = ''
        while counter <= 4:
            gen += f'{choice(gens)} '
            counter += 1
        return gen

    def movement(self):
        genes = self.gen.split()
        if hex(0) in genes and 2 <= self.X <= 126:
            self.X += 1
        elif hex(46) in genes and 2 <= self.X <= 126:
            self.X += -1
        elif hex(30) in genes and 2 <= self.Y <= 126:
            self.Y += 1
        elif hex(28) in genes and 2 <= self.Y <= 126:
            self.Y += -1

def create_population():
    for i in range(creatures):
        creatures_list[i] = Creature()
        plt.scatter(creatures_list[i].X, creatures_list[i].Y, marker='o', s=5)

def movement(i):
    plt.clf()
    # Drawing bounds of our little world
    plt.plot([0, 0, 128, 128, 0], [0, 128, 128, 0, 0], color='black')
    # Updating coordinates
    for i in range(creatures):
        creatures_list[i].movement()
        plt.scatter(creatures_list[i].X, creatures_list[i].Y, marker='o', s=5)

remaining_creatures = {}
def selection():
    for i in range(creatures):
        if creatures_list[i].X <= 64:
            remaining_creatures[i] = creatures_list[i]
    return remaining_creatures


create_population()

ani = FuncAnimation(plt.gcf(), movement, interval=100, frames=101, repeat=False)

plt.grid(b=True)
plt.show()
