# -*- encoding: utf-8 -*-
from ext.database import database as db
from sqlalchemy import Integer, Float, String

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