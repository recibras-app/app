from flask import Flask 

from .ext import database
from .ext import toolbar
from .ext import dashboard

from .ext.modulos import colaborador, equipe, material

def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "recibrasapp@"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
    app.config["DEBUG_TB_TEMPLATE_EDITOR_ENABLED"] = True

    database.init_app(app)
    toolbar.init_app(app)
    dashboard.init_app(app)
    colaborador.init_app(app)
    equipe.init_app(app)
    material.init_app(app)

    with app.app_context():
        database.db.create_all()
    
    return app