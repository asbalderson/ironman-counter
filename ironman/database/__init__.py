"""The SQLAlchemy database."""
from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

def create_tables():
    DB.create_all()