from . import db

class signup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(150), nullable=False)
    lname = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(550), nullable=False)

# class Purchase(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), db.ForeignKey('user.email'), nullable=False)
#     item_name = db.Column(db.String(100), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     purchase_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
#     amount = db.Column(db.Float, nullable=False)

class staff_signup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(150), nullable=False)
    lname = db.Column(db.String(150), nullable=False)
    designation = db.Column(db.String(150), nullable =False)
    age = db.Column(db.Integer, nullable=False)
    sex = db.Column(db.String(10), nullable=False)
    contact_number = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(550), nullable=False)
