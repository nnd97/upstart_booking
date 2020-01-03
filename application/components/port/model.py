from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import (
    Column, String, Integer,
    DateTime, Date, Boolean,
    event, func, Text
)

from application.database import db



class Port(db.Model):
    __tablename__ = "port"
    id = db.Column(Integer(), primary_key=True, unique=True)
    port = db.Column(Integer(), nullable=False)
    server_name = db.Column(String(30))
    assigned_page = db.Column(String(255))
    tenant_id = db.Column(String(12))
    tenant_name = db.Column(String(100))
    coupon_prefix = db.Column(String(10))
    address = db.Column(String(255))
    note = db.Column(Text())
    
