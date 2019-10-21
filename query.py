from models import Usuario
from connection import Session
from flask import jsonify
import json

session = Session()

def list_user(id=None):
    try:
        if id:
            user = session.query(Usuario).filter(Usuario.id == id).first()
            dic = {
                'id' : user.id,
                'nome' : user.nome,
                'senha' : user.senha
            }
            return jsonify(dic)
        else:
            user = session.query(Usuario).all()
            users = []
            for user in user:
                dic = {
                    'id' : user.id,
                    'nome' : user.nome,
                    'senha' : user.senha
                }
                users.append(dic)
            return jsonify(users)
    except Exception as e:
        return jsonify({'erro':'Erro ao tentar listar.'}), e
    finally:
        session.close()

def create_user(user):
    try:
        session.add(user)
        session.refresh(user)
    except Exception as e:
        return jsonify({'error' : 'Erro ao tentar criar.'}), e

    finally:
        session.commit()
        session.close()

def update_user(id,user):
    try:
        session.query(Usuario).filter(Usuario.id == id).update({
            Usuario.nome : user.nome,
            Usuario.senha : user.senha
        }, synchronize_session=False)
    except Exception as e:
        return jsonify({'error' : 'Error ao tentar atualizar!'}), e
    finally:
        session.commit()
        session.close()

def del_user(id):
    try:
        user = session.query(Usuario).filter(Usuario.id==id).first()
        session.delete(user)
        session.commit()
    except Exception as e:
        return jsonify({'error' : 'Error ao tentar deletar!'}), e
    finally:
        session.commit()
        session.close()




