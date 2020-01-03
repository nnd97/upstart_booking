from sqlalchemy import (
    Column, String, Integer, DateTime, Date, Boolean, DECIMAL, Text, ForeignKey, UniqueConstraint
)
#from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.dialects.postgresql import JSONB

#from sqlalchemy.orm import relationship, backref

from application.database import db
from application.database.model import CommonModel
# from application.components.workstation.model import Workstation
# from application.components.currency.model import Currency
from application.components.contact.model import Contact
# from application.components.account.model import Account


def default_user_config():
    data = {
        'show_navbar': True,
        'theme_color': '#315294'
    }
    return data


# workstations_users = db.Table('workstations_users',
#                        db.Column('user_id', UUID(as_uuid=True), db.ForeignKey('user.id', ondelete=None), primary_key=True),
#                        db.Column('workstation_id', UUID(as_uuid=True), db.ForeignKey('workstation.id', ondelete=None), primary_key=True))


roles_users = db.Table('roles_users',
                       db.Column('user_id', UUID(as_uuid=True), db.ForeignKey('user.id', ondelete='cascade'), primary_key=True),
                       db.Column('role_id', UUID(as_uuid=True), db.ForeignKey('role.id', onupdate='cascade'), primary_key=True))


class Role(CommonModel):
    __tablename__ = 'role'
    role_code = db.Column(Integer(), index=True, nullable=True)
    role_name = db.Column(String(100), index=True, nullable=False, unique=True)
    display_name = db.Column(String(255), nullable=False)
    description = db.Column(String(255))
    permissions = db.relationship("Permission", order_by="Permission.id", cascade="all")


class User(CommonModel):
    __tablename__ = 'user'
    display_name = db.Column(String(255), nullable=True)
    phone = db.Column(String(50), unique=True, nullable=True)
    email = db.Column(String(100), unique=True, nullable=True)
    birthday = db.Column(DateTime())
    
    roles = db.relationship("Role", secondary=roles_users, cascade="save-update", single_parent=True)
    # workstations = db.relationship("Workstation", secondary=workstations_users, cascade="save-update", single_parent=True,
    #                 backref=backref('users', cascade='all'))

    phone_other = db.Column(String(50), nullable=True)
    email_other = db.Column(String(100), nullable=True)
    cal_color = db.Column(String(25), nullable=True, default='#E6FAD8')
    reports_to_id = db.Column(UUID(as_uuid=True), nullable=True)
    is_admin = db.Column(Boolean(), default=False)
    # currency_id = db.Column(UUID(as_uuid=True), ForeignKey('currency.id'), nullable=True)
    # currency = db.relationship("Currency")
    
    contact_id = db.Column(UUID(as_uuid=True), ForeignKey('contact.id'), nullable=True)
    contact = db.relationship("Contact")
    
    description = db.Column(Text(), nullable=True)
    title = db.Column(String(50), nullable=True)
    department = db.Column(String(50), nullable=True)
    
    fax = db.Column(String(50), nullable=True)
    status = db.Column(String(50), nullable=True)
    signature = db.Column(Text(), nullable=True)
    address_street = db.Column(String(150), nullable=True)
    address_city = db.Column(String(100), nullable=True)
    address_state = db.Column(String(100), nullable=True)
    address_country = db.Column(String(25), nullable=True)
    address_postalcode = db.Column(String(10), nullable=True)
    tz = db.Column(String(30), nullable=True)
    holidays = db.Column(String(60), nullable=True)
    namedays = db.Column(String(60), nullable=True)
    workdays = db.Column(String(30), nullable=True)
    weekstart = db.Column(Integer(), nullable=True)
    date_format = db.Column(String(200), nullable=True)
    hour_format = db.Column(String(30), nullable=True)
    start_hour = db.Column(String(30), nullable=True)
    end_hour = db.Column(String(30), nullable=True)
    is_owner = db.Column(String(100), nullable=True)
    activity_view = db.Column(String(200), nullable=True)
    lead_view = db.Column(String(200), nullable=True)
    user_image = db.Column(String(250), nullable=True)
    internal_mailer = db.Column(Boolean(), nullable=True, default=True)
    reminder_interval = db.Column(String(100), nullable=True)
    reminder_next_time = db.Column(String(100), nullable=True)
    theme = db.Column(String(100), nullable=True)
    language = db.Column(String(36), nullable=True)
    time_zone = db.Column(String(200), nullable=True)
    user_preferences = db.Column(Text(), nullable=True)
    currency_grouping_pattern = db.Column(String(100))
    currency_decimal_separator = db.Column(String(2))
    currency_grouping_separator = db.Column(String(2))
    currency_symbol_placement = db.Column(String(20))
    no_of_currency_decimals = db.Column(String(2))
    truncate_trailing_zeros = db.Column(Boolean())
    dayoftheweek = db.Column(String(100))
    callduration = db.Column(String(100))
    othereventduration = db.Column(String(100)) 
    calendarsharedtype = db.Column(String(100))
    default_record_view = db.Column(String(10))
    defaulteventstatus = db.Column(String(50))
    defaultactivitytype = db.Column(String(50))
    hidecompletedevents = db.Column(Integer())
    defaultcalendarview = db.Column(String(100))
    config_data = db.Column(JSONB(), default=default_user_config)
    
    def __repr__(self):
        """ Show user object info. """
        return '<User: {}>'.format(self.id)
    
    def has_role(self, role):
        if isinstance(role, str):
            return role in (role.role_name for role in self.roles)
        else:
            return role in self.roles
    
    def add_role(self, role):
        pass
    
    def remove_role(self,role):
        pass
    
class Permission(CommonModel):
    __tablename__ = 'permission'
    role_id = db.Column(UUID(as_uuid=True), ForeignKey('role.id'), nullable=True)
    subject = db.Column(String,index=True)
    permission = db.Column(String)
    value = db.Column(Boolean, default=False)
    __table_args__ = (UniqueConstraint('role_id', 'subject', 'permission', name='uq_permission_role_subject_permission'),)


