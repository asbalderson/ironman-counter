from . import DB

class Tourny(DB.model):
    __tablename__ = 'tourny'
    tournyid = DB.Column(DB.Integer, nullable=False, primarykey=True)
    name = DB.Column(DB.Text, nullable=False)
