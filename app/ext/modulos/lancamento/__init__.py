from .main import bp_lancamentopeso
def init_app(app):
    app.register_blueprint(bp_lancamentopeso)