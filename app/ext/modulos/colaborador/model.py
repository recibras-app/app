# -*- encoding: utf-8 -*-
from ext.database import database as db
from sqlalchemy import Integer, Float, String

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