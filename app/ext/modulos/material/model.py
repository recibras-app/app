# -*- encoding: utf-8 -*-
from ext.database import database as db
from sqlalchemy import Integer, Float, String

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