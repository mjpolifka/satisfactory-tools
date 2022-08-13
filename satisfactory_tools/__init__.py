from flask import Flask
from satisfactory_tools.db import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(SQLALCHEMY_DATABASE_URI=f'sqlite:///database.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False)
    
    db.init_app(app)
    
    from satisfactory_tools import components, init_db, handcraft
    app.register_blueprint(components.bp)
    app.register_blueprint(init_db.bp)
    app.register_blueprint(handcraft.bp)
    
    return app