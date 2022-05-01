from flask import Blueprint, render_template

home_bp = Blueprint("home_view", __name__)


@home_bp.route("/")
def index():
    return render_template('index.html')
