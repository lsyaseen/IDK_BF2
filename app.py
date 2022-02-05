from flask import Flask, render_template, request, jsonify, redirect, url_for
import random
from random import randint
import json
app = Flask(__name__)

# p1 = []
# p1.extend(range(0,22))
# p2 = p1
# p3 = p2
# p4 = p3
players = []
player1LightChars = []
player2LightChars = []
player3LightChars = []
player4LightChars = []
player1DarkChars = []
player2DarkChars = []
player3DarkChars = []
player4DarkChars = []
p1RandomList = []
p2RandomList = []
p3RandomList = []
p4RandomList = []

@app.route('/')
def main():
    # read file
    with open('./files/chars.json', 'r') as f:
        data = f.read()
        chars = json.loads(data)
    # Light Side Random Numbers
    num = random.sample(range(0, 9), 4)
    rand1 = num[0]
    rand2 = num[1]
    rand3 = num[2]
    rand4 = num[3]
    c1 = [row for row in chars if(row['id'] == rand1)]
    c2 = [row for row in chars if(row['id'] == rand2)]
    c3 = [row for row in chars if(row['id'] == rand3)]
    c4 = [row for row in chars if(row['id'] == rand4)]

    # Dark Side Random Numbers
    num2 = random.sample(range(10, 21), 4)
    rand5 = num2[0]
    rand6 = num2[1]
    rand7 = num2[2]
    rand8 = num2[3]
    c5 = [row for row in chars if(row['id'] == rand5)]
    c6 = [row for row in chars if(row['id'] == rand6)]
    c7 = [row for row in chars if(row['id'] == rand7)]
    c8 = [row for row in chars if(row['id'] == rand8)]

    return render_template('index.html', player4DarkChars=player4DarkChars, player3DarkChars=player3DarkChars, player2DarkChars=player2DarkChars, player1DarkChars=player1DarkChars, player4LightChars=player4LightChars, player3LightChars=player3LightChars, player2LightChars=player2LightChars, player1LightChars=player1LightChars, players=players, chars=chars, c1=c1[0]['name'],c2=c2[0]['name'],c3=c3[0]['name'],c4=c4[0]['name'],c5=c5[0]['name'],c6=c6[0]['name'],c7=c7[0]['name'],c8=c8[0]['name'])


@app.route('/addPlayer', methods=['POST'])
def addPlayer():
    p1 = request.form['text']
    players.append(p1)
    print(players)
    return redirect('/')

@app.route('/resetPlayers', methods=['POST'])
def resetPlayers():
    players.clear()
    print(players)
    return redirect('/')

@app.route('/resetChars', methods=['POST'])
def resetChars():
    # Clear Light Side Characthers
    player1LightChars.clear()
    player2LightChars.clear()
    player3LightChars.clear()
    player4LightChars.clear()

    # Clear Dark Side Characthers
    player1DarkChars.clear()
    player2DarkChars.clear()
    player3DarkChars.clear()
    player4DarkChars.clear()

    return redirect('/')

@app.route('/shuffleLightSide', methods=['POST'])
def shuffleLightSide():
    with open('./files/chars.json', 'r') as f:
        data = f.read()
        chars = json.loads(data)

        # Light Side Random Numbers
        num = random.sample(range(0, 9), 4)
        rand1 = num[0]
        rand2 = num[1]
        rand3 = num[2]
        rand4 = num[3]
        c1 = [row for row in chars if(row['id'] == rand1)]
        c2 = [row for row in chars if(row['id'] == rand2)]
        c3 = [row for row in chars if(row['id'] == rand3)]
        c4 = [row for row in chars if(row['id'] == rand4)]

        if c1[0] in player1LightChars:
            print("Already played with this char")
        else:
            player1LightChars.append(c1[0])

        if c2[0] in player2LightChars:
            print("Already played with this char")
        else:
            player2LightChars.append(c2[0])

        if c3[0] in player3LightChars:
            print("Already played with this char")
        else:
            player3LightChars.append(c3[0])

        if c4[0] in player4LightChars:
            print("Already played with this char")
        else:
            player4LightChars.append(c4[0])

    return redirect('/')

@app.route('/shuffleDarkSide', methods=['POST'])
def shuffleDarkSide():
    with open('./files/chars.json', 'r') as f:
        data = f.read()
        chars = json.loads(data)

        # Dark Side Random Numbers
        num2 = random.sample(range(10, 21), 4)
        rand5 = num2[0]
        rand6 = num2[1]
        rand7 = num2[2]
        rand8 = num2[3]
        c5 = [row for row in chars if(row['id'] == rand5)]
        c6 = [row for row in chars if(row['id'] == rand6)]
        c7 = [row for row in chars if(row['id'] == rand7)]
        c8 = [row for row in chars if(row['id'] == rand8)]

        if c5[0] in player1DarkChars:
            print("Already played with this char")
        else:
            player1DarkChars.append(c5[0])

        if c6[0] in player2DarkChars:
            print("Already played with this char")
        else:
            player2DarkChars.append(c6[0])

        if c7[0] in player3DarkChars:
            print("Already played with this char")
        else:
            player3DarkChars.append(c7[0])

        if c8[0] in player4DarkChars:
            print("Already played with this char")
        else:
            player4DarkChars.append(c8[0])

        print(player1DarkChars)
        print(player2DarkChars)
        print(player3DarkChars)
        print(player4DarkChars)
        

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)