#!/usr/bin/env python3
"""
Simple flask page
"""

from flask import Flask, render_template
from typing import Final


app: Final[Flask] = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index() -> str:
    """Return the content of the html page"""
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
