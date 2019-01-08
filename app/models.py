from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column, TIMESTAMP

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String)


class SignInRequest(Base):
    __tablename__ = 'sign_in_requests'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    token = Column(String)
    ip = Column(String)
    activated = Column(TIMESTAMP)
    expired = Column(TIMESTAMP)
