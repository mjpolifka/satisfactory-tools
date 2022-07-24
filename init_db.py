from satisfactory_tools.db import db
from satisfactory_tools.models import Ingredient, Recipe

db.drop_all()
db.create_all()


iron_ore = Ingredient(name='iron ore', made_in='miner', speed=60, quantity=60)
iron_ingot = Ingredient(name='iron ingot', made_in='smelter', speed=30, quantity=15)
iron_rod = Ingredient(name='iron rod', made_in='constructor', speed=30, quantity=15)
iron_plate = Ingredient(name='iron plate', made_in='constructor', speed=30, quantity=30)
screw = Ingredient(name='screw', made_in='constructor', speed=30, quantity=20)
reinforced_iron_plate = Ingredient(name='reinforced iron plate', made_in='assembler', speed=60, quantity=5)

Recipe(component=iron_ingot, ingredient=iron_ore, quantity=1)
Recipe(component=iron_rod, ingredient=iron_ingot, quantity=1)
Recipe(component=iron_plate, ingredient=iron_ingot, quantity=3)
Recipe(component=screw, ingredient=iron_rod, quantity=1)
Recipe(component=reinforced_iron_plate, ingredient=iron_plate, quantity=1)
Recipe(component=reinforced_iron_plate, ingredient=screw, quantity=1)


db.session.add_all([iron_ore, iron_ingot, iron_rod, iron_plate, screw, reinforced_iron_plate])

db.session.commit()