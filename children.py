from random import random, choices
from Adaptation.setup import k, size, gens

# This class is used to create ChildCreatures by pairing two adult Creatures
class ChildCreature:
    def __init__(self, genes1, genes2):
        self.X = round(random() * size)
        self.Y = round(random() * size)
        self.parant_genes1 = genes1
        self.parant_genes2 = genes2
        self.gen = self.genom()

    def genom(self):
        gen = ''
        genes = choices(self.parant_genes1, k=int(len(self.parant_genes1)/2))
        genes += choices(self.parant_genes2, k=int(len(self.parant_genes2)/2))
        for i in range(len(self.parant_genes1)):
            gen += f'{genes[i]} '
        return gen

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

def mutation(creature):
    gen = ''
    genes = creature.gen.split()
    genes.remove(*choices(genes, k=1))
    genes += choices(gens, k=1)
    for i in range(len(genes)):
        gen += f'{genes[i]} '
    creature.gen = gen
