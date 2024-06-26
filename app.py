# Import Modules for FLASK
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from routes import main_bp
from flask_mail import Mail

# Initialize Flask app
app = Flask(__name__)
CORS(app, support_credentials=True)

app.config["IMAGE_UPLOAD"] = "/FIDDL/images"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG", "JPG", "JPEG"]
app.config["MAX_IMAGE_FILESIZE"] = 1.5 * 1024 * 1024

# Initialize Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'trantthien2503@gmail.com'
app.config['MAIL_PASSWORD'] = 'Thuytrang2009'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

api = Api(app)

if __name__ == "__main__":
    app.register_blueprint(main_bp)
    app.run(debug=True)  # Make sure debug is false on production environment