from random import choice, random
import matplotlib.pyplot as plt
from os import mkdir, getcwd, rmdir, remove
from Adaptation.setup import size, creatures, creatures_list, k, max_population, gens, mutation_delay
from Adaptation.children import ChildCreature, mutation
from sys import setrecursionlimit

setrecursionlimit(10000)

# Example gen - 00010203

# This class creating cretures with different properties
class Creature:
    def __init__(self):
        self.X = round(random() * size)
        self.Y = round(random() * size)
        self.gen = self.genom()

    @staticmethod
    def genom():
        counter = 1
        gen = ''
        while counter <= 4:
            gen += f'{choice(gens)} '
            counter += 1
        return gen

    # Function that is responsible for movement of a SINGLE creature
    # K here means coefficient
    def movement(self):
        genes = self.gen.split()
        if hex(0) in genes:
            self.X += 1 * k
            if self.X > size - 1:
                self.X = size - 1
        elif hex(4) in genes:
            self.X += -1 * k
            if self.X < 1:
                self.X = 1
        elif hex(8) in genes:
            self.Y += 1 * k
            if self.Y > size - 1:
                self.Y = size - 1
        elif hex(12) in genes:
            self.Y += -1 * k
            if self.Y < 1:
                self.Y = 1

index = 0
def create_population(population, shots):
    global index
    if population != max_population:
        plt.clf()
        if population == 0:
            for i in range(creatures):
                creatures_list[i] = Creature()
                plt.scatter(creatures_list[i].X, creatures_list[i].Y, marker='o', s=5)
        else:
            for i in range(creatures):
                plt.scatter(creatures_list[i].X, creatures_list[i].Y, marker='o', s=5)
        plt.plot([0, 0, size, size, 0], [0, size, size, 0, 0], color='black')
        try:
            if population == shots[index]:
                try:
                    remove(f'{getcwd()}\\populations\\population №{population}\\start.png')
                    remove(f'{getcwd()}\\populations\\population №{population}\\end.png')
                    rmdir(f'{getcwd()}\\populations\\population №{population}')
                except FileNotFoundError:
                    pass
                mkdir(f'{getcwd()}\\populations\\population №{population}')
                plt.savefig(f'populations\\population №{population}\\start.png')
        except IndexError:
            pass
        movement(population, shots)

# Function that is responsible for movement of EVERY creature
def movement(population, shots):
    global index
    plt.clf()
    # Drawing bounds of our little world
    plt.plot([0, 0, size, size, 0], [0, size, size, 0, 0], color='black')
    # Updating coordinates
    for i in range(creatures):
        creatures_list[i].movement()
        plt.scatter(creatures_list[i].X, creatures_list[i].Y, marker='o', s=5)
    try:
        if population == shots[index]:
            plt.savefig(f'populations\\population №{population}\\end.png')
            index += 1
    except IndexError:
        pass
    rem = selection()
    creatures_list.clear()
    reproduction(rem)
    create_population(population + 1, shots)

remaining_creatures = {}
def selection():
    for i in range(creatures):
        if creatures_list[i].X <= size / 2:
            remaining_creatures[len(remaining_creatures)] = creatures_list[i]
    return remaining_creatures

newburns = 0
def reproduction(rem):
    global newburns
    for i in range(len(rem) - 1):
        if i % 2 == 1:
            continue
        creatures_list[len(creatures_list)] = ChildCreature(rem[i].gen.split(), rem[i + 1].gen.split())
        newburns += 1
        if newburns == mutation_delay:
            mutation(creatures_list[len(creatures_list)-1])
            newburns = 0
        if len(creatures_list) == 50:
            return
    if len(creatures_list) != 50:
        reproduction(rem)

if __name__ == '__main__':
    # [i for i in range(150) if (i - 9) % 10 == 0 or i == 1] - every 10th
    create_population(0, (0, 249, 499))
