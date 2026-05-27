class Nodo:
    def __init__(self, Chromosome):
        self._Chromosome = Chromosome

    def __hash__(self):
        return hash(self._Chromosome)

    def __eq__(self, other):
        if other is None:
            return False
        return self._Chromosome == other._Chromosome