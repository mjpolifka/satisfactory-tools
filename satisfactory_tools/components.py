from flask import Blueprint, render_template, request
from satisfactory_tools.models import Ingredient

bp = Blueprint("components", __name__)

@bp.route("/")
def index():
    # create a list of all possible buildings to create headings
    building_list = []
    all_components = Ingredient.query.all()
    for component in all_components:
        if component.made_in not in building_list:
            building_list.append(component.made_in)

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
    buildings = build_buildings(component, qpm, {})
    if request.method == "POST":
        qpm = float(request.form["qpm"])
        ingredients = build_ingredients(component, qpm)
    return render_template("components/component.html",
                            component=component,
                            qpm = qpm,
                            ingredients = ingredients,
                            buildings = buildings)

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

def build_buildings(component, qpm, building_list):
    try:
        existing = building_list[component.name]
        num_buildings = existing["num_buildings"] + qpm / ( ( 60 / component.speed ) * component.quantity )
        building_list.update({component.name: {"made_in": component.made_in, "num_buildings": num_buildings}})
        print("Already exists: " + component.name + " - " + str(qpm / ( ( 60 / component.speed ) * component.quantity )) + " (previous: " + str(existing["num_buildings"]) + ")")
    except KeyError:
        num_buildings = qpm / ( ( 60 / component.speed ) * component.quantity )
        building_list.update({component.name: {"made_in": component.made_in,"num_buildings": num_buildings}})
        print("Did not exist: " + component.name + " - " + str(num_buildings))
    
    for ingredient in component.ingredient_list:
        ingredient_component = Ingredient.query.filter_by(id=ingredient.ingredient.id).first()
        new_qpm = (ingredient.quantity/component.quantity) * qpm
        building_list = build_buildings(ingredient_component, new_qpm, building_list)

    return building_list