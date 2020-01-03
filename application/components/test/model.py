from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.schema import Sequence
from sqlalchemy import (
    Column, String, Integer,
    DateTime, Date, Boolean, DECIMAL, Text,
    ForeignKey
)
from application.database import db


class Test(db.Model):
    __tablename__ = "test"
    id          = db.Column(UUID(as_uuid=True), primary_key=True)
    name        = db.Column(String(50))
    image       = db.Column(String(255))
    price       = db.Column(DECIMAL(10,2))
    describe    = db.Column(Text())
    
    
# id_seq = Sequence('id_seq', start=1, increment=1)

class TestUser(db.Model):
    __tablename__ = "test_user"
    id          = db.Column(Integer, primary_key=True)
    name        = db.Column(String(100))
    password    = db.Column(String(255))
    image       = db.Column(String(255))
    role        = db.Column(String(10))
    salary      = db.Column(DECIMAL(10,2))
    

