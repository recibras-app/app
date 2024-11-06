from flask import Blueprint, request, redirect, render_template, url_for
from app.ext.database import db, Material


bp_material = Blueprint("material", __name__, template_folder="templates")

@bp_material.route("/material")
def index():
    material = Material.query.all()
    return render_template("material.html", material=material)

@bp_material.route("/material/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        material = Material(request.form["sku"], request.form["nome"], request.form["valor"])
        db.session.add(material)
        db.session.commit()
        material = Material.query.all()
        return render_template("material.html", material=material)
    return render_template("material_create.html")

@bp_material.route("/material/update/<int:id>", methods=["GET", "POST"])
def update(id):
    material = Material.query.get(id)
    if request.method == "POST":
        material.sku = request.form["sku"]
        material.nome = request.form["nome"]
        material.valor = request.form["valor"]
        db.session.commit()
        material = Material.query.all()
        return render_template("material.html", material=material)
    return render_template("material_update.html", material=material)

@bp_material.route("/material/delete/<int:id>")
def delete(id):
    material = Material.query.get(id)
    db.session.delete(material)
    db.session.commit()
    material = Material.query.all()
    return render_template("material.html", material=material)