from flask import Blueprint, request, redirect, render_template, url_for
from app.ext.database import db, Equipe, EquipeMembros, Colaborador


bp_equipe = Blueprint("equipe", __name__, template_folder="templates")

@bp_equipe.route("/equipe")
def index():
    equipe = Equipe.query.all()
    return render_template("equipe.html", equipe=equipe)

@bp_equipe.route("/equipe/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        equipe = Equipe(request.form["sku"], request.form["colaborador_id"], request.form["cor"])
        db.session.add(equipe)
        db.session.commit()
        equipe = Equipe.query.all()
        return render_template("equipe.html", equipe=equipe)
    lider = Colaborador.query.filter_by(lider="SIM")
    return render_template("equipe_create.html", lider=lider)

@bp_equipe.route("/equipe/detalhes/<int:id>")
def details(id):
    equipe = Equipe.query.get(id)
    membros = EquipeMembros.query.filter_by(equipe_id=id)
    return render_template("equipe_detalhes.html", equipe=equipe, membros=membros)     

@bp_equipe.route("/equipe/update/<int:id>", methods=["GET", "POST"])
def update(id):
    equipe = Equipe.query.get(id)
    if request.method == "POST":
        equipe.sku = request.form["sku"]
        equipe.colaborador_id = request.form["colaborador_id"]
        equipe.cor = request.form["cor"]
        db.session.commit()
        equipe = Equipe.query.all()
        return render_template("equipe.html", equipe=equipe)
    return render_template("equipe_update.html", equipe=equipe)

@bp_equipe.route("/equipe/delete/<int:id>")
def delete(id):
    equipe = Equipe.query.get(id)
    db.session.delete(equipe)
    db.session.commit()
    equipe = Equipe.query.all()
    return render_template("equipe.html", equipe=equipe)


@bp_equipe.route("/equipe/<int:id>/add", methods=["GET", "POST"])
def add_member(id):
    if request.method == "POST":
        add_member = EquipeMembros(id, request.form["colaborador_id"])
        db.session.add(add_member)
        db.session.commit()
        equipe = Equipe.query.get(id)
        return render_template("equipe_detalhes.html", equipe=equipe)
    equipe = Equipe.query.get(id)
    membro = Colaborador.query.filter_by(lider="NAO")
    return render_template("add_membro.html", equipe=equipe, membro=membro)

@bp_equipe.route("/equipe/<int:id>/remove", methods=["POST"])
def remove_member(id):
    remove_member = EquipeMembros.query.get(id)
    db.session.delete(remove_member)
    db.session.commit()