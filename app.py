from flask import Flask, render_template
from apps.auth import auth
from apps.main import main
from apps.doctor import doctor
from extensions import db, cors
from api.api import api
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///db.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'this-is-secret')

# Initialize extensions
db.init_app(app)
cors.init_app(app)
migrate = Migrate(app, db)  # ✅ Added Flask-Migrate

# Register blueprints
app.register_blueprint(auth)
app.register_blueprint(main)
app.register_blueprint(doctor, url_prefix="/doctor")

# Initialize API
api.init_app(app)
if __name__ == "__main__":
    app.run(debug=True)
