import logging
import numpy as np

import settings


class DNA(object):
    
    def __init__(self, init_sequence=None):
        if init_sequence is None:
            self._dna_sequence = np.random.randint(0, 7, settings.DNA_LENGTH)
        else:
            self._dna_sequence = [self._mutate(x) for x in init_sequence]

    def _mutate(self, gene):
        return (np.random.randint(0, 7) 
            if np.random.randint(1, settings.MUTATION)==1 
            else gene)

    def splice(self, dna_object):
        break_point = np.random.randint(0, settings.DNA_LENGTH)
        child1 = np.concatenate((
            self._dna_sequence[:break_point],
            dna_object.get_sequence()[break_point:]))
        child2 = np.concatenate((
            dna_object.get_sequence()[:break_point],
            self._dna_sequence[break_point:]))
        return DNA(child1), DNA(child2)

    def get_sequence(self):
        return self._dna_sequence

    def get_gene(self, position):
        return self._dna_sequence[position]


class Robby(object):

    def __init__(self, dna=None):
        if dna is None:
            self._dna = DNA()
        else:
            self._dna = dna
        self._fitness = 0
        self._position = {'y': 0, 'x': 0}
        self._actions = {
            0: self._move_north,
            1: self._move_east,
            2: self._move_west,
            3: self._move_south,
            4: self._move_random,
            5: self._stay_put,
            6: self._pick_up
        }

    def mate(self, partner):
        dna1, dna2 = self._dna.splice(partner.get_dna())
        return Robby(dna1), Robby(dna2)

    def get_dna(self):
        return self._dna

    def live(self):
        scores = []
        for i in range(0, settings.TRIES):
            trial_fitness = 0
            board = Board()
            self._position = {'y': 0, 'x': 0}
            for step in range(0, settings.LIFESPAN):
                scenario = board.get_scenario(**self._position)
                gene = self._dna.get_gene(scenario)
                trial_fitness = self._actions[gene](board, trial_fitness)
            scores.append(trial_fitness)
        self._fitness = np.array(scores).mean()
        logging.debug("Individual Fitness {}".format(self._fitness))
                    
    def get_fitness(self):
        return self._fitness

    def _move_north(self, board, fitness):
        if self._position['y']==0:
            fitness -= settings.CRASH_PENALTY
        else:
            self._position['y'] -= 1
        return fitness

    def _move_east(self, board, fitness):
        y, x = board.get_size()
        if self._position['x']==x-1:
            fitness -= settings.CRASH_PENALTY
        else:
            self._position['x'] += 1
        return fitness

    def _move_west(self, board, fitness):
        if self._position['x']==0:
            fitness -= settings.CRASH_PENALTY
        else:
            self._position['x'] -= 1
        return fitness
        
    def _move_south(self, board, fitness):
        y, x = board.get_size()
        if self._position['y']==y-1:
            fitness -= settings.CRASH_PENALTY
        else:
            self._position['y'] += 1
        return fitness

    def _move_random(self, board, fitness):
        action = np.random.choice([
            self._move_north,
            self._move_east,
            self._move_west,
            self._move_south
        ])
        return action(board, fitness)

    def _stay_put(self, board, fitness):
        return fitness

    def _pick_up(self, board, fitness):
        if board.cleanup_site(**self._position):
            fitness += settings.PICKUP_POINTS
        else:
            fitness -= settings.PICKUP_PENALTY
        return fitness


class Board(object):
    
    def __init__(self):
        self._board = np.rint(np.random.rand(10, 10)).astype(np.int64)

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

    def cleanup_site(self, x, y):
        if self._board[x, y]:
            self._board[x, y] = 0
            return True
        else:
            return False

    def get_size(self):
        return self._board.shape


def base3_to_base10(base3_str):
    strlen = len(base3_str)
    base10_int = 0
    for index, value in enumerate(base3_str):
        base10_int += int(value) * 3**(strlen-1-index)
    return base10_int
