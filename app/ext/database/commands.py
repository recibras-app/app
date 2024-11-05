from ext.modulos.colaborador import model
from ext.modulos.equipe import model
from ext.modulos.material import model

from ext.database import database as db

def create_database():
    db.create_all()
    return "[AVISO] - Banco de dados criado!"

def drop_database():
    db.drop_all()
    return "[AVISO] - Banco de dados foi zerado!"