# Import Modules for FLASK
from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from routes import main_bp

# Initialize Flask app
app = Flask(__name__)
CORS(app, support_credentials=True)
api = Api(app)

if __name__ == "__main__":
    app.register_blueprint(main_bp)
    app.run(debug=True) # Make sure debug is false on production environment