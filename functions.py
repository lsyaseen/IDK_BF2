import json

def printAll(data):
    chars = json.loads(data)
    return chars


def allchars(data):
    x = json.loads(data)

    for row in x:
        print(row['name'])

def lightSideRand(x):
    num = random.sample(range(0,9),4)
    rand1 = num[0]
    rand2 = num[1]
    rand3 = num[2]





