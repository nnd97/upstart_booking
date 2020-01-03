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
    date = db.Column(DateTime())
    slot = db.Column(Integer())
    note = db.Column(Text(), nullable=True)
    contact_id = db.Column(UUID(as_uuid=True), ForeignKey('contact.id', onupdate='cascade', ondelete='cascade'))
    contact = db.relationship("Contact")


    def __repr__(self):
        return '<Booking: {}>'.format(self.id)


class BookingPayment(CommonModel):
    __tablename__ = 'booking_payment'

    promotion_id = db.Column(String(), nullable=True)
    booking_id = db.Column(UUID(as_uuid=True), ForeignKey('booking.id', onupdate='cascade', ondelete='cascade'))
    booking = db.relationship("Booking")
    payment_amount = db.Column(DECIMAL() )




class BookingItem(CommonModel):
    __tablename__ = 'booking_item'

    booking_id = db.Column(UUID(as_uuid=True), ForeignKey('booking.id', onupdate='cascade', ondelete='cascade'))
    booking = db.relationship("Booking")
    # item_id = db.Column(UUID(as_uuid=True), ForeignKey('item.id', onupdate='cascade', ondelete='cascade'))
    # item = db.relationship("Item") // chứng từ không foreignkey vì dữ liệu chứng từ phải fixed tránh update theo từ bảng reference 
    item_name = db.Column(String(), nullable=False)
    # list_price = db.Column(DECIMAL() ) #khong can
    quantity = db.Column(Integer())
    note = db.Column(Text(), nullable=True)
    


