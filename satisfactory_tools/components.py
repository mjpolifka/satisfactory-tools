from flask import Blueprint, render_template
from satisfactory_tools.models import Ingredient

bp = Blueprint("components", __name__)

@bp.route("/")
def index():
    # This is NOT the right way to do this
    # I need a model for Building so I can query.all() to get this list
    building_list = ['miner', 'smelter', 'constructor', 'assembler', 'manufacturer']
    components = Ingredient.query.order_by(Ingredient.id).all()
    return render_template(
        "components/index.html",
        components=components,
        building_list=building_list
    )

@bp.route("/component/<id>")
def component_by_id(id):
    component = Ingredient.query.filter_by(id=id).first()
    return render_template("components/component.html", component=component)

@bp.route("/test")
def test():
    return "Test complete"