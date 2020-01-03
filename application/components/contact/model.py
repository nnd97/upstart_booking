from sqlalchemy import (
    Column, String, Integer, BigInteger,
    DateTime, Date, Boolean, DECIMAL, Text,
    ForeignKey
)
from sqlalchemy.orm import *
from sqlalchemy.dialects.postgresql import UUID, JSONB

from application.database import db
from application.database.model import CommonModel


class Contact(CommonModel):
    __tablename__ = 'contact'

    contact_name = db.Column(String(255))
    phone = db.Column(String(50), unique=True, nullable=False)
    gender = db.Column(String(30), nullable=True)
    birthday = db.Column(String(30), nullable=True)

    bdate = db.Column(Integer()) # date of birthday
    bmonth = db.Column(Integer()) # month of birthday
    byear = db.Column(Integer(), index=True) # year of birthday

    email = db.Column(String(100), unique=True, nullable=True, index=True)
    email_other = db.Column(String(100), nullable=True)

    phone = db.Column(String(50), unique=True, nullable=False, index=True)
    phone_other = db.Column(String(50), nullable=True)

    address_city = db.Column(String(30), nullable=True)
    address_code = db.Column(String(30), nullable=True)
    address_country = db.Column(String(30), nullable=True)
    address_state = db.Column(String(30), nullable=True)
    address_street = db.Column(String(250), nullable=True)
    address_pobox = db.Column(String(30), nullable=True)
    def __repr__(self):
        return '<ContactCategory: {}>'.format(self.contact_name)


