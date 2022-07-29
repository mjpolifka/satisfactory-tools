from turtle import circle, speed
from unicodedata import name
from flask import Blueprint, render_template
from satisfactory_tools.components import component_by_id

from satisfactory_tools.db import db
from satisfactory_tools.models import Ingredient, Recipe, ingredient

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
    raw_quartz = Ingredient(name='raw quartz', made_in=made_in, speed=1, quantity=1)
    sulphur = Ingredient(name='sulphur', made_in=made_in, speed=1, quantity=1)
    caterium_ore = Ingredient(name='caterium', made_in=made_in, speed=1, quantity=1)
    list.extend([iron_ore, copper_ore, limestone, coal, raw_quartz, sulphur, caterium_ore])

    # Oil Extractor
    made_in = 'oil extractor'
    crude_oil = Ingredient(name='crude oil', made_in=made_in, speed=1, quantity=2)
    list.extend([crude_oil])

    # Water Extractor
    made_in = 'water extractor'
    water = Ingredient(name='water', made_in=made_in, speed=1, quantity=2)
    list.extend([water])

    # Smelter
    made_in = 'smelter'
    iron_ingot = Ingredient(name='iron ingot', made_in=made_in, speed=2, quantity=1)
    copper_ingot = Ingredient(name='copper ingot', made_in=made_in, speed=2, quantity=1)
    caterium_ingot = Ingredient(name='caterium ingot', made_in=made_in, speed=4, quantity=1)
    list.extend([iron_ingot, copper_ingot, caterium_ingot])

    # Foundry
    made_in = 'foundry'
    steel_ingot = Ingredient(name='steel ingot', made_in=made_in, speed=4, quantity=3)
    list.extend([steel_ingot])

    # Refinery
    made_in = 'refinery'
    polymer_resin = Ingredient(name='polymer resin', made_in=made_in, speed=6, quantity=3)
    plastic = Ingredient(name='plastic', made_in=made_in, speed=6, quantity=2)
    rubber = Ingredient(name='rubber', made_in=made_in, speed=6, quantity=2)
    list.extend([polymer_resin, plastic, rubber])
    
    # Constructor
    made_in = 'constructor'
    iron_rod = Ingredient(name='iron rod', made_in=made_in, speed=4, quantity=1)
    iron_plate = Ingredient(name='iron plate', made_in=made_in, speed=6, quantity=2)
    screw = Ingredient(name='screw', made_in=made_in, speed=6, quantity=4)
    wire = Ingredient(name='wire', made_in=made_in, speed=4, quantity=2)
    cable = Ingredient(name='cable', made_in=made_in, speed=2, quantity=1)
    concrete = Ingredient(name='concrete', made_in=made_in, speed=4, quantity=1)
    copper_sheet = Ingredient(name='copper sheet', made_in=made_in, speed=6, quantity=1)
    quartz_crystal = Ingredient(name='quartz crystal', made_in=made_in, speed=8, quantity=3)
    silica = Ingredient(name='silica', made_in=made_in, speed=8, quantity=5)
    steel_beam = Ingredient(name='steel beam', made_in=made_in, speed=4, quantity=1)
    steel_pipe = Ingredient(name='steel pipe', made_in=made_in, speed=6, quantity=2)
    iron_rebar = Ingredient(name='iron rebar', made_in=made_in, speed=4, quantity=1)
    quickwire = Ingredient(name='quickwire', made_in=made_in, speed=5, quantity=5)
    #biomass is made from ingredients harvested by hand
    list.extend([iron_rod, iron_plate, wire, cable, concrete, copper_sheet, quartz_crystal, silica, steel_beam, 
                 steel_pipe, iron_rebar, quickwire])

    # Assembler
    made_in = 'assembler'
    reinforced_iron_plate = Ingredient(name='reinforced iron plate', made_in=made_in, speed=12, quantity=1)
    rotor = Ingredient(name='rotor', made_in=made_in, speed=15, quantity=1)
    modular_frame = Ingredient(name='modular frame', made_in=made_in, speed=60, quantity=2)
    smart_plating = Ingredient(name='smart plating', made_in=made_in, speed=30, quantity=1)
    versatile_framework = Ingredient(name='versatile framework', made_in=made_in, speed=24, quantity=2)
    black_powder = Ingredient(name='black powder', made_in=made_in, speed=4, quantity=2)
    encased_industrial_beam = Ingredient(name='encased industrial beam', made_in=made_in, speed=10, quantity=1)
    stator = Ingredient(name='stator', made_in=made_in, speed=12, quantity=1)
    motor = Ingredient(name='motor', made_in=made_in, speed=12, quantity=1)
    automated_wiring = Ingredient(name='automated wiring', made_in=made_in, speed=24, quantity=1)
    ai_limiter = Ingredient(name='ai limiter', made_in=made_in, speed=12, quantity=1)
    circuit_board = Ingredient(name='circuit board', made_in=made_in, speed=8, quantity=1)
    list.extend([reinforced_iron_plate, rotor, modular_frame, smart_plating, versatile_framework, black_powder, 
                 encased_industrial_beam, stator, motor, automated_wiring, ai_limiter, circuit_board])

    # Manufacturer
    made_in = 'manufacturer'
    crystal_oscillator = Ingredient(name='crystal oscillator', made_in=made_in, speed=120, quantity=2)
    heavy_modular_frame = Ingredient(name='heavy modular frame', made_in=made_in, speed=30, quantity=1)
    computer = Ingredient(name='computer', made_in=made_in, speed=24, quantity=1)
    modular_engine = Ingredient(name='modular engine', made_in=made_in, speed=60, quantity=1)
    adaptive_control_unit = Ingredient(name='adaptive control unit', made_in=made_in, speed=120, quantity=2)
    list.extend([crystal_oscillator, heavy_modular_frame, computer, modular_engine, adaptive_control_unit])



    # Smelter
    Recipe(component=iron_ingot, ingredient=iron_ore, quantity=1)
    Recipe(component=copper_ingot, ingredient=copper_ore, quantity=1)
    Recipe(component=caterium_ingot, ingredient=caterium_ore, quantity=1)

    # Foundry
    Recipe(component=steel_ingot, ingredient=iron_ore, quantity=3)
    Recipe(component=steel_ingot, ingredient=coal, quantity=3)

    # Refinery
    Recipe(component=polymer_resin, ingredient=crude_oil, quantity=6)
    Recipe(component=plastic, ingredient=polymer_resin, quantity=6)
    Recipe(component=plastic, ingredient=water, quantity=2)
    Recipe(component=rubber, ingredient=polymer_resin, quantity=4)
    Recipe(component=rubber, ingredient=water, quantity=4)

    # Constructor
    Recipe(component=iron_rod, ingredient=iron_ingot, quantity=1)
    Recipe(component=iron_plate, ingredient=iron_ingot, quantity=3)
    Recipe(component=screw, ingredient=iron_rod, quantity=1)
    Recipe(component=wire, ingredient=copper_ingot, quantity=1)
    Recipe(component=cable, ingredient=wire, quantity=2)
    Recipe(component=concrete, ingredient=limestone, quantity=3)
    Recipe(component=copper_sheet, ingredient=copper_ingot, quantity=2)
    Recipe(component=quartz_crystal, ingredient=raw_quartz, quantity=5)
    Recipe(component=silica, ingredient=raw_quartz, quantity=3)
    Recipe(component=steel_beam, ingredient=steel_ingot, quantity=4)
    Recipe(component=steel_pipe, ingredient=steel_ingot, quantity=3)
    Recipe(component=iron_rebar, ingredient=iron_rod, quantity=1)
    Recipe(component=quickwire, ingredient=caterium_ingot, quantity=1)

    # Assembler
    Recipe(component=reinforced_iron_plate, ingredient=iron_plate, quantity=6)
    Recipe(component=reinforced_iron_plate, ingredient=screw, quantity=12)
    Recipe(component=rotor, ingredient=screw, quantity=25)
    Recipe(component=rotor, ingredient=iron_rod, quantity=5)
    Recipe(component=modular_frame, ingredient=reinforced_iron_plate, quantity=3)
    Recipe(component=modular_frame, ingredient=iron_rod, quantity=12)
    Recipe(component=smart_plating, ingredient=reinforced_iron_plate, quantity=1)
    Recipe(component=smart_plating, ingredient=rotor, quantity=1)
    Recipe(component=versatile_framework, ingredient=modular_frame, quantity=1)
    Recipe(component=versatile_framework, ingredient=steel_beam, quantity=12)
    Recipe(component=black_powder, ingredient=coal, quantity=1)
    Recipe(component=black_powder, ingredient=sulphur, quantity=1)
    Recipe(component=encased_industrial_beam, ingredient=steel_beam, quantity=4)
    Recipe(component=encased_industrial_beam, ingredient=concrete, quantity=5)
    Recipe(component=stator, ingredient=steel_pipe, quantity=3)
    Recipe(component=stator, ingredient=wire, quantity=8)
    Recipe(component=motor, ingredient=rotor, quantity=2)
    Recipe(component=motor, ingredient=stator, quantity=2)
    Recipe(component=automated_wiring, ingredient=stator, quantity=1)
    Recipe(component=automated_wiring, ingredient=cable, quantity=20)
    Recipe(component=ai_limiter, ingredient=copper_sheet, quantity=5)
    Recipe(component=ai_limiter, ingredient=quickwire, quantity=20)
    Recipe(component=circuit_board, ingredient=copper_sheet, quantity=2)
    Recipe(component=circuit_board, ingredient=plastic, quantity=4)
    
    # Manufacturer
    Recipe(component=crystal_oscillator, ingredient=quartz_crystal, quantity=36)
    Recipe(component=crystal_oscillator, ingredient=cable, quantity=28)
    Recipe(component=crystal_oscillator, ingredient=reinforced_iron_plate, quantity=5)
    Recipe(component=heavy_modular_frame, ingredient=modular_frame, quantity=5)
    Recipe(component=heavy_modular_frame, ingredient=steel_pipe, quantity=15)
    Recipe(component=heavy_modular_frame, ingredient=encased_industrial_beam, quantity=5)
    Recipe(component=heavy_modular_frame, ingredient=screw, quantity=100)
    Recipe(component=computer, ingredient=circuit_board, quantity=10)
    Recipe(component=computer, ingredient=cable, quantity=9)
    Recipe(component=computer, ingredient=plastic, quantity=18)
    Recipe(component=computer, ingredient=screw, quantity=52)
    Recipe(component=modular_engine, ingredient=motor, quantity=2)
    Recipe(component=modular_engine, ingredient=rubber, quantity=15)
    Recipe(component=modular_engine, ingredient=smart_plating, quantity=2)
    Recipe(component=adaptive_control_unit, ingredient=automated_wiring, quantity=15)
    Recipe(component=adaptive_control_unit, ingredient=circuit_board, quantity=10)
    Recipe(component=adaptive_control_unit, ingredient=heavy_modular_frame, quantity=2)
    Recipe(component=adaptive_control_unit, ingredient=computer, quantity=2)

    db.session.add_all(list)

    db.session.commit()

    return render_template('init_db.html')