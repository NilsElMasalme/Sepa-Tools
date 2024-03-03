from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255), nullable=False)


    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

    def __repr__(self):
        return f'<Payment {self.id}>'
