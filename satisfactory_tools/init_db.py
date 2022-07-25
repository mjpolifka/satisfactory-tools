from flask import Blueprint, render_template

from satisfactory_tools.db import db
from satisfactory_tools.models import Ingredient, Recipe

bp = Blueprint("init_db", __name__, url_prefix='/init_db')

@bp.route("/")
def init_db():
    db.drop_all()
    db.create_all()

    list = []

    # By Hand
    made_in = 'by_hand'
    # need to add leaves, wood, alien components, etc

    # Miner
    made_in = 'miner'
    iron_ore = Ingredient(name='iron ore', made_in=made_in, speed=1, quantity=1)
    copper_ore = Ingredient(name='copper ore', made_in=made_in, speed=1, quantity=1)
    limestone = Ingredient(name='limestone', made_in=made_in, speed=1, quantity=1)
    coal = Ingredient(name='coal', made_in=made_in, speed=1, quantity=1)
    list.extend([iron_ore, copper_ore, limestone, coal])

    # Smelter
    made_in = 'smelter'
    iron_ingot = Ingredient(name='iron ingot', made_in=made_in, speed=2, quantity=1)
    copper_ingot = Ingredient(name='copper ingot', made_in=made_in, speed=2, quantity=1)
    list.extend([iron_ingot, copper_ingot])

    # Foundry
    made_in = 'foundry'
    steel_ingot = Ingredient(name='steel ingot', made_in=made_in, speed=4, quantity=3)
    list.extend([steel_ingot])
    
    # Constructor
    made_in = 'contructor'
    iron_rod = Ingredient(name='iron rod', made_in=made_in, speed=4, quantity=1)
    iron_plate = Ingredient(name='iron plate', made_in=made_in, speed=6, quantity=2)
    screw = Ingredient(name='screw', made_in=made_in, speed=6, quantity=4)
    wire = Ingredient(name='wire', made_in=made_in, speed=4, quantity=2)
    cable = Ingredient(name='cable', made_in=made_in, speed=2, quantity=1)
    concrete = Ingredient(name='concrete', made_in=made_in, speed=4, quantity=1)
    copper_sheet = Ingredient(name='copper sheet', made_in=made_in, speed=6, quantity=1)
    #biomass is made from ingredients harvested by hand
    list.extend([iron_rod, iron_plate, wire, cable, concrete, copper_sheet])

    # Assembler
    made_in = 'assembler'
    reinforced_iron_plate = Ingredient(name='reinforced iron plate', made_in=made_in, speed=12, quantity=1)
    list.extend([reinforced_iron_plate])

    # Manufacturer
    made_in = 'manufacturer'
    list.extend([])



    # Smelter
    Recipe(component=iron_ingot, ingredient=iron_ore, quantity=1)
    Recipe(component=copper_ingot, ingredient=copper_ore, quantity=1)

    # Foundry
    Recipe(component=steel_ingot, ingredient=iron_ore, quantity=3)
    Recipe(component=steel_ingot, ingredient=coal, quantity=3)

    # Constructor
    Recipe(component=iron_rod, ingredient=iron_ingot, quantity=1)
    Recipe(component=iron_plate, ingredient=iron_ingot, quantity=3)
    Recipe(component=screw, ingredient=iron_rod, quantity=1)
    Recipe(component=wire, ingredient=copper_ingot, quantity=1)
    Recipe(component=cable, ingredient=wire, quantity=2)
    Recipe(component=concrete, ingredient=limestone, quantity=3)
    Recipe(component=copper_sheet, ingredient=copper_ingot, quantity=2)

    # Assembler
    Recipe(component=reinforced_iron_plate, ingredient=iron_plate, quantity=6)
    Recipe(component=reinforced_iron_plate, ingredient=screw, quantity=12)

    db.session.add_all(list)

    db.session.commit()

    return render_template('init_db.html')