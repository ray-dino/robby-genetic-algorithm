from numpy.random import rand, randint
from numpy import rint, int64

import settings


class DNA(object):
    
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

    def __init__(self, dna):
        self._dna = dna

    def mate(self, partner):
        dna1, dna2 = self._dna.splice(partner.get_dna())
        return Robby(dna1), Robby(dna2)

    def get_dna(self):
        return self._dna


class Board(object):
    
    def __init__(self):
        self._board = rint(rand(10, 10)).astype(int64)

    def get_scenario(self, x, y):
        """Return a base-10 integer that is the equivalent of the 5-digit 
        base-3 number that corresponds to one of 234 possible scenarios.

        The trit positions mean:
        North - East - West - South - Current
        3^4   - 3^3  - 3^2  - 3^1   - 3^0

        Trit value meanings:
        0 - Empty
        1 - With a can
        2 - Edge of board

        Arguments:
        x -- x-coordinate
        y -- y-coordinate

        """
        
        scenario = [
            str(self._get_trit(x, y-1)),
            str(self._get_trit(x+1, y)),
            str(self._get_trit(x-1, y)),
            str(self._get_trit(x, y+1)),
            str(self._get_trit(x, y))
        ]
        return base3_to_base10(''.join(scenario))

    def _get_trit(self, x, y):
        try:
            if x<0 or y<0:
                raise Exception
            return self._board[x, y]
        except:
            return 2

    def pickup_can(self, x, y):
        if self._board[x, y]:
            self._board[x, y] = 0
            return True
        else:
            return False


def base3_to_base10(base3_str):
    strlen = len(base3_str)
    base10_int = 0
    for index, value in enumerate(base3_str):
        base10_int += int(value) * 3**(strlen-1-index)
    return base10_int
