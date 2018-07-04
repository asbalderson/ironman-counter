from . import DB

class Tourny(DB.Model):
    __tablename__ = 'tourny'
    tournyid = DB.Column(DB.Integer, nullable=False, primary_key=True)
    name = DB.Column(DB.Text, nullable=False)
