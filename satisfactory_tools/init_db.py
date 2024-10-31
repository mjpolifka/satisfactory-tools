# from turtle import circle, speed
# from unicodedata import name
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
    sulfur = Ingredient(name='sulfur', made_in=made_in, speed=1, quantity=1)
    caterium_ore = Ingredient(name='caterium', made_in=made_in, speed=1, quantity=1)
    bauxite = Ingredient(name='bauxite', made_in=made_in, speed=1, quantity=1)
    uranium = Ingredient(name='uranium', made_in=made_in, speed=1, quantity=1)
    uranium_waste = Ingredient(name='uranium waste', made_in=made_in, speed=60, quantity=10)
    list.extend([iron_ore, copper_ore, limestone, coal, raw_quartz, sulfur, caterium_ore,
                 bauxite, uranium, uranium_waste])

    # Oil Extractor
    made_in = 'oil extractor'
    crude_oil = Ingredient(name='crude oil', made_in=made_in, speed=1, quantity=2)
    list.extend([crude_oil])

    # Water Extractor
    made_in = 'water extractor'
    water = Ingredient(name='water', made_in=made_in, speed=1, quantity=2)
    list.extend([water])

    # Resource Well Extractor
    made_in = 'resource well extractor'
    nitrogen_gas = Ingredient(name='nitrogen gas', made_in=made_in, speed=1, quantity=1)
    list.extend([nitrogen_gas])

    # Smelter
    made_in = 'smelter'
    iron_ingot = Ingredient(name='iron ingot', made_in=made_in, speed=2, quantity=1)
    copper_ingot = Ingredient(name='copper ingot', made_in=made_in, speed=2, quantity=1)
    caterium_ingot = Ingredient(name='caterium ingot', made_in=made_in, speed=4, quantity=1)
    list.extend([iron_ingot, copper_ingot, caterium_ingot])

    # Foundry
    made_in = 'foundry'
    steel_ingot = Ingredient(name='steel ingot', made_in=made_in, speed=4, quantity=3)
    aluminum_ingot = Ingredient(name='aluminum ingot', made_in=made_in, speed=4, quantity=4)
    list.extend([steel_ingot, aluminum_ingot])

    # Refinery
    made_in = 'refinery'
    polymer_resin = Ingredient(name='polymer resin', made_in=made_in, speed=6, quantity=3)
    plastic = Ingredient(name='plastic', made_in=made_in, speed=6, quantity=2)
    rubber = Ingredient(name='rubber', made_in=made_in, speed=6, quantity=2)
    alumina_solution = Ingredient(name='alumina solution', made_in=made_in, speed=6, quantity=12)
    aluminum_scrap = Ingredient(name='aluminum scrap', made_in=made_in, speed=1, quantity=6)
    sulfuric_acid = Ingredient(name='sulfuric acid', made_in=made_in, speed=6, quantity=5)
    fabric = Ingredient(name='fabric', made_in=made_in, speed=2, quantity=1)
    list.extend([polymer_resin, plastic, rubber, alumina_solution, aluminum_scrap, sulfuric_acid, fabric])
    
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
    aluminum_casing = Ingredient(name='aluminum casing', made_in=made_in, speed=2, quantity=2)
    empty_canister = Ingredient(name='empty canister', made_in=made_in, speed=4, quantity=4)
    copper_powder = Ingredient(name='copper powder', made_in=made_in, speed=6, quantity=5)
    list.extend([iron_rod, iron_plate, wire, cable, concrete, copper_sheet, quartz_crystal, silica, steel_beam, 
                 steel_pipe, iron_rebar, quickwire, aluminum_casing, empty_canister, copper_powder])
    
    #biomass is made from ingredients harvested by hand
        #so what?  Works fine for the miner; just give it a fake time and remember it needs to be fixed
        #it also has 3 different recipes and I'm not sure how to do that yet


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
    alclad_aluminum_sheet = Ingredient(name='alclad aluminum sheet', made_in=made_in, speed=6, quantity=3)
    assembly_director_system = Ingredient(name='assembly director system', made_in=made_in, speed=80, quantity=1)
    heat_sink = Ingredient(name='heat sink', made_in=made_in, speed=8, quantity=1)
    electromagnetic_control_rod = Ingredient(name='electromagnetic control rod', made_in=made_in, speed=30, quantity=2)
    compacted_coal = Ingredient(name='compacted coal', made_in=made_in, speed=12, quantity=5)
    encased_plutonium_cell = Ingredient(name='encased plutonium cell', made_in=made_in, speed=12, quantity=1)
    pressure_conversion_cube = Ingredient(name='pressure conversion cube', made_in=made_in, speed=60, quantity=1)
    list.extend([reinforced_iron_plate, rotor, modular_frame, smart_plating, versatile_framework, black_powder, 
                 encased_industrial_beam, stator, motor, automated_wiring, ai_limiter, circuit_board,
                 alclad_aluminum_sheet, assembly_director_system, heat_sink, electromagnetic_control_rod,
                 compacted_coal, encased_plutonium_cell, pressure_conversion_cube])

    # Manufacturer
    made_in = 'manufacturer'
    crystal_oscillator = Ingredient(name='crystal oscillator', made_in=made_in, speed=120, quantity=2)
    heavy_modular_frame = Ingredient(name='heavy modular frame', made_in=made_in, speed=30, quantity=1)
    computer = Ingredient(name='computer', made_in=made_in, speed=24, quantity=1)
    modular_engine = Ingredient(name='modular engine', made_in=made_in, speed=60, quantity=1)
    adaptive_control_unit = Ingredient(name='adaptive control unit', made_in=made_in, speed=120, quantity=2)
    high_speed_connector = Ingredient(name='high speed connector', made_in=made_in, speed=16, quantity=1)
    supercomputer = Ingredient(name='supercomputer', made_in=made_in, speed=32, quantity=1)
    radio_control_unit = Ingredient(name='radio control unit', made_in=made_in, speed=48, quantity=2)
    classic_battery = Ingredient(name='classic battery (alt)', made_in=made_in, speed=8, quantity=4)
    gas_filter = Ingredient(name='gas filter', made_in=made_in, speed=8, quantity=1)
    iodine_infused_filter = Ingredient(name='iodine infused filter', made_in=made_in, speed=16, quantity=1)
    uranium_fuel_rod = Ingredient(name='uranium fuel rod', made_in=made_in, speed=150, quantity=1)
    magnetic_field_generator = Ingredient(name='magnetic field generator', made_in=made_in, speed=120, quantity=2)
    turbo_motor = Ingredient(name='turbo motor', made_in=made_in, speed=32, quantity=1)
    thermal_propulsion_rocket = Ingredient(name='thermal propulsion rocket', made_in=made_in, speed=120, quantity=2)
    plutonium_fuel_rod = Ingredient(name='plutonium fuel rod', made_in=made_in, speed=240, quantity=1)
    list.extend([crystal_oscillator, heavy_modular_frame, computer, modular_engine, adaptive_control_unit, 
                 high_speed_connector, supercomputer, radio_control_unit, classic_battery, gas_filter,
                 iodine_infused_filter, uranium_fuel_rod, magnetic_field_generator, turbo_motor,
                 thermal_propulsion_rocket, plutonium_fuel_rod])

    # Blender
    made_in = 'blender'
    battery = Ingredient(name='battery', made_in=made_in, speed=3, quantity=1)
    cooling_system = Ingredient(name='cooling system', made_in=made_in, speed=10, quantity=1)
    fused_modular_frame = Ingredient(name='fused modular frame', made_in=made_in, speed=40, quantity=1)
    encased_uranium_cell = Ingredient(name='encased uranium cell', made_in=made_in, speed=12, quantity=5) #byproduct: 2 sulfuric acid
    nitric_acid = Ingredient(name='nitric acid', made_in=made_in, speed=6, quantity=3)
    non_fissile_uranium = Ingredient(name='non-fissile uranium', made_in=made_in, speed=24, quantity=20) #byproduct: 6 water
    list.extend([battery, cooling_system, fused_modular_frame, encased_uranium_cell, nitric_acid, non_fissile_uranium])


    # Particle Accelerator
    made_in = 'particle_accelerator'
    plutonium_pellet = Ingredient(name='plutonium pellet', made_in=made_in, speed=60, quantity=30)
    nuclear_pasta = Ingredient(name='nuclear pasta', made_in=made_in, speed=120, quantity=1)
    list.extend([plutonium_pellet, nuclear_pasta])



