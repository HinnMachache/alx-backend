#!/usr/bin/env python3
"""
A flask app file to demo Babel capabilities
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class containing default locale, languages and UTC
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/', strict_slashes=False)
def home():
    """ Home page"""
    return render_template('1-index.html')


if (__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0', port=5000)
