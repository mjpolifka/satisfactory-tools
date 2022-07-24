from flask import Blueprint, render_template

bp = Blueprint("components", __name__)

@bp.route("/")
def index():
    return render_template("components/index.html")

@bp.route("/test")
def test():
    return "Test complete"