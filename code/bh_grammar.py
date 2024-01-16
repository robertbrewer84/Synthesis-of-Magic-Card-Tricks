def noop_grammar():
    return [turntop, turntop2, toptobottom, top2tobottom, cut]

def tt_grammar():
    return [turntop2, toptobottom, top2tobottom, cut]

def tt2_grammar():
    return [turntop, toptobottom, top2tobottom, cut]

def ttb_grammar():
    return [turntop, turntop2, top2tobottom]

def t2tb_grammar():
    return [turntop, turntop2]

def c_grammar():
    return [turntop, turntop2]
    


def turntop(deck):
    if deck[0][1] == "faceup":
        return [(deck[0][0],"facedown")] + deck[1:]
    elif deck[0][1] == "facedown":
        return [(deck[0][0],"faceup")] + deck[1:]

def turntop2(deck):
    card0 = deck[0]
    card1 = deck[1]
    if card0[1] == "faceup":
        card0 = (card0[0],"facedown")
    elif card0[1] == "facedown":
        card0 = (card0[0],"faceup")
    if card1[1] == "faceup":
        card1 = (card1[0],"facedown")
    elif card1[1] == "facedown":
        card1 = (card1[0],"faceup")
    return [card1] + [card0] + deck[2:]

def toptobottom(deck):
    return deck[1:] + [deck[0]]

def top2tobottom(deck):
    return deck[2:] + [deck[0]] + [deck[1]]

def cut(deck,n):
    return deck[n:] + deck[:n]
