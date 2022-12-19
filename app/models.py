from app import db, login_manager
from flask_login import UserMixin
from datetime import datetime as dt

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
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    date_created = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    
    def __repr__(self) -> str:
        return 'Player({id}, {fn}, {nn}, {ln}, {email}, Activity Status: {status}, Created: {created})'.format(
            id=self.id,
            fn=self.first_name,
            nn=self.nickname,
            ln=self.last_name,
            email=self.email,
            status=self.is_active,
            created=self.date_created
        )
        
class Bar(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(10), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    date_created = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    teams = db.relationship('Team', backref='bar', lazy=True)

    def __repr__(self) -> str:
        return 'Bar({id}, {name}, {address}, {phone}, Activity Status: {status}, Created: {created}, {teams})'.format(
            id=self.id,
            name=self.name,
            address=self.address,
            phone=self.phone,
            status=self.is_active,
            created=self.date_created,
            teams=self.teams
        )

class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    date_created = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    home_bar_id = db.Column(db.Integer, db.ForeignKey('bar.id'), nullable=False)

    def __repr__(self) -> str:
        return 'Team({id}, {name}, Activity Status: {status}, Created: {created}, Home Bar ID: {home_bar_id})'.format(
            id=self.id,
            name=self.name,
            status=self.is_active,
            created=self.date_created,
            home_bar_id=self.home_bar_id
        )

class SeasonName(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    seasons = db.relationship('Season', backref='seasonName', lazy=True)

    def __repr__(self) -> str:
        return 'SeasonName({id}, {name}, Created: {created}, Seasons: {seasons})'.format(
            id=self.id,
            name=self.name,
            created=self.date_created,
            seasons=self.seasons,
        )

class Season(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=dt.utcnow)
    season_name_id = db.Column(db.Integer, db.ForeignKey('seasonName.id'), nullable=False)

    def __repr__(self) -> str:
        return 'Season({id}, {season_name_id}, {year}, Created: {created})'.format(
            id=self.id,
            season_name_id=self.season_name_id,
            year=self.year,
            created=self.date_created
        )