# IMPORTS
import copy
import random
import time
import math
from sortedcontainers import SortedKeyList


# Data type for storing tricks and their heuristic score
class Trick:
    def __init__(self, trick, results, heuristic):
        self.trick = trick
        self.score = calcScore(trick, results, heuristic)


# Getter for score attribute 
get_score = lambda trick: trick.score


# Calculates the score for a given trick and associated results
# Higher scores more likely to be expanded first
def calcScore(trick, results, heuristic):
    if heuristic == '%Success':
        return results.count(True) + 1
    elif heuristic == 'Adapted':
        return int(round(math.e ** (-0.5 * results.count(False)), 2) * 100)
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
        r = copy.copy(tricks[i].trick)
        r.append("r")
        b = copy.copy(tricks[i].trick)
        b.append("b")
        new_tricks = [r,b]
        tricks.pop(i)
    return new_tricks, tricks


# Performs trick on example inputs and returns results
def verifyOnExamples(trick, audience, examples):
    results = []
    for i in examples:
        success = True
        if trick:
            cut = trick[i%(len(trick)):] + trick[:i%(len(trick))]
            for j in range(1,len(cut)+1-audience):
                if cut[0:audience] == cut[j:j+audience]:
                    success = False
        results.append(success)      
    return results


# Performs trick on all possible inputs
# On finding counterexample for trick, returns it
# If no such input found, returns None
def verifyOnAll(trick, audience):
    if trick:
        for i in range(len(trick)):
            cut = trick[i:] + trick[:i]
            for j in range(1,len(cut)+1-audience):
                if cut[0:audience] == cut[j:j+audience]:
                    return i
    return None


# Main CEGIS loop
# Keeps a list of generated tricks sorted low to high by score on heuristic
# Each iteration considers a list of new_tricks from synthesis()
# Send each trick to verifyOnExamples()
# If successful on all examples, send to verifyOnAll()
# If counterexample exists, it is added to examples, else trick is added to solutions
# All tricks (regardless of success) added to tricks for future calls to synthesis()
# Ends when no new tricks can be synthesised
def cegis(setting, target, audience, heuristic):
    examples = []
    solutions = []
    tricks = SortedKeyList(key=get_score)
    new_tricks = [[]]
    maxlength = 2**audience
    while new_tricks:
        for trick in new_tricks:
            if trick not in solutions:
                results = verifyOnExamples(trick, audience, examples)
                if all(results):
                    cex = verifyOnAll(trick, audience)
                    if cex is None: 
                        if setting == 1 and len(trick) == maxlength:
                            return trick
                        elif setting == 2 and len(trick) == maxlength:
                            return trick
                        elif setting == 3 and len(trick) == maxlength and trick == target:
                            return trick
                        elif len(trick) == maxlength:
                            solutions.append(trick)
                            tricks.add(Trick(trick, results, heuristic))
                            temp = open("temp.txt","a")
                            temp.write("a")
                            temp.close()
                        else:
                            tricks.add(Trick(trick, results, heuristic))
                    else:
                        examples.append(cex)
                        tricks.clear()
                        break
                else:
                    tricks.add(Trick(trick, results, heuristic))
            else:
                tricks.add(Trick(trick, results, heuristic))
        if not tricks:
            new_tricks = [[]]
        else:
            new_tricks, tricks = synthesis(tricks,maxlength)
    if setting == 4:
        return solutions
    else:
        return []
