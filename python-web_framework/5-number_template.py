"""
A script that starts a Flask Web application and also has
an additional route/path.
"""

from flask import Flask, render_template

app = Flask(__name__)
"""
using @app.route to map "/" to the url
"""

@app.route('/', strict_slashes=False)
def hello_hbnb():
        """
        Route handler for the root URL '/'. Displays "Hello HBNB!".
        """
        return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for '/hbnb'. Displays "HBNB".
    """
    return "HBNB"
        
@app.route('/c/<text>', strict_slashes=False)
def custom_text(text):
    """
        Route handler for '/c/<text>'. Displays "C " followed by the value of the text variable.
        Replace underscore _ symbols with spaces.

        Args:
            text (str): The text variable captured from the URL.
        """
    modified_text = text.replace('_', ' ')
    return "C {}".format(modified_text)

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
            Route handler for '/python/<text>'. Displays "Python " followed by the value of the text variable.
            Replace underscore _ symbols with spaces.

            Args:
                text (str): The text variable captured from the URL.
    """
    modified_text = text.replace('_', ' ') if text else 'is cool'
    return "Python {}".format(modified_text)

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
            Route handler for '/number/<n>'. Displays "<n> is a number" if n is an integer.

            Args:
                n (int): The number captured from the URL.
    """
    return "{} is a number".format(n)

@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
            """
            Route handler for '/number_template/<n>'. Displays an HTML page with "Number: n" in an H1 tag.

            Args:
                n (int): The number captured from the URL.
            """
            return render_template('number_template.html', number=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
