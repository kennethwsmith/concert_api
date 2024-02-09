from database import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey, DateTime, Table
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship
from enums import BAND_GENRES

class User(Base):
    __tablename__='app_user'
    id=Column(Integer,primary_key=True)
    username=Column(String(25),unique=True)
    email=Column(String(80),unique=True)
    password=Column(Text,nullable=True)
    is_staff=Column(Boolean,default=False)
    is_active=Column(Boolean,default=False)
    # concerts=relationship('Concert',back_populates='concert')

    def __repr__(self):
        return f"<User {self.username}"

class Band(Base):
    __tablename__='band'
    id=Column(Integer,primary_key=True)
    name=Column(String(100),unique=True) 
    genre=Column(ChoiceType(choices=BAND_GENRES), default="ROCK")
    # concerts=relationship('Concert',back_populates='concert')

    def __repr__(self):
        return f"<Band {self.id}"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    building=Column(String(100)) #      Apt, office, suite, etc. (Optional)
    street=Column(String(100)) #        Street address     
    city=Column(String(100)) #          City
    state=Column(String(100)) #         State, province or prefecture
    zip_code=Column(String(100)) #      Zip code 
    country=Column(String(100)) #       Country

class Concert(Base):
    __tablename__='concert'
    id=Column(Integer,primary_key=True)
    setlist_url=Column(Text,nullable=True)
    showdate=Column(DateTime)
    venue=Column(String(100))
    address_id = Column(Integer,ForeignKey(Address.id),nullable=True)
    # band_id = Column(Integer,ForeignKey(Band.id))
    # user_id = Column(Integer,ForeignKey(User.id))

    def __repr__(self):
        return f"<Concert {self.id}"

class UserConcert(Base):
    __tablename__ = "user_concert_xref"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('app_user.id'))
    concert_id = Column(Integer, ForeignKey('concert.id'))

class BandConcert(Base):
    __tablename__ = "band_concert_xref"
    id = Column(Integer, primary_key=True)
    band_id = Column(Integer, ForeignKey('band.id'))
    concert_id = Column(Integer, ForeignKey('concert.id'))