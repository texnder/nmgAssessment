from app import db


class Upload(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    vdoname = db.Column(db.String, unique=True, nullable=False)

