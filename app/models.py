from app import db

class Player(db.Model):
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