from .main import index

def init_app(app):
    app.register_blueprint(index)