#############   Recipes   #############


    # Smelter
    Recipe(component=iron_ingot, ingredient=iron_ore, quantity=1)
    Recipe(component=copper_ingot, ingredient=copper_ore, quantity=1)
    Recipe(component=caterium_ingot, ingredient=caterium_ore, quantity=3)

    # Foundry
    Recipe(component=steel_ingot, ingredient=iron_ore, quantity=3)
    Recipe(component=steel_ingot, ingredient=coal, quantity=3)
    Recipe(component=aluminum_ingot, ingredient=aluminum_scrap, quantity=6)
    Recipe(component=aluminum_ingot, ingredient=silica, quantity=5)

    # Refinery
    Recipe(component=polymer_resin, ingredient=crude_oil, quantity=6)
    Recipe(component=plastic, ingredient=polymer_resin, quantity=6)
    Recipe(component=plastic, ingredient=water, quantity=2)
    Recipe(component=rubber, ingredient=polymer_resin, quantity=4)
    Recipe(component=rubber, ingredient=water, quantity=4)
    Recipe(component=alumina_solution, ingredient=bauxite, quantity=12)
    Recipe(component=alumina_solution, ingredient=water, quantity=18)
    Recipe(component=aluminum_scrap, ingredient=alumina_solution, quantity=4)
    Recipe(component=aluminum_scrap, ingredient=coal, quantity=2)
    Recipe(component=sulfuric_acid, ingredient=sulfur, quantity=5)
    Recipe(component=sulfuric_acid, ingredient=water, quantity=5)
    Recipe(component=fabric, ingredient=polymer_resin, quantity=1)
    Recipe(component=fabric, ingredient=water, quantity=1)

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
    Recipe(component=aluminum_casing, ingredient=aluminum_ingot, quantity=3)
    Recipe(component=empty_canister, ingredient=plastic, quantity=2)
    Recipe(component=copper_powder, ingredient=copper_ingot, quantity=30)

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
    Recipe(component=black_powder, ingredient=sulfur, quantity=1)
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
    Recipe(component=alclad_aluminum_sheet, ingredient=aluminum_ingot, quantity=3)
    Recipe(component=alclad_aluminum_sheet, ingredient=copper_ingot, quantity=1)
    Recipe(component=assembly_director_system, ingredient=adaptive_control_unit, quantity=2)
    Recipe(component=assembly_director_system, ingredient=supercomputer, quantity=1)
    Recipe(component=heat_sink, ingredient=alclad_aluminum_sheet, quantity=5)
    Recipe(component=heat_sink, ingredient=copper_sheet, quantity=3)
    Recipe(component=electromagnetic_control_rod, ingredient=stator, quantity=3)
    Recipe(component=electromagnetic_control_rod, ingredient=ai_limiter, quantity=4)
    Recipe(component=compacted_coal, ingredient=coal, quantity=5)
    Recipe(component=compacted_coal, ingredient=sulfur, quantity=5)
    Recipe(component=encased_plutonium_cell, ingredient=plutonium_pellet, quantity=2)
    Recipe(component=encased_plutonium_cell, ingredient=concrete, quantity=4)
    Recipe(component=pressure_conversion_cube, ingredient=fused_modular_frame, quantity=1)
    Recipe(component=pressure_conversion_cube, ingredient=radio_control_unit, quantity=2)

    # Manufacturer
    Recipe(component=crystal_oscillator, ingredient=quartz_crystal, quantity=36)
    Recipe(component=crystal_oscillator, ingredient=cable, quantity=28)
    Recipe(component=crystal_oscillator, ingredient=reinforced_iron_plate, quantity=5)
    Recipe(component=heavy_modular_frame, ingredient=modular_frame, quantity=5)
    Recipe(component=heavy_modular_frame, ingredient=steel_pipe, quantity=20)
    Recipe(component=heavy_modular_frame, ingredient=encased_industrial_beam, quantity=5)
    Recipe(component=heavy_modular_frame, ingredient=screw, quantity=120)
    Recipe(component=computer, ingredient=circuit_board, quantity=4)
    Recipe(component=computer, ingredient=cable, quantity=8)
    Recipe(component=computer, ingredient=plastic, quantity=16)
    Recipe(component=modular_engine, ingredient=motor, quantity=2)
    Recipe(component=modular_engine, ingredient=rubber, quantity=15)
    Recipe(component=modular_engine, ingredient=smart_plating, quantity=2)
    Recipe(component=adaptive_control_unit, ingredient=automated_wiring, quantity=15)
    Recipe(component=adaptive_control_unit, ingredient=circuit_board, quantity=10)
    Recipe(component=adaptive_control_unit, ingredient=heavy_modular_frame, quantity=2)
    Recipe(component=adaptive_control_unit, ingredient=computer, quantity=2)
    Recipe(component=high_speed_connector, ingredient=quickwire, quantity=56)
    Recipe(component=high_speed_connector, ingredient=cable, quantity=10)
    Recipe(component=high_speed_connector, ingredient=circuit_board, quantity=1)
    Recipe(component=supercomputer, ingredient=computer, quantity=2)
    Recipe(component=supercomputer, ingredient=ai_limiter, quantity=2)
    Recipe(component=supercomputer, ingredient=high_speed_connector, quantity=3)
    Recipe(component=supercomputer, ingredient=plastic, quantity=28)
    Recipe(component=radio_control_unit, ingredient=aluminum_casing, quantity=32)
    Recipe(component=radio_control_unit, ingredient=crystal_oscillator, quantity=1)
    Recipe(component=radio_control_unit, ingredient=computer, quantity=1)
    Recipe(component=classic_battery, ingredient=sulfur, quantity=6)
    Recipe(component=classic_battery, ingredient=alclad_aluminum_sheet, quantity=7)
    Recipe(component=classic_battery, ingredient=plastic, quantity=8)
    Recipe(component=classic_battery, ingredient=wire, quantity=12)
    Recipe(component=gas_filter, ingredient=coal, quantity=5)
    Recipe(component=gas_filter, ingredient=rubber, quantity=2)
    Recipe(component=gas_filter, ingredient=fabric, quantity=2)
    Recipe(component=iodine_infused_filter, ingredient=gas_filter, quantity=1)
    Recipe(component=iodine_infused_filter, ingredient=quickwire, quantity=8)
    Recipe(component=iodine_infused_filter, ingredient=aluminum_casing, quantity=1)
    Recipe(component=uranium_fuel_rod, ingredient=encased_uranium_cell, quantity=50)
    Recipe(component=uranium_fuel_rod, ingredient=encased_industrial_beam, quantity=3)
    Recipe(component=uranium_fuel_rod, ingredient=electromagnetic_control_rod, quantity=5)
    Recipe(component=magnetic_field_generator, ingredient=versatile_framework, quantity=5)
    Recipe(component=magnetic_field_generator, ingredient=electromagnetic_control_rod, quantity=2)
    Recipe(component=magnetic_field_generator, ingredient=battery, quantity=10)
    Recipe(component=turbo_motor, ingredient=cooling_system, quantity=4)
    Recipe(component=turbo_motor, ingredient=radio_control_unit, quantity=2)
    Recipe(component=turbo_motor, ingredient=motor, quantity=4)
    Recipe(component=turbo_motor, ingredient=rubber, quantity=24)
    Recipe(component=thermal_propulsion_rocket, ingredient=modular_engine, quantity=5)
    Recipe(component=thermal_propulsion_rocket, ingredient=turbo_motor, quantity=2)
    Recipe(component=thermal_propulsion_rocket, ingredient=cooling_system, quantity=6)
    Recipe(component=thermal_propulsion_rocket, ingredient=fused_modular_frame, quantity=2)
    Recipe(component=plutonium_fuel_rod, ingredient=encased_plutonium_cell, quantity=30)
    Recipe(component=plutonium_fuel_rod, ingredient=steel_beam, quantity=18)
    Recipe(component=plutonium_fuel_rod, ingredient=electromagnetic_control_rod, quantity=6)
    Recipe(component=plutonium_fuel_rod, ingredient=heat_sink, quantity=10)

    # Blender
    Recipe(component=battery, ingredient=sulfuric_acid, quantity=2.5)
    Recipe(component=battery, ingredient=alumina_solution, quantity=2)
    Recipe(component=battery, ingredient=aluminum_casing, quantity=1)
    Recipe(component=cooling_system, ingredient=heat_sink, quantity=2)
    Recipe(component=cooling_system, ingredient=rubber, quantity=2)
    Recipe(component=cooling_system, ingredient=water, quantity=5)
    Recipe(component=cooling_system, ingredient=nitrogen_gas, quantity=25)
    Recipe(component=fused_modular_frame, ingredient=heavy_modular_frame, quantity=1)
    Recipe(component=fused_modular_frame, ingredient=aluminum_casing, quantity=50)
    Recipe(component=fused_modular_frame, ingredient=nitrogen_gas, quantity=25)
    Recipe(component=encased_uranium_cell, ingredient=uranium, quantity=10)
    Recipe(component=encased_uranium_cell, ingredient=concrete, quantity=3)
    Recipe(component=encased_uranium_cell, ingredient=sulfuric_acid, quantity=8)
    Recipe(component=nitric_acid, ingredient=nitrogen_gas, quantity=12)
    Recipe(component=nitric_acid, ingredient=water, quantity=3)
    Recipe(component=nitric_acid, ingredient=iron_plate, quantity=1)
    Recipe(component=non_fissile_uranium, ingredient=uranium_waste, quantity=15)
    Recipe(component=non_fissile_uranium, ingredient=silica, quantity=10)
    Recipe(component=non_fissile_uranium, ingredient=nitric_acid, quantity=60)
    Recipe(component=non_fissile_uranium, ingredient=sulfuric_acid, quantity=60)


    # Particle Accelerator
    Recipe(component=plutonium_pellet, ingredient=non_fissile_uranium, quantity=100)
    Recipe(component=plutonium_pellet, ingredient=uranium_waste, quantity=25)
    Recipe(component=nuclear_pasta, ingredient=copper_powder, quantity=200)
    Recipe(component=nuclear_pasta, ingredient=pressure_conversion_cube, quantity=1)


    db.session.add_all(list)
    db.session.commit()
    return render_template('init_db.html')