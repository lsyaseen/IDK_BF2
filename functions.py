import json

def printAll(data):
    chars = json.loads(data)
    return chars


def allchars(data):
    x = json.loads(data)

    for row in x:
        print(row['name'])

