import duckControl

ducks = []

def duckGen(surface, timer):
    if timer <= 0: ducks = []

    if timer % 23 == 0: ducks.append(duckControl.Duck())