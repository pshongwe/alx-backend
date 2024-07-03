#!/usr/bin/python3
"""
Flask application with Babel
and forced locale via URL parameter
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _
import logging

app = Flask(__name__)


class Config:
    """
    Configuration class for Flask app.
    Defines supported languages, default locale,
    and default timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the best match for
    supported languages based on
    request's accepted languages.
    Check for 'locale' parameter
    in the request and use it if valid.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    a = request.accept_languages
    return a.best_match(app.config['LANGUAGES'])


@app.context_processor
def inject_conf_var():
    """
    Inject configuration
    variables into the template context.
    """
    return dict(get_locale=get_locale)


@app.route('/')
def index():
    """
    Route for the index page.
    Renders the 4-index.html
    template with translated messages.
    """
    app.logger.info('Index route was accessed')
    return render_template('4-index.html',
                           home_title=_("home_title"),
                           home_header=_("home_header"))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True, port=5000)
