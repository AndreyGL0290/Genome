from random import random, choices

class ChildCreature:
    def __init__(self, genes1, genes2):
        self.X = round(random() * 128)
        self.Y = round(random() * 128)
        self.parant_genes1 = genes1
        self.parant_genes2 = genes2
        self.gen = self.genom()

    def genom(self):
        gen = ''
        genes = choices(self.parant_genes1, k=int(len(self.parant_genes1)/2))
        genes += choices(self.parant_genes2, k=int(len(self.parant_genes2)/2))
        for i in range(len(self.parant_genes1)):
            print()
            gen += f'{genes[i]} '
        return gen

jimmy = ChildCreature([hex(0), hex(1), hex(2), hex(3)], [hex(252), hex(253), hex(254), hex(255)])
print(jimmy.gen)
