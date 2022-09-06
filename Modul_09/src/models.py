from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from src.db import Base


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=True)
    birthday = Column('birthday', Date, nullable=True)
    email = Column('email', String(100), nullable=True)
    address = Column('address', String(300), nullable=True)
    phone_ = relationship('Phone', back_populates='contact_')


class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone = Column('phone', String(20), nullable=False)
    contacts_id = Column('contacts_id', ForeignKey('contacts.id', ondelete='CASCADE'), nullable=False)
    contact_ = relationship('Contact', back_populates='phone_')
