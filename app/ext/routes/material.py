from flask import Blueprint, render_template, url_for


bp_material = Blueprint("material", __name__, template_folder="templates/material")

@bp_material.route("/material")
def index():
    #material = Material.query.all()
    return render_template("material.html", material="material")

@bp_material.route("/create", methods=["POST"])
def create():
    material = Material(request.form["sku"], request.form["nome"], request.form["valor"])
    db.session.add(material)
    db.session.commit()
    return redirect(url_for("index"))

@bp_material.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    material = Material.query.get(id)
    if request.method == "POST":
        material.sku = request.form["sku"]
        material.nome = request.form["nome"]
        material.valor = request.form["valor"]
        db.session.commit()
        return redirect(url_for("material"))
    return render_template("update.html", material=material)

@bp_material.route("/delete/<int:id>")
def delete(id):
    material = Material.query.get(id)
    db.session.delete(material)
    db.session.commit()
    return redirect(url_for("index"))