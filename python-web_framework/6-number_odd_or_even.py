#!/usr/bin/python3
'''
   so we install the flask pakage
'''
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text):
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return '{} is a number'.format(n)


@app.route('/5-number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    return render_template('5-number_template.html', number=n)

@app.route('/6-number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    return render_template('6-number_odd_or_even.html', number=n, parity='even' if n % 2 == 0 else 'odd')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)