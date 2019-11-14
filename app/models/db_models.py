from . import db


class Name(db.Model):
    """Table to get the name from npm"""

    id = db.Column(db.Integer, primary_key=True)
    first_word = db.Column(db.String(256))
    second_word = db.Column(db.String(256))
    third_word = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime(timezone=False))
