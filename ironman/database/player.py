from . import DB


class Player(DB.Model):
    __tablename__ = 'player'
    id = DB.Column(DB.Integer, nullable=False, primary_key=True)
    playerid = DB.Column(DB.Integer, nullable=False)
    wins = DB.Column(DB.Integer, nullable=False, default=0)
    tournyid = DB.Column(DB.Integer, DB.ForeignKey('tourny.tournyid'),
                         nullable=False)
