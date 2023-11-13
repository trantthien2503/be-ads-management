from flask import Blueprint, jsonify, request, redirect
from firebase_service import FirestoreCollection
from werkzeug.utils import secure_filename
from flask import current_app

import os
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
    try:
        if request.files:
            image = request.files["image"]

            # Kiểm tra xem tệp tồn tại hay không
            if image.filename == "":
                return jsonify({'message': 'Không có tệp được cung cấp'})

            # Kiểm tra phần mở rộng của tệp hợp lệ
            if not allowed_image_extension(image.filename):
                return jsonify({'message': 'Phần mở rộng tệp không được phép'})

            # Kiểm tra kích thước tệp hợp lệ
            image.seek(0, os.SEEK_END)
            file_size = image.tell()

            if not allowed_image_filesize(file_size):
                return jsonify({'message': 'Kích thước tệp vượt quá giới hạn cho phép'})

            # Tạo tên tệp an toàn
            filename = secure_filename(image.filename)

            # Thực hiện hoạt động lưu trữ
            storage_path = os.path.join(
                current_app.config["IMAGE_UPLOAD"], filename)
            image.save(storage_path)

            # Thực hiện hoạt động lưu trữ trên Firebase
            firestore = FirestoreCollection("images")
            response = firestore.upload_image(storage_path)

            return jsonify(response)
        else:
            return jsonify({'message': 'Không có tệp được cung cấp'})
    except Exception as e:
        return jsonify({'message': f'Lỗi không xác định: {e}'})


def allowed_image_filesize(filesize):
    return filesize <= current_app.config["MAX_IMAGE_FILESIZE"]


def allowed_image_extension(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].upper(
           ) in current_app.config["ALLOWED_IMAGE_EXTENSIONS"]
