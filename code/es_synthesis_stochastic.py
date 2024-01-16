# IMPORTS
import copy
import random
import time
import math
from sortedcontainers import SortedKeyList


# Data type for storing tricks and their heuristic score
class Trick:
    def __init__(self, trick, pos, target_pos, heuristic):
        self.trick = trick
        self.score = calcScore(trick, pos, target_pos, heuristic)


# Getter for score attribute 
get_score = lambda trick: trick.score


# Calculates the score for a given trick and associated results
# Higher scores more likely to be expanded first
def calcScore(trick, pos, target_pos, heuristic):
    if heuristic == '%Success':
        return int(checkSuccess(pos, target_pos)) + 1
    elif heuristic == 'Adapted':
        return int(round(math.e ** (-0.5 * int(checkSuccess(pos, target_pos))), 2) * 100)
    else:
        raise ValueError("heuristic has unexpected value")

        
# Returns a list of tricks obtained by adding an action to the end of an existing trick
def synthesis(tricks, maxlength):
    new_tricks = []
    while not new_tricks:
        if not tricks:
            return [],[]
        scores = list(map(get_score, tricks))
        target = random.randint(1,sum(scores))
        i = 0
        total = scores[0]
        while total < target:
            i += 1
            total += scores[i]
        while len(tricks[i].trick) >= maxlength:
            tricks.pop(i)
            if not tricks:
                return [],[]
            else:
                scores = list(map(get_score, tricks))
                target = random.randint(1,sum(scores))
                i = 0
                total = scores[0]
                while total < target:
                    i += 1
                    total += scores[i]
        i = copy.copy(tricks[0].trick)
        i.append("inS")
        o = copy.copy(tricks[0].trick)
        o.append("outS")
        new_tricks = [i,o]
        tricks.pop(0)
    return new_tricks, tricks


# Main CEGIS loop
# Keeps a list of generated tricks sorted low to high by score on heuristic
# Each iteration considers a list of new_tricks from synthesis()
# Send each trick to verifyOnExamples()
# If successful on all examples, send to verifyOnAll()
# If counterexample exists, it is added to examples, else trick is added to solutions
# All tricks (regardless of success) added to tricks for future calls to synthesis()
# Ends when no new tricks can be synthesised
def cegis(setting, target, maxlength, target_pos, heuristic):
    examples = []
    solutions = []
    tricks = SortedKeyList(key=get_score)
    new_tricks = [[]]
    while new_tricks:
        for trick in new_tricks:
            if trick not in solutions:
                pos = performTrick(trick)
                if checkSuccess(pos, target_pos):
                        if setting == 1:
                            return trick
                        elif setting == 2:
                            return trick
                        elif setting == 3 and trick == target:
                            return trick
                        else:
                            solutions.append(trick)
                            tricks.add(Trick(trick, pos, target_pos, heuristic))
                else:
                    tricks.add(Trick(trick, pos, target_pos, heuristic))
            else:
                tricks.add(Trick(trick, pos, target_pos, heuristic))
        if not tricks:
            new_tricks = [[]]
        else:
            new_tricks, tricks = synthesis(tricks,maxlength)
    if setting == 4:
        return solutions
    else:
        return []


# Performs the given trick on the given input
def performTrick(trick):
    deck = ["audience",2,3,4,5,6,7,8]
    for op in trick:
        if op == 'inS':
            deck = [deck[4],deck[0],deck[5],deck[1],deck[6],deck[2],deck[7],deck[3]] 
        elif op == 'outS':
            deck = [deck[0],deck[4],deck[1],deck[5],deck[2],deck[6],deck[3],deck[7]]
        else:
            raise ValueError('Instruction was neither inS or outS')
    return deck.index("audience")


# Returns True if a given deck has the audience card is facing the opposite way to all other cards
# Returns False otherwise
def checkSuccess(pos, target_pos):
    return pos == target_pos
