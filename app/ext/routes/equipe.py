from flask import Blueprint, render_template, url_for


bp_equipe = Blueprint("equipe", __name__, template_folder="templates/equipe")

@bp_equipe.route("/equipe")
def index():
    #equipe = Equipe.query.all()
    return render_template("equipe.html", equipe="equipe")

@bp_equipe.route("/create", methods=["POST"])
def create():
    equipe = Equipe(request.form["sku"], request.form["lider"], request.form["cor"])
    db.session.add(equipe)
    db.session.commit()
    return redirect(url_for("index"))

@bp_equipe.route("/detalhes/<int:id>")
def details(id):
    equipe = Equipe.query.get(id)
    return render_template("detalhes.html", equipe=equipe)

@bp_equipe.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    equipe = Equipe.query.get(id)
    if request.method == "POST":
        equipe.sku = request.form["sku"]
        equipe.lider = request.form["lider"]
        equipe.cor = request.form["cor"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("update.html", equipe=equipe)

@bp_equipe.route("/delete/<int:id>")
def delete(id):
    equipe = Equipe.query.get(id)
    db.session.delete(equipe)
    db.session.commit()
    return redirect(url_for("index"))