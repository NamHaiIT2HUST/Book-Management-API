from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.base import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(255), nullable = False, index = True)
    description = Column(Text, nullable = False)
    published_year = Column(Integer, nullable = False)
    
    author_id = Column(Integer, ForeignKey("authors.id", ondelete = "RESTRICT"), nullable = False)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete = "RESTRICT"), nullable = False)

    cover_image = Column(String(255), nullable = True) #save path, example: "static/covers/xxx.jpg"

    created_at = Column(DateTime(timezone = True), server_default = func.now(), nullable = False)
    updated_at = Column(DateTime(timezone = True), server_default = func.now(), onupdate = func.now(), nullable = False)

    #Relationship Author, Category
    author = relationship("Author", back_populates = "book")
    category = relationship("Category",back_populates = "book")