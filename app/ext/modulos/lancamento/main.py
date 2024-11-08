from flask import Blueprint, request, redirect, render_template, url_for
from app.ext.database import db, LancamentoMaterial, Material, Equipe, EquipeMembros


bp_lancamentopeso = Blueprint("lancamentopeso", __name__, template_folder="templates")

@bp_lancamentopeso.route("/lancar_peso")
def index():
    equipe = Equipe.query.all()
    material = Material.query.all()
    return render_template("lancamento.html", equipe=equipe, material=material)