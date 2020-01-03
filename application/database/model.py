import uuid
from sqlalchemy.dialects.postgresql import UUID
from application.database import db
from application.common.helper import now_timestamp

#from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Column, String, Integer,
    DateTime, Date, Boolean,
    event, func, BigInteger
)


def default_uuid():
    return str(uuid.uuid4())

def model_oncreate_listener(mapper, connection, instance):
    instance.created_at = now_timestamp()
    instance.updated_at = now_timestamp()
    
def model_onupdate_listener(mapper, connection, instance):
    instance.created_at = instance.created_at
    instance.updated_at = instance.updated_at
    if instance.deleted is True:
        instance.deleted_at = now_timestamp()

# CommonModel
# a common model using to add all below attributes into model class
# using CommonModel as argument of Model Class
class CommonModel(db.Model):
    __abstract__ = True
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=default_uuid)
    created_at = db.Column(BigInteger, index=True, default=now_timestamp())
    created_by = db.Column(UUID(as_uuid=True), nullable=True)
    created_by_name = db.Column(String)
    updated_at = db.Column(BigInteger, default=now_timestamp())
    updated_by = db.Column(UUID(as_uuid=True), nullable=True)
    updated_by_name = db.Column(String)
    deleted = db.Column(Boolean, default=False)
    deleted_by = db.Column(UUID(as_uuid=True), nullable=True)
    deleted_at = db.Column(BigInteger)
    deleted_by_name = db.Column(String)
    
event.listen(CommonModel, 'before_insert', model_oncreate_listener, propagate=True)
event.listen(CommonModel, 'before_update', model_onupdate_listener, propagate=True)