from flask import Blueprint, jsonify, request
from firebase_service import FirestoreCollection

import os
# Tạo blueprint với tên là "main"
main_bp = Blueprint('main', __name__)
# Định nghĩa route cho blueprint "main"


# Hàm thực hiện tạo dữ liệu
@main_bp.route('/api/get-data-by-fields', methods=['POST'])
def getByFields():
    req = request.get_json()
    field = req.get('field')
    firestore = FirestoreCollection(field)
    get = firestore.get_all_data()
    return jsonify(get)


# Hàm thực hiện tạo dữ liệu
@main_bp.route('/api/add-data-by-fields', methods=['POST'])
def addByFields():
    req = request.get_json()
    field = req.get('field')
    data = req.get('data')
    firestore = FirestoreCollection(field)
    add_data = firestore.add_data(data)
    return jsonify(add_data)


# Hàm thực hiện cập nhật dữ liệu
@main_bp.route('/api/update-by-fields', methods=['POST'])
def updateByFields():
    req = request.get_json()
    field = req.get('field')
    id_update = req.get('id')
    data_update = req.get('data_update')
    firestore = FirestoreCollection(field)
    update = firestore.update_data(id_update, data_update)
    return jsonify(update)


# Hàm thực hiện cập nhật dữ liệu
@main_bp.route('/api/search-by-fields', methods=['POST'])
def searchByFields():
    req = request.get_json()
    field = req.get('field')
    search_field = req.get('search_field')
    search_value = req.get('search_value')
    firestore = FirestoreCollection(field)
    find = firestore.search_data(search_field, search_value)
    return jsonify(find)


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
    req = request.get_json()  # Tạo đối tượng từ dữ liệu nhận được
    user = {
        "email": req.get('email'),
        "password": req.get('password'),
    }
    firestore = FirestoreCollection("users")
    data = firestore.loginUser(user)
    return jsonify(data)


@main_bp.route('/api/images/upload-image',  methods=["POST"])
def upload_image():
    if request.files:
        image = request.files["image"]
        # Upload lên Firebase
        firestore = FirestoreCollection("images") 
        upload_image = firestore.upload_image(image)
    
        return upload_image
    else:
        return jsonify({'message': 'No file provided'})
