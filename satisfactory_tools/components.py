import math
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
    (buildings, total_buildings) = sort_buildings(build_buildings(component, qpm, {}))
    if request.method == "POST":
        qpm = float(request.form["qpm"])
        ingredients = build_ingredients(component, qpm)
    return render_template("components/component.html",
                            component=component,
                            qpm = qpm,
                            ingredients = ingredients,
                            buildings = buildings,
                            total_buildings = total_buildings)

@bp.route("/test")
def test():
    return "Test complete"

def build_ingredients(component, qpm):
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
        # print("Already exists: " + component.name + " - " + str(qpm / ( ( 60 / component.speed ) * component.quantity )) + " (previous: " + str(existing["num_buildings"]) + ")")
    except KeyError:
        num_buildings = qpm / ( ( 60 / component.speed ) * component.quantity )
        building_list.update({component.name: {"made_in": component.made_in,"num_buildings": num_buildings}})
        # print("Did not exist: " + component.name + " - " + str(num_buildings))
    
    for ingredient in component.ingredient_list:
        ingredient_component = Ingredient.query.filter_by(id=ingredient.ingredient.id).first()
        new_qpm = (ingredient.quantity/component.quantity) * qpm
        building_list = build_buildings(ingredient_component, new_qpm, building_list)

    return building_list

def sort_buildings(building_list):
    master_dict = {}
    total_buildings = {}
    # get full list of building names
    # maybe make it manual so I can have whatever sorting I want?
    building_options = ["manufacturer", "assembler", "constructor", "foundry", "refinery", "smelter", "miner", "water extractor", "oil extractor"]
    # for loop through this list
        # if there's a match, add it to global dict
    for building in building_options:
        total_buildings.update({building: 0})
        for component in building_list:
            if building == building_list[component]["made_in"]:
                master_dict.update({component: building_list[component]})
                total_buildings.update({building: total_buildings[building] + math.ceil(building_list[component]["num_buildings"])})
    # return
    return (master_dict, total_buildings)