from database import Base
from sqlalchemy import Column, Integer, Boolean, Text, String, ForeignKey, DateTime
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

class Concert(Base):
    __tablename__='concert'
    id=Column(Integer,primary_key=True)
    setlist_url=Column(Text,nullable=True)
    showdate=Column(DateTime)
    band_id = Column(Integer,ForeignKey(Band.id))
    user_id = Column(Integer,ForeignKey(User.id))

    def __repr__(self):
        return f"<Concert {self.id}"

# class Banana(Base):
#     __tablename__='banana'
#     id=Column(Integer,primary_key=True)
#     name=Column(String(100),unique=True) 
#     ## concert fields here...
#     # band_id = Column(Integer,ForeignKey(Band.id))
#     # user_id = Column(Integer,ForeignKey(User.id))

#     def __repr__(self):
#         return f"<Banana {self.id}"