from numpy.random import randint

import settings


class DNA(object):
    _dna_sequence = list()
    
    def __init__(self, init_sequence=None):
        if init_sequence is None:
            self._dna_sequence = randint(0, 6, settings.DNA_LENGTH)
        else:
            self._dna_sequence = [self._mutate(x) for x in init_sequence]

    def _mutate(self, gene):
        return randint(0,6) if randint(1, settings.MUTATION)==1 else gene

    def splice(dna_object):
        break_point = randint(0, settings.DNA_LENGTH)
        child1 = self._dna_sequence[:break_point] + dna_object.get_sequence()[break_point:]
        child2 = dna_object.get_sequence()[:break_point] + self._dna_sequence[break_point:]
        return child1, child2

    def get_sequence(self):
        return self._dna_sequence


class Robby(object):
    _dna = None
    
    def __init__(self):
        pass
