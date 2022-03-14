from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cors import CORS
from config import DB_URI, KEY

app = Flask(__name__, static_url_path='', static_folder='')
CORS(app)
app.config["MONGODB_HOST"] = DB_URI
app.config['SECRET_KEY'] = KEY
db = MongoEngine(app)
