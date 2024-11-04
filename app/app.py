from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Float, String


from .ext.routes.dashboard import home
from .ext.routes.colaborador import bp_colaborador
from .ext.routes.material import bp_material
from .ext.routes.equipe import bp_equipe

app = Flask(__name__)

app.register_blueprint(home)
app.register_blueprint(bp_colaborador)
app.register_blueprint(bp_material)
app.register_blueprint(bp_equipe)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy()
db.init_app(app)

class Colaborador(db.Model):
    __tablename__="colaborador"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column("nome", db.String(150))
    apelido = db.Column("apelido", db.String(16))
    telefone = db.Column("telefone", db.String(16))
    lider = db.Column("lider", db.String(8))

    def __init__(self, nome, apelido, telefone, lider):
        self.nome = nome
        self.apelido = apelido
        self.telefone = telefone
        self.lider = lider

class Material(db.Model):
    __tablename__="material"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    sku = db.Column("sku", db.String(40))
    nome = db.Column("nome", db.String(150))
    valor = db.Column("custo", db.Float(5,2))

    def __init__(self, sku, nome, valor):
        self.sku = sku
        self.nome = nome
        self.valor = valor

class Equipe(db.Model):
    __tablename__="equipe"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    sku = db.Column("sku", db.String(40))
    lider = db.Column(db.String(), db.ForeignKey("colaborador.id"))
    cor = db.Column("cor", db.String(10))

    def __init__(self, sku, lider, cor):
        self.sku = sku
        self.lider = lider
        self.cor = cor

class EquipeMembros(db.Model):
    __tablename__="equipe_membros"
    id = db.Column("id", db.Integer, primary_key=True, autoincrement=True)
    equipe_id = db.Column(db.Integer, db.ForeignKey("equipe.id"))
    colaborador_id = db.Column(db.Integer, db.ForeignKey("colaborador.id"))

with app.app_context():
    db.create_all()