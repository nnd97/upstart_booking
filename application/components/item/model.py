from sqlalchemy import (
    Column, String, Integer, BigInteger,
    DateTime, Date, Boolean, DECIMAL, Text,
    ForeignKey
)
from sqlalchemy.orm import *
from sqlalchemy.dialects.postgresql import UUID, JSONB

from application.database import db
from application.database.model import CommonModel

items_categories =  db.Table('items_categories',
                    db.Column('item_id', UUID(as_uuid=True), db.ForeignKey('item.id', ondelete='cascade', onupdate='cascade'), primary_key=True),
                    db.Column('category_id', UUID(as_uuid=True), db.ForeignKey('item_category.id', ondelete='cascade', onupdate='cascade'), primary_key=True))

class ItemCategory(CommonModel):
    __tablename__ = 'item_category'

    name = db.Column(String(50), nullable=False)

    def __repr__(self):
        return '<ItemCategory: {}>'.format(self.name)

class Item(CommonModel):
    __tablename__ = 'item'

    name = db.Column(String(255), nullable=False)
    priceEach = db.Column(DECIMAL() , nullable=False)
    itemCategory_id = db.Column(UUID(as_uuid=True), ForeignKey('item_category.id', onupdate='cascade', ondelete='cascade'))
    item_category = db.relationship("ItemCategory")

    def __repr__(self):
        return '<Item: {}>'.format(self.name)

