from sqlalchemy.dialects.postgresql import UUID
from application.database import db
from application.database.model import CommonModel


class Country(CommonModel):
    __tablename__ = "country"
    country_name = db.Column(db.String(50))
    code = db.Column(db.String(50))
    cities = db.relationship("City", order_by="City.id", cascade="all, delete-orphan")
    
    

class City(CommonModel):
    __tablename__ = "city"
    city_name = db.Column(db.String(50))
    code = db.Column(db.String(50))
    country_id = db.Column(UUID(as_uuid=True), db.ForeignKey("country.id"))
    country = db.relationship("Country")
