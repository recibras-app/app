from flask import Flask # type: ignore
from flask import render_template, url_for, request, redirect  # type: ignore
from flask_sqlalchemy import SQLAlchemy  # type: ignore
from sqlalchemy import Integer, Float, String # type: ignore


app = Flask(__name__)
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

@app.route("/")
def dashboard():
    return render_template("index.html")

# COLABORADOR
@app.route("/colaborador")
def colaborador():
    colaborador = Colaborador.query.all()
    return render_template("colaborador.html", colaborador=colaborador)

@app.route("/create_colaborador", methods=["POST"])
def create_colaborador():
    colaborador = Colaborador(request.form["nome"], request.form["apelido"], request.form["telefone"], request.form["lider"])
    db.session.add(colaborador)
    db.session.commit()
    return redirect(url_for("colaborador"))

@app.route("/update_colaborador/<int:id>", methods=["GET", "POST"])
def update_colaborador(id):
    colaborador = Colaborador.query.get(id)
    if request.method == "POST":
        colaborador.nome = request.form["nome"]
        colaborador.apelido = request.form["apelido"]
        colaborador.telefone = request.form["telefone"]
        colaborador.lider = request.form["lider"]
        db.session.commit()
        return redirect(url_for("colaborador"))
    return render_template("update_colaborador.html", colaborador=colaborador)

@app.route("/delete_colaborador/<int:id>")
def delete_colaborador(id):
    colaborador = Colaborador.query.get(id)
    db.session.delete(colaborador)
    db.session.commit()
    return redirect(url_for("colaborador"))


# MATERIAL
@app.route("/material")
def material():
    material = Material.query.all()
    return render_template("material.html", material=material)

@app.route("/create_material", methods=["POST"])
def create_material():
    material = Material(request.form["sku"], request.form["nome"], request.form["valor"])
    db.session.add(material)
    db.session.commit()
    return redirect(url_for("material"))

@app.route("/update_material/<int:id>", methods=["GET", "POST"])
def update_material(id):
    material = Material.query.get(id)
    if request.method == "POST":
        material.sku = request.form["sku"]
        material.nome = request.form["nome"]
        material.valor = request.form["valor"]
        db.session.commit()
        return redirect(url_for("material"))
    return render_template("update_material.html", material=material)

@app.route("/delete_material/<int:id>")
def delete_material(id):
    material = Material.query.get(id)
    db.session.delete(material)
    db.session.commit()
    return redirect(url_for("material"))

# EQUIPE
@app.route("/equipe")
def equipe():
    equipe = Equipe.query.all()
    return render_template("equipe.html", equipe=equipe)

@app.route("/create_equipe", methods=["POST"])
def create_equipe():
    equipe = Equipe(request.form["sku"], request.form["lider"], request.form["cor"])
    db.session.add(equipe)
    db.session.commit()
    return redirect(url_for("equipe"))

@app.route("/details_equipe/<int:id>")
def details_equipe(id):
    equipe = Equipe.query.get(id)
    return render_template("details_equipe.html", equipe=equipe)

@app.route("/update_equipe/<int:id>", methods=["GET", "POST"])
def update_equipe(id):
    equipe = Equipe.query.get(id)
    if request.method == "POST":
        equipe.sku = request.form["sku"]
        equipe.lider = request.form["lider"]
        equipe.cor = request.form["cor"]
        db.session.commit()
        return redirect(url_for("equipe"))
    return render_template("update_equipe.html", equipe=equipe)

@app.route("/delete_equipe/<int:id>")
def delete_equipe(id):
    equipe = Equipe.query.get(id)
    db.session.delete(equipe)
    db.session.commit()
    return redirect(url_for("equipe"))