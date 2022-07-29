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
    ingredients = build_ingredients(component, qpm)
    if request.method == "POST":
        qpm = float(request.form["qpm"])
        ingredients = build_ingredients(component, qpm)
    return render_template("components/component.html",
                            component=component,
                            qpm = qpm,
                            ingredients = ingredients)

@bp.route("/test")
def test():
    return "Test complete"

def build_ingredients(component, qpm):
    # To get a full list of components and buildings, I'll have to keep track of it separately
    # I can do build_ingredients(component, qpm, first=False): 
    # Then if(first): (~~create empty tracking_dict~~)
    # And if(first): (return (built_ingredients, tracking_dict)) else: (return built_ingredients)
    # Each time I parse an ingredient and calculate a qpm, do 
    #   tracking_dict.update({ingredient: tracking_dict.ingredient + quantity, building: tracking_dict.building + ~~calculate percent of building~~})
    # Send tracking_dict in render_template() and render it in the template

    # Or, above I can create empty_tracking_dict = {~~etc~~}
    # build_ingredients(component, qpm, tracking_dict)
    # And call build_ingredients(component, qpm, empty_tracking_dict) above
    # Below, call build_ingredients(component, qpm, tracking_dict)
    # 
    # I still need to calculate percent_of_building as I go
    
    if component.made_in not in ("by_hand, miner, oil extractor, water extractor"):
        ingredients = component.ingredient_list
        built_ingredients = {}
        
        for ingredient in ingredients:
            quantity = ingredient.quantity
            ingredient = Ingredient.query.filter_by(id=ingredient.ingredient.id).first()
            new_qpm = (quantity/component.quantity) * qpm

            ingredient_dict = {"ingredient": ingredient, "quantity": quantity, "qpm": new_qpm}
            
            ingredients = build_ingredients(ingredient, new_qpm)
            
            if ingredients != 0:
                ingredient_dict.update({"ingredients": ingredients})

            built_ingredients.update({ingredient.name: ingredient_dict})
        
        return built_ingredients
    else:
        return 0