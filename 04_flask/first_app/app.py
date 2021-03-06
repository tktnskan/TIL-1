import random
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hi!'

@app.route('/pick_lotto')
def pick_lotto():
    numbers = random.sample(range(1, 46), 6)
    return jsonify(numbers)

@app.route('/hi/<string:name>')
def hi(name):
    return(f'hi {name}!')

if __name__ == '__main__':
    app.run(debug=True)