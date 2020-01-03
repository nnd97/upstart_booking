from sqlalchemy import (
    Column, String, Integer, BigInteger,
    DateTime, Date, Boolean, DECIMAL, Text,
    ForeignKey, Numeric
)
from sqlalchemy.orm import *
from sqlalchemy.dialects.postgresql import UUID, JSONB

from application.database import db
from application.database.model import CommonModel



class Booking(CommonModel):
    __tablename__ = 'booking'

    phone = db.Column(String(50), nullable=False, index=True)
    date = db.Column(DateTime(), nullable=False)
    slot = db.Column(Integer(), nullable=False)
    note = db.Column(Text(), nullable=True)
    contact_id = db.Column(UUID(as_uuid=True), ForeignKey('contact.id', onupdate='cascade', ondelete='cascade'))
    contact = db.relationship("Contact")
    booking_items = db.relationship("BookingItem")


    def __repr__(self):
        return '<Booking: {}>'.format(self.id)


class BookingPayment(CommonModel):
    __tablename__ = 'booking_payment'

    booking_id = db.Column(UUID(as_uuid=True), ForeignKey('booking.id', onupdate='cascade', ondelete='cascade'))
    promotion_id = db.Column(String(), nullable=True)
    payment_id = db.Column(UUID(as_uuid=True), ForeignKey('payment.id'))
    payment_method = db.relationship('Payment')
    payment_amount = db.Column(DECIMAL())

class Payment(CommonModel):
    __tablename__ = 'payment'

    method = db.Column(String())




class BookingItem(CommonModel):
    __tablename__ = 'booking_item'

    booking_id = db.Column(UUID(as_uuid=True), ForeignKey('booking.id', onupdate='cascade', ondelete='cascade'))
    # booking = db.relationship("Booking")
    item_id = db.Column(String())
    item_name = db.Column(String())
    quantity = db.Column(Integer())
    note = db.Column(Text(), nullable=True)
    # item = db.relationship("Item") chứng từ không foreignkey vì dữ liệu chứng từ phải fixed tránh update theo từ bảng reference 
    


