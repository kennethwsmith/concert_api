from database import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey, DateTime, Table, Enum
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.orm import relationship
from pydantic import BaseModel
import enum

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str | None = None

class AuthUser(BaseModel):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool | None = None

class AuthUserInDB(AuthUser):
    hashed_password: str

class User(Base):
    __tablename__='app_user'
    id=Column(Integer,primary_key=True)
    username=Column(String(25),unique=True)
    email=Column(String(80),unique=True)
    password=Column(Text,nullable=True)
    is_staff=Column(Boolean,default=False)
    is_active=Column(Boolean,default=False)
    def __repr__(self):
        return f"<User {self.username}"

class BandGenre_enum(enum.Enum):
    ROCK = "Rock"
    COUNTRY = "Country"
    POP = "Pop"
    CLASSICAL = "Classical"
    JAZZ = "Jazz"
    BLUES = "Blues"
    RNB = "R&B"
    HIPHOP = "Hip-Hop"
    ELECTRONIC = "Electronic"

class Band(Base):
    __tablename__='band'
    id=Column(Integer,primary_key=True)
    name=Column(String(100),unique=True)
    genre = Column(Enum(BandGenre_enum),default="ROCK")
    def __repr__(self):
        return f"<Band {self.id}"

class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    building=Column(String(100),nullable=True) #      Apt, office, suite, etc. (Optional)
    street=Column(String(100)) #        Street address     
    city=Column(String(100)) #          City
    state=Column(String(100)) #         State, province or prefecture
    zip_code=Column(String(100)) #      Zip code 
    country=Column(String(100)) #       Country
    def __repr__(self):
        return f"<Address {self.id}"

class Venue(Base):
    __tablename__ = "venue"
    id = Column(Integer, primary_key=True)
    name=Column(String(100))
    building=Column(String(100),nullable=True) #      Apt, office, suite, etc. (Optional)
    street=Column(String(100)) #        Street address     
    city=Column(String(100)) #          City
    state=Column(String(100)) #         State, province or prefecture
    zip_code=Column(String(100)) #      Zip code 
    country=Column(String(100)) #       Country
    def __repr__(self):
        return f"<Venue {self.id}"

class Concert(Base):
    __tablename__='concert'
    id=Column(Integer,primary_key=True)
    setlist_url=Column(Text,nullable=True)
    showdate=Column(DateTime)
    venue_id = Column(Integer,ForeignKey(Venue.id),nullable=True)
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