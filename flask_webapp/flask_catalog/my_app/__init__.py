from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C://sqlite//tmp//test.db'
db = SQLAlchemy(app)

app.secret_key = 'admin@123'

from my_app.catalog.views import catalog
app.register_blueprint(catalog)

db.create_all()