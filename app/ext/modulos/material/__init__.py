from .main import bp_material
def init_app(app):
    app.register_blueprint(bp_material)