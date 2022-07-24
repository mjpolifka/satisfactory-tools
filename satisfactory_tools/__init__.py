from flask import Flask
from satisfactory_tools.db import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(SQLALCHEMY_DATABASE_URI=f'sqlite:///database.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False)
    
    @app.route('/hello/')
    def hello():
        return "Hello, world!"
    
    from satisfactory_tools import components
    app.register_blueprint(components.bp)

    app.add_url_rule("/", endpoint="index")
    
    return app