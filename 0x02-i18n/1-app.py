#!/usr/bin/python3
"""
Basic Flask application with Babel integration
"""
from flask import Flask, render_template
from flask_babel import Babel
import logging


app = Flask(__name__)

class Config:
    """Config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """index"""
    app.logger.info('Index route was accessed')
    return render_template('1-index.html')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True, port=5000)
