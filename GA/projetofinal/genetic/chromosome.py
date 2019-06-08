

class Chromosome(object):
    
    def __init__(self,genes,**kwargs):
        self.genes = genes
        self.score = None
        self.fitness = self.score

    def __str__(self):
        genes = str(self.genes)
        return f'Chromosome: {genes}'

    def __repr__(self):
        return self.__str__()

    def __len__(self):
        return len(self.genes)

    def __iter__(self):
        return iter(self.genes)