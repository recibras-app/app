from flask import Flask

from .ext.dashboard.main import index
from .ext.modulos.colaborador.main import bp_colaborador
from .ext.modulos.equipe.main import bp_equipe
from .ext.modulos.material.main import bp_material

def create_app():
    app = Flask(__name__)

    app.register_blueprint(index)
    app.register_blueprint(bp_colaborador)
    app.register_blueprint(bp_equipe)
    app.register_blueprint(bp_material)
    
    return app