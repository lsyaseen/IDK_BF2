from flask import Flask, render_template
from random import randint
import json
app = Flask(__name__)


@app.route('/')
def main():
    # read file
    with open('./files/chars.json', 'r') as f:
        data = f.read()
        chars = json.loads(data)
    # Light Side Random Numbers
    rand1 = randint(0,9)
    rand2 = randint(0,9)
    rand3 = randint(0,9)
    rand4 = randint(0,9)
    c1 = [row for row in chars if(row['id'] == rand1)]
    c2 = [row for row in chars if(row['id'] == rand2)]
    c3 = [row for row in chars if(row['id'] == rand3)]
    c4 = [row for row in chars if(row['id'] == rand4)]

    # Light Side Random Numbers
    rand5 = randint(11,21)
    rand6 = randint(11,21)
    rand7 = randint(11,21)
    rand8 = randint(11,21)
    c5 = [row for row in chars if(row['id'] == rand5)]
    c6 = [row for row in chars if(row['id'] == rand6)]
    c7 = [row for row in chars if(row['id'] == rand7)]
    c8 = [row for row in chars if(row['id'] == rand8)]

    return render_template('index.html', chars=chars, c1=c1[0]['name'],c2=c2[0]['name'],c3=c3[0]['name'],c4=c4[0]['name'],c5=c5[0]['name'],c6=c6[0]['name'],c7=c7[0]['name'],c8=c8[0]['name'])

if __name__ == '__main__':
    app.run(debug=True)