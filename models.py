from sqlalchemy import Column,  Integer,  String,UniqueConstraint, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from operator import itemgetter
from datetime import datetime

Base = declarative_base()
metadata = Base.metadata

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, server_default=text("nextval('usuarios_id_seq'::regclass)"))
    nome = Column(String(150), nullable=False)
    senha = Column(String(250), nullable=False)


    def __init__(self,nome,senha):
        self.nome = nome
        self.senha = senha



