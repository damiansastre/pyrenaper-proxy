from .db import db

class User(db.Document):
    user_id = db.IntField(required=True)
    status = db.StringField(required=False)
    data = db.DictField(required=False)