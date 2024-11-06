from .main import bp_equipe
def init_app(app):
    app.register_blueprint(bp_equipe)