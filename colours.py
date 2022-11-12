BLUE = [0, 0, 150]
GREEN = [0, 150, 0]
RED = [150, 0, 0]
CYAN = [0, 150, 150]
PURPLE = [150, 0, 150]
YELLOW = [150, 150, 0]

'''
colours = [
    [BLUE, 1],
    [GREEN, 2],
    [RED, 3],
    [CYAN, 4],
    [PURPLE, 5],
    [YELLOW, 6]
]'''

colours = {
    "blue" : [BLUE, 1],
    "green" : [GREEN, 2],
    "red" : [RED, 3],
    "cyan" : [CYAN, 4],
    "purple" : [PURPLE, 5],
    "yellow" : [YELLOW, 6]
}

def colourType(colour): return colours[colour][0]

def colourPoints(colour): return colours[colour][1]