from flask import Blueprint, render_template, request
from satisfactory_tools.models import Ingredient

bp = Blueprint("components", __name__)

@bp.route("/")
def index():
    # This is NOT the right way to do this
    # I need a model for Building so I can query.all() to get this list
    building_list = ['miner', 'smelter', 'constructor', 
                     'assembler', 'manufacturer']
    components = Ingredient.query.order_by(Ingredient.id).all()
    return render_template(
        "components/index.html",
        components=components,
        building_list=building_list
    )

@bp.route("/component/<id>", methods=("GET", "POST"))
def component_by_id(id):
    component = Ingredient.query.filter_by(id=id).first()
    qpm = (60 / component.speed) * component.quantity
    if request.method == "POST":
        qpm = float(request.form["qpm"])
    return render_template("components/component.html",
                            component=component,
                            qpm = qpm)

@bp.route("/test")
def test():
    return "Test complete"

# def build_ingredients(component):
#     if component.made_in not in ("by_hand, miner, oil extractor, water extractor"):
#         ingredients = component.ingredient_list
#         built_ingredients = []
#         for ingredient in ingredients:
#             quantity = ingredient.quantity
#             ingredient = Ingredient.query.filter_by(id=ingredient.ingredient.id).first()
#             built_ingredients.append({"ingredient": ingredient, "quantity": quantity})
#         print(built_ingredients)
#         return built_ingredients
#     else:
#         return 0