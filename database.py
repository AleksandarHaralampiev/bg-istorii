from flask_sqlalchemy import SQLAlchemy
from main import db, Msg, app

with app.app_context():
    db.create_all()
    