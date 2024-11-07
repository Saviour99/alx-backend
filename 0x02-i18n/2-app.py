#!/usr/bin/env python3
"""
Simple flask app
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.frpm_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@app.route("/")
def index() -> str:
    """Return the content of the html page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
