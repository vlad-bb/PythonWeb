from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from src.db import Base


class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column('phone', String(20), nullable=False)
    birthday = Column('birthday', Date, nullable=True)
    email = Column('email', String(30), nullable=True)
    address = Column('address', String(120), nullable=True)

