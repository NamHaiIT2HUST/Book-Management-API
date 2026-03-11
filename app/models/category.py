from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from app.db.base import Base 

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String(250), nullable = False)
    description = Column(Text, nullable = False)

    #Relationship 1-n with Book
    books = relationship("Book", back_populates = "category")