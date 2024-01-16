# IMPORTS
import copy
import random
import time
import math
from bh_grammar import *
from sortedcontainers import SortedKeyList


# Data type for storing tricks and their heuristic score
class Trick:
    def __init__(self, trick, results, heuristic):
        self.trick = trick
        self.score = calcScore(trick, results, heuristic)


# Getter for score attribute 
get_score = lambda trick: trick.score


# Calculates the score for a given trick and associated results
# Low scoring tricks expanded first
def calcScore(trick, results, heuristic):
    if heuristic == 'BFS':
        return len(trick)
    elif heuristic == 'DFS':
        return 0 - len(trick)
    elif heuristic == '%Success':
        return (list(map(checkSuccess, results))).count(False)
    else:
        raise ValueError("heuristic has unexpected value")
    
        
# Returns a list of tricks obtained by adding an action to the end of an existing trick
def synthesis(tricks, maxlength):
    new_tricks = []
    while not new_tricks:
        if not tricks:
            return [],[]
        while len(tricks[0].trick) >= maxlength:
            tricks.pop(0)
            if not tricks:
                return [],[]  
        if not tricks[0].trick:
            ops = noop_grammar()
        elif tricks[0].trick[-1] == turntop:
            ops = tt_grammar()
        elif tricks[0].trick[-1] == turntop2:
            ops = tt2_grammar()
        elif tricks[0].trick[-1] == toptobottom:
            ops = ttb_grammar()
        elif tricks[0].trick[-1] == top2tobottom:
            ops = t2tb_grammar()
        elif tricks[0].trick[-1] == cut:
            ops = c_grammar()
        for op in ops:
            trick = copy.copy(tricks[0].trick)
            if trick.count(op) < 4:
                trick.append(op)
                new_tricks.append(trick)
        tricks.pop(0)
    return new_tricks, tricks


# Performs trick on example inputs and returns results
def verifyOnExamples(trick, examples):
    results = []
    for i in range(len(examples)):
        example = copy.copy(examples[i])    
        deck = performTrick(trick, example)
        results.append(deck)
    return results


# Performs trick on all possible inputs
# On finding counterexample for trick, returns it
# If no such input found, returns None
def verifyOnAll(trick):
    inputs = [[a,b,c,d] for a in range(0,4) for b in range(0,4) for c in range(0,4) for d in range(0,4)]
    for i in range(len(inputs)):
        sample = copy.copy(inputs[i])
        deck = performTrick(trick, sample)
        if not(checkSuccess(deck)):
            return inputs[i]
    return None


# Main CEGIS loop
# Keeps a list of generated tricks sorted low to high by score on heuristic
# Each iteration considers a list of new_tricks from synthesis()
# Send each trick to verifyOnExamples()
# If successful on all examples, send to verifyOnAll()
# If counterexample exists, it is added to examples, else trick is added to solutions
# All tricks (regardless of success) added to tricks for future calls to synthesis()
# Ends when no new tricks can be synthesised
def cegis(setting, target, maxlength, heuristic):
    examples = []
    solutions = []
    tricks = SortedKeyList(key=get_score)
    new_tricks = [[]]
    while new_tricks:
        for trick in new_tricks:
            if trick not in solutions:
                results = verifyOnExamples(trick, examples)
                if all(list(map(checkSuccess, results))):
                    cex = verifyOnAll(trick)
                    if cex is None: 
                        if setting == 1:
                            return trick
                        elif setting == 2 and trick.count(cut) >= 2 and trick[-1] != cut:
                            return trick
                        elif setting == 3 and trick == target:
                            return trick
                        else:
                            solutions.append(trick)
                            tricks.add(Trick(trick, results, heuristic))
                            temp = open("temp.txt","a")
                            temp.write("a")
                            temp.close()
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


# Performs the given trick on the given input
def performTrick(trick,inputs):
    deck = [(1,"facedown"),(2,"facedown"),(3,"facedown"),("audience","facedown")]
    for op in trick:
        if op == cut:
            deck = op(deck,inputs[0])
            inputs.pop(0)
        else:
            deck = op(deck)
    return deck


# Returns True if a given deck has the audience card is facing the opposite way to all other cards
# Returns False otherwise
def checkSuccess(deck):
    up_count = 0
    down_count = 0
    for card in deck:
        if card[1] == "faceup":
            up_count += 1
        elif card[1] == "facedown":
            down_count += 1
    if (up_count + down_count == len(deck)) and (up_count == 1):
        for card in deck:
            if card[0] == "audience" and card[1] == "faceup":
                return True
            elif card[0] == "audience" or card[1] == "faceup":
                return False
    elif (up_count + down_count == len(deck)) and (down_count == 1):
        for card in deck:
            if card[0] == "audience" and card[1] == "facedown":
                return True
            elif card[0] == "audience" or card[1] == "facedown":
                return False
    else:
        return False


# 1 = Return first result
# 2 = Return first meaningful results
# 3 = Return target result
# 4 = Return all results with a maximum length
##setting = 1
##target = []
##length = 10
##heuristic = 'BFS'
##solution = cegis(setting, target, length, heuristic)
