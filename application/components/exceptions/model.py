from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import (
    Column, String, Integer,
    BigInteger, Date, Boolean,
    event, func, Text
)
from sqlalchemy.dialects.postgresql import JSONB
from application.database import db
from application.common.helper import now_timestamp

class Exceptions(db.Model):
    __tablename__ = "exception"
    id = db.Column(Integer(), primary_key=True, unique=True)
    app_type = db.Column(String(30))
    source_id = db.Column(String(50))
    timestamp = db.Column(BigInteger(), default=now_timestamp())
    details = db.Column(JSONB())
    
