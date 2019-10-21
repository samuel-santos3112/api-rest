from flask import Flask,jsonify,request
import connection
from models import Usuario
import query

app = Flask(__name__)


@app.route('/user/<int:id>',methods=['GET'])
def user(id):
    user = query.list_user(id)

    return user

@app.route('/users',methods=['GET'])
def users():
    users = query.list_user()

    return users


@app.route('/user',methods=['POST'])
def save_user():
    data = request.get_json()
    user = Usuario(data['nome'],data['senha'])
    query.create_user(user)

    return jsonify(data), 201

@app.route('/user/<int:id>',methods=['PUT'])
def change_lang(id):
    data = request.get_json()
    user = Usuario(data['nome'],data['senha'])
    query.update_user(id,user)
  
    return jsonify(dev), 200
    #return jsonify ({'error' : 'Not Found'}), 404

@app.route('/user/<int:id>', methods=['DELETE'])
def remove_user(id):
    query.del_user(id)

    return jsonify({'message' : 'successfully removed'}), 200

if __name__ == '__main__':
    app.run(debug=True)

