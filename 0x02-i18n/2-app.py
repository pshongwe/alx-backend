#!/usr/bin/python3
"""
Flask application with Babel and locale selection
"""
from flask import Flask, render_template, request
from flask_babel import Babel
import logging

app = Flask(__name__)


class Config:
    """
    Configuration class for Flask app.
    Defines supported languages,
    default locale, and default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages
    based on request's accepted languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Route for the index page.
    Renders the 2-index.html template.
    """
    app.logger.info('Index route was accessed')
    return render_template('2-index.html')


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True)
