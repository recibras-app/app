from flask import Blueprint, request, redirect, render_template, url_for
from app.ext.database import db, Equipe, EquipeMembros


bp_equipe = Blueprint("equipe", __name__, template_folder="templates")

@bp_equipe.route("/equipe")
def index():
    equipe = Equipe.query.all()
    return render_template("equipe.html", equipe=equipe)

@bp_equipe.route("/equipe/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        equipe = Equipe(request.form["sku"], request.form["lider"], request.form["cor"])
        db.session.add(equipe)
        db.session.commit()
        equipe = Equipe.query.all()
        return render_template("equipe.html", equipe=equipe)
    return render_template("equipe_create.html")

@bp_equipe.route("/equipe/detalhes/<int:id>")
def details(id):
    equipe = Equipe.query.get(id)
    return render_template("equipe_detalhes.html", equipe=equipe)

@bp_equipe.route("/equipe/update/<int:id>", methods=["GET", "POST"])
def update(id):
    equipe = Equipe.query.get(id)
    if request.method == "POST":
        equipe.sku = request.form["sku"]
        equipe.lider = request.form["lider"]
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