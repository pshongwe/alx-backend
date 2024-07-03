#!/usr/bin/python3
"""
Flask application with Babel, forced locale
via URL parameter, and mock user login
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, format_datetime, _
import logging
import pytz

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
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """
    Retrieve user from the
    mock database based on login_as parameter.
    """
    user_id = request.args.get('login_as', '')
    if user_id:
        user = users.get(int(user_id), None)
        return user
    return None


@app.before_request
def before_request():
    """
    Executed before all requests.
    Sets g.user to the logged-in user, if any.
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """
    Determine the best match for supported languages based
    on request's accepted languages.
    Check for 'locale' parameter in
    the request and use it if valid.
    """
    qs = request.query_string.decode('utf-8').split('&')
    qt = dict(map(
                  lambda x: (x if '=' in x else '{}='.format(x)).split('='),
                  qs,
    ))
    locale = qt.get('locale', '')
    if locale in app.config['LANGUAGES']:
        return locale
    user_details = getattr(g, 'user', None)
    if user_details and user_details['locale'] in app.config["LANGUAGES"]:
        return user_details['locale']
    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """Retrieve the timezone for a web page.
    """
    timezone = request.args.get('timezone', '').strip()
    if not timezone and g.user:
        timezone = g.user['timezone']
    try:
        return pytz.timezone(timezone).zone
    except pytz.exceptions.UnknownTimeZoneError:
        return app.config['BABEL_DEFAULT_TIMEZONE']


@app.context_processor
def inject_conf_var():
    """
    Inject configuration variables into the template context.
    """
    return dict(get_locale=get_locale)


@app.route('/')
def index():
    """
    Route for the index page.
    Renders the 7-index.html template with translated messages.
    """
    app.logger.info('Index route was accessed')
    g.time = format_datetime()
    return render_template('index.html',
                           home_title=_("home_title"),
                           home_header=_("home_header"))


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    app.run(debug=True, port=5000)
