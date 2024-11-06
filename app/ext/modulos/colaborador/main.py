from flask import Blueprint, request, redirect, render_template, url_for
from app.ext.database import db, Colaborador

bp_colaborador = Blueprint("colaborador", __name__, template_folder="templates")

@bp_colaborador.route("/colaborador")
def index():
    colaborador = Colaborador.query.all()
    return render_template("colaborador.html", colaborador=colaborador)

@bp_colaborador.route("/colaborador/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        colaborador = Colaborador(request.form["nome"], request.form["apelido"], request.form["telefone"], request.form["lider"])
        db.session.add(colaborador)
        db.session.commit()
        colaborador = Colaborador.query.all()
        return render_template("colaborador.html", colaborador=colaborador)
    return render_template("colaboradores_create.html")

@bp_colaborador.route("/colaborador/update/<int:id>", methods=["GET", "POST"])
def update(id):
    colaborador = Colaborador.query.get(id)
    if request.method == "POST":
        colaborador.nome = request.form["nome"]
        colaborador.apelido = request.form["apelido"]
        colaborador.telefone = request.form["telefone"]
        colaborador.lider = request.form["lider"]
        db.session.commit()
        colaborador = Colaborador.query.all()
        return render_template("colaborador.html", colaborador=colaborador)
    return render_template("colaboradores_update.html", colaborador=colaborador)

@bp_colaborador.route("/colaborador/delete/<int:id>")
def delete(id):
    colaborador = Colaborador.query.get(id)
    db.session.delete(colaborador)
    db.session.commit()
    colaborador = Colaborador.query.all()
    return render_template("colaborador.html", colaborador=colaborador)