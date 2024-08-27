#!/usr/bin/env python3
"""
A flask app file to demo Babel capabilities
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """ Home page"""
    return render_template('0-index.html')


if (__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0', port=5000)
