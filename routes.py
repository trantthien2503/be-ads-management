from flask import Blueprint, jsonify, request
from firebase_service import FirestoreCollection
import json
import ast
# Tạo blueprint với tên là "main"
main_bp = Blueprint('main', __name__)
# Định nghĩa route cho blueprint "main"

# Format route /api/${ tên table }/ ${các giao tác}

# Hàm thực hiện đăng kí
@main_bp.route('/api/update-by-fields', methods=['POST'])
def updateByFields():
    req = request.get_json()
    field = req.get('field')
    id_update = req.get('id')
    data_update = req.get('data_update')
    firestore = FirestoreCollection(field)
    update = firestore.update_data(id_update, data_update)
    return jsonify(update)



# Hàm thực hiện đăng kí
@main_bp.route('/api/users/register', methods=['POST'])
def registerUser():
    req = request.get_json() 
    user = {
        "email": req.get('email'),
        "password": req.get('password'),
        "phoneNumber": req.get('phoneNumber'),
        "role": req.get('role')
    }
    firestore = FirestoreCollection("users")
    data = firestore.registerUser(user)
    return jsonify(data)

# Hàm thực hiện đăng nhập
@main_bp.route('/api/users/login', methods=['POST'])
def loginUser():
    req = request.get_json() # Tạo đối tượng từ dữ liệu nhận được
    user = {
        "email": req.get('email'),
        "password": req.get('password'),
    }
    firestore = FirestoreCollection("users")
    data = firestore.loginUser(user)
    return jsonify(data)


 



