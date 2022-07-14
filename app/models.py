from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def get_player(player_id):
    """Given an ID, get player

    Args:
        player_id (int): player unique identifier

    Returns:
        Player: Player object from database where ID matched
    """
    return Player.query.get(int(player_id))

class Player(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    nickname = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Player('{self.first_name}', '{self.nickname}', '{self.last_name}', '{self.email}')"

class Bar(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(100), unique=True, nullable=False)
    teams = db.relationship('Team', backref='bar', lazy=True)

    def __repr__(self):
        return f"Bar('{self.name}', '{self.address}')"

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    home_bar_id = db.Column(db.Integer, db.ForeignKey('bar.id'), nullable=False)

    def __repr__(self):
        return f"Team('{self.name}')"