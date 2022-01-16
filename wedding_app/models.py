from wedding_app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return Guest.query.get(int(user_id))

class Guest(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    guest_group = db.Column(db.String)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True, nullable=False)
    attendance = db.Column(db.String())
    menu = db.Column(db.String())
    transportation = db.Column(db.String())
    
    def __repr__(self):
        return f"Guest('{self.name}', '{self.email}')"