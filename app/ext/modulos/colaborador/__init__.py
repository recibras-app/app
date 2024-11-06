from .main import bp_colaborador

def init_app(app):
    app.register_blueprint(bp_colaborador)