from . import DB


class Player(DB.model):
    __tablename__ = 'player'
    playerid = DB.Column(DB.integer, nullable=False, primarykey=True)
    wins = DB.Column(DB.integer, nullable=False, default=0)
    tournyid = DB.Column(DB.integer, DB.ForeignKey('tourny.tournyid'),
                         nullable=False)
