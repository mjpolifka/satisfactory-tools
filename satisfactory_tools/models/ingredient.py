from satisfactory_tools.db import db

class Ingredient(db.Model):
  __tablename__ = 'ingredient'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(36), nullable=False)
  made_in = db.Column(db.String(25), nullable=False)
  speed = db.Column(db.Integer(), nullable=False)
  quantity = db.Column(db.Integer(), nullable=False)

  def __repr__(self):
    return f'<Ingredient {self.name}>'

class Recipe(db.Model):
  __tablename__ = 'recipe'
  id = db.Column(db.Integer, primary_key=True)
  quantity = db.Column(db.Integer, nullable=False)

  ingredient_id = db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredient.id'))
  ingredient = db.relationship("Ingredient",
                               backref='component_list',
                               primaryjoin = (Ingredient.id == ingredient_id)
                              )

  component_id = db.Column('component_id', db.Integer, db.ForeignKey('ingredient.id'))
  component = db.relationship("Ingredient",
                               backref='ingredient_list',
                               primaryjoin = (Ingredient.id == component_id)
                              )
  def __repr__(self):
    return f'<Recipe [makes] {self.component} [from] {self.ingredient}>'