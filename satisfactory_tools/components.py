from flask import Blueprint, render_template
from satisfactory_tools.models import Ingredient

bp = Blueprint("components", __name__)

@bp.route("/")
def index():
    components = Ingredient.query.all()
    return render_template("components/index.html", components=components)

@bp.route("/test")
def test():
    return "Test complete"