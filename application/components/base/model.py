from sqlalchemy import (
    Column, String, Integer, BigInteger,
    Date, Boolean, Text, 
    ForeignKey
)
from sqlalchemy.dialects.postgresql import JSONB

from application.database import db
from application.database.model import CommonModel

class ConnectionApp(CommonModel):
    __tablename__ = 'connection_app'
    app_id = db.Column(String(16), unique=True, nullable=False)
    app_name = db.Column(String(100))
    secret_key = db.Column(String(128), nullable=False)
    type = db.Column(String(20)) # wekhook, call-api
    scope = db.Column(JSONB())
    permission = db.Column(JSONB())
    tenant_id = db.Column(String(24))
    tenant_name = db.Column(String(100))
    expired_at = db.Column(BigInteger)


class Configuration(CommonModel):
    __tablename__ = 'configuration'
    category = db.Column(String(50))
    app_key = db.Column(String(128))
    app_secret = db.Column(String(256))
    token = db.Column(Text())
    token_expired_at = db.Column(BigInteger)
    data = db.Column(JSONB())


class Notify(CommonModel):
    __tablename__ = 'notify'
    target = db.Column(String(20))
    action = db.Column(String(16))
    api_path = db.Column(String(255))
    message = db.Column(Text())
